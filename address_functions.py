import hashlib
import hmac 
import codecs
import struct

from ecdsa.ecdsa import int_to_string, string_to_int 
from pbkdf2 import PBKDF2
from ecdsa_functions import *

BASE58=b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

CHARSET = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"

OP_DUP = b'\x76'
OP_EQUALVERIFY = b'\x88'
OP_HASH160 = b'\xa9'
OP_CHECKSIG = b'\xac'
OP_EQUAL = b'\x87'
OP_HASH160 = b'\xa9'
OP_0 = b'\x00'


def hash256(secret):
	return hashlib.sha256(hashlib.sha256(secret).digest()).digest()

def hash160(secret):
	return hashlib.new('ripemd160', hashlib.sha256(secret).digest()).digest()

def seed_to_master(seed, passphrase, derivation_path, hardened_items, total_addresses, address_type, testnet):
	pbkdf2_result=PBKDF2.hexread(PBKDF2(seed, 'mnemonic'+passphrase, 
		iterations=2048, macmodule=hmac, digestmodule=hashlib.sha512), 64)
	hmac_hash= hmac.new(key=b"Bitcoin seed", msg=codecs.decode(pbkdf2_result, 'hex'), digestmod=hashlib.sha512).digest()
	master_pk, master_cc = hmac_hash[:32], hmac_hash[32:]
	master_pubkey=S256Point.sec((string_to_int(master_pk))*G)
	return path_gen_keylist(master_cc,master_pk, master_pubkey, derivation_path,
		hardened_items,total_addresses, address_type, testnet)

class Keylevel:
	def __init__(self,chaincode, priv_key, pub_key, index, hardened, depth, fingerprint, address_type, testnet):
		self.chaincode=chaincode
		self.priv_key=priv_key
		self.pub_key=pub_key
		self.index=index
		self.hardened=hardened
		self.depth=depth
		self.fingerprint=fingerprint

		self.address_type=address_type

		self.testnet=testnet


	def CKDpriv(self):
		if self.hardened == True:
			i= 2147483648+self.index 
			i_str=struct.pack('>L',i)
			child_L_MPK=b'\x00'+self.priv_key+i_str

		else:
			i= self.index 
			i_str=struct.pack('>L',i)
			child_L_MPK=self.pub_key+i_str 
		child_L_MPKhmac=hmac.new(key=self.chaincode, msg=child_L_MPK , digestmod=hashlib.sha512).digest()
		child_LPhml, output_chaincode = child_L_MPKhmac[:32], child_L_MPKhmac[32:]
		child_LPhml_int=(string_to_int(child_LPhml))
		master_pk_int=(string_to_int(self.priv_key))
		presecret=child_LPhml_int+master_pk_int
		return (b'\x00'*32 + int_to_string(presecret% CURVE_ORDER))[-32:]

	def CKCpriv(self):
		if self.hardened == True:
			i= 2147483648+self.index 
			i_str=struct.pack('>L',i)
			child_L_MPK=b'\x00'+self.priv_key+i_str

		else:
			i= self.index 
			i_str=struct.pack('>L',i)
			child_L_MPK=self.pub_key+i_str
		child_L_MPKhmac=hmac.new(key=self.chaincode, msg=child_L_MPK , digestmod=hashlib.sha512).digest()
		output_chaincode = child_L_MPKhmac[32:]
		return bytes(output_chaincode)
		
	def pubkey(self):
		pubpoint =int.from_bytes(self.CKDpriv(), byteorder='big')*G
		return bytes(S256Point.sec(pubpoint))

	def fprint(self):
		identifier=(hash160(self.pub_key))[:4]
		return bytes(identifier)

	def xprv(self):
		if self.address_type == 'p2wpkh-p2sh':
			if self.testnet== True:
				prefix=b'\x04\x4A\x4E\x28'
			else:
				prefix=b'\x04\x9D\x78\x78'
		elif self.address_type == 'p2wpkh':
			if self.testnet== True:
				prefix=b'\x04\x5F\x18\xBC'
			else:
				prefix=b'\x04\xB2\x43\x0C'
		elif self.address_type == 'p2wsh':
			if self.testnet== True:
				prefix=b'\x02\x57\x50\x48'
			else:
				prefix=b'\x02\xAA\x7A\x99'

		elif self.testnet==True:
			prefix=b'\x04\x35\x83\x94'
		else:
			prefix=b'\x04\x88\xAD\xE4'

		xprvraw=prefix+bytes([self.depth])+self.fingerprint+bytes.fromhex(format(self.index, 'x').rjust(8, '0'))+self.CKCpriv()+b'\x00'+self.CKDpriv()
		checksum = hash256(xprvraw)[:4]
		xprvfull=xprvraw+checksum
		return encode_base58(xprvfull)

	def xpub(self):
		if self.address_type == 'p2wpkh-p2sh':
			if self.testnet== True:
				prefix=b'\x04\x4A\x52\x62'
			else:
				prefix=b'\x04\x9D\x7C\xB2'
		elif self.address_type == 'p2wpkh':
			if self.testnet== True:
				prefix=b'\x04\x5F\x1C\xF6'
			else:
				prefix=b'\x04\xB2\x47\x46'
		elif self.address_type == 'p2wsh':
			if self.testnet== True:
				prefix=b'\x02\x42\x89\xEF'
			else:
				prefix=b'\x02\xAA\x7E\xD3'

		elif self.testnet==True:
			prefix=b'\x04\x35\x87\xCF'
		else:
			prefix=b'\x04\x88\xB2\x1E'

		xpubraw=prefix+bytes([self.depth])+self.fingerprint+bytes.fromhex(format(self.index, 'x').rjust(8, '0'))+self.CKCpriv()+self.pubkey()
		checksum= hash256(xpubraw)[:4]
		xpubfull=xpubraw+checksum
		return encode_base58(xpubfull)

def path_gen_keylist(master_cc, master_pk,master_pubkey, index_list, hardened_list,total_keys, address_type, testnet):
	depth=1
	inputs=[master_cc, master_pk, master_pubkey, b'\x00\x00\x00\x00']

	for index_str in index_list:
		if depth== 1:
			getprint=Keylevel(inputs[0], inputs[1], inputs[2], int(index_str),hardened_list[depth], depth, inputs[3], address_type, testnet)
			inputs[3]=getprint.fprint()
			master_key_data=Keylevel(inputs[0], inputs[1], inputs[2], int(index_str),hardened_list[depth], depth, inputs[3], address_type, testnet)
			inputs=[master_key_data.CKCpriv(),master_key_data.CKDpriv(), master_key_data.pubkey(),master_key_data.fprint()]
		else:
			master_key_data=Keylevel(inputs[0], inputs[1], inputs[2], int(index_str),hardened_list[depth], depth, inputs[3], address_type, testnet)
			inputs=[master_key_data.CKCpriv(),master_key_data.CKDpriv(), master_key_data.pubkey(),master_key_data.fprint()]
		xprv=master_key_data.xprv()
		xpub=master_key_data.xpub()
		depth+=1
		gen_fp=Keylevel(inputs[0], inputs[1], inputs[2], int(index_str),hardened_list[depth], depth, inputs[3], address_type, testnet)
		inputs[3]=gen_fp.fprint()
	key_index=0
	key_result=[]
	for key in range(0, total_keys):
		hardened_key=(hardened_list[depth])
		index_key_data=Keylevel(inputs[0],inputs[1], inputs[2], key, hardened_key, depth,inputs[3], address_type, testnet)
		path_pubkey=index_key_data.pubkey()
		path_private=indv_priv_key(index_key_data.CKDpriv(), testnet)
		privatehex=index_key_data.CKDpriv().hex()
		if address_type=='p2pkh':
			public=indv_P2PKH_pub_key(index_key_data.pubkey(), testnet)
			script_pub=p2pkh_script(index_key_data.pubkey()) 
		
		elif address_type=='p2sh':
			redeemscript=p2sh_redeemscript(index_key_data.pubkey())
			public=indv_P2SH_pub_key(redeemscript, testnet)
			script_pub=p2sh_script(redeemscript)
			signscript=(bytes([len(redeemscript)])+redeemscript).hex()
		
		elif address_type=='p2wpkh-p2sh':
			public=indv_P2WPKH_P2SH_pub_key(index_key_data.pubkey(), testnet)
			script_pub=p2sh_script(index_key_data.pubkey())
			redeemscript=p2wpkh_p2sh_redeemscript(index_key_data.pubkey())
			signscript=('1976a9'+redeemscript[6:]+'88ac')

		elif address_type=='p2wpkh':
			public=indv_P2WPKH_pub_key(index_key_data.pubkey(), testnet)
			script_pub=p2wpkh_script(index_key_data.pubkey())
			signscript=('1976a9'+script_pub[4:]+'88ac')
		
		elif address_type=='p2wsh':
			redeemscript=p2sh_redeemscript(index_key_data.pubkey())
			public=indv_P2WSH_pub_key(redeemscript, testnet)
			script_pub=p2wsh_script(index_key_data.pubkey())
			signscript=(bytes([len(redeemscript)])+redeemscript).hex()
		index_items=[str(item) for item in index_list]
		counter=1
		for item in hardened_list[1:]:
			if str(item) == 'True':
				index_items.insert(counter, "'")
				index_items.insert(counter+1, "/")
				counter+=3
			else:
				index_items.insert(counter, "/")
				counter+=2
		derivation_path_text="m/"+ "".join(index_items[:-1])	
		script_to_sign_results=['p2sh', 'p2wpkh-p2sh', 'p2wsh']		
		if address_type in script_to_sign_results:
			result_text= 'XPRV='+str(xprv, 'utf-8')+'\n''XPUB='+str(xpub, 'utf-8')+'\n'+'DERIVATION PATH='+str(derivation_path_text)+ " -KEY INDEX="+str(key_index)+' HARDENED ADDRESS='+str(hardened_list[-1:])+'\n'+'privatekey='+str(path_private, 'utf-8')+'\n'+'Private hex='+privatehex+'\n'+'Private scalar='+str(string_to_int(index_key_data.CKDpriv()))+'\n'+'publickey='+public+'\n'+'public point='+str(codecs.encode(path_pubkey,'hex'), 'utf-8')+'\n'+'Script Pubkey='+script_pub+'\n'+'Scriptpub to sign='+signscript+'\n'#
		else:
			result_text= 'XPRV='+str(xprv, 'utf-8')+'\n''XPUB='+str(xpub, 'utf-8')+'\n'+'DERIVATION PATH='+str(derivation_path_text)+ " -KEY INDEX="+str(key_index)+' HARDENED ADDRESS='+str(hardened_list[-1:])+'\n'+'privatekey='+str(path_private, 'utf-8')+'\n'+'Private hex='+privatehex+'\n'+'Private scalar='+str(string_to_int(index_key_data.CKDpriv()))+'\n'+'publickey='+public+'\n'+'public point='+str(codecs.encode(path_pubkey,'hex'), 'utf-8')+'\n'+'Script Pubkey='+script_pub+'\n'#
		key_index+=1
		key_result.append(result_text)
	return key_result

def indv_priv_key(secret, testnet=True):
	if testnet==True:
		raw=b"\xEF"+secret+ b'\x01'
	else:
		raw=b"\x80"+secret+ b'\x01'
	raw = raw +hash256(raw)[:4]
	addr = encode_base58(raw)
	return addr

def indv_P2PKH_pub_key(pubkey,testnet=True):
	h160=hash160(pubkey)
	if testnet==True:
		raw = b'\x6F' + h160
	else:
		raw = b"\x00" + h160 
	raw = raw + hash256(raw)[:4]
	addr = encode_base58(raw)
	return str(addr,'utf-8')

def indv_P2WPKH_P2SH_pub_key(pubkey,testnet=True):
	h160 = hash160(pubkey)
	redeemscript=hash160(b"\x00\x14" +h160)
	if testnet==True:
		raw = b'\xC4' + redeemscript
	else:
		raw = b'\x05'+redeemscript
	raw = raw + hash256(raw)[:4]
	addr = encode_base58(raw)
	return str(addr,'utf-8')

def indv_P2SH_pub_key(pubkey,testnet=True):
	h160 = hash160(pubkey)
	if testnet==True:
		raw = b'\xC4' + h160
	else:
		raw = b'\x05'+h160
	raw = raw + hash256(raw)[:4]
	addr = encode_base58(raw)
	return str(addr,'utf-8')


def indv_P2WPKH_pub_key(pubkey,testnet=True):
	h160 = hash160(pubkey)
	if testnet==True:
		addr=encode_bech32('tb', 0, h160)
	else:
		addr=encode_bech32('bc', 0, h160)
	return addr

def indv_P2WSH_pub_key(pubkey, testnet=True):
	witnessprog=hashlib.sha256(pubkey).digest()
	if testnet==True:
		addr=encode_bech32('tb', 0, witnessprog)
	else:
		addr=encode_bech32('bc', 0, witnessprog)
	return addr

def p2wpkh_p2sh_redeemscript(pubkey):
    h160=hash160(pubkey)
    redeemscript_hash=hash160(OP_0+bytes([len(h160)])+h160)
    redeemscript_raw=(OP_0+bytes([len(h160)])+h160)
    redeemscript_full=bytes([len(redeemscript_raw)])+redeemscript_raw
    redeemscript_full2=bytes([len(redeemscript_full)])+redeemscript_full
    tx_redeemscript=redeemscript_full2.hex()
    return tx_redeemscript

def p2sh_redeemscript(pubkey):
    tx_redeemscript= b''.join([
        bytes([len(pubkey)]),
        pubkey,
        OP_CHECKSIG,
        ])
    return tx_redeemscript 


def encode_base58(s):
	count = 0
	for c in s:
		if c == 0:
			count += 1
		else:
			break
	prefix = b'1' * count
   
	num = int(s.hex(), 16)
	result = bytearray()
	while num > 0:
		num, mod = divmod(num, 58)
		result.insert(0, BASE58[mod])

	return prefix + bytes(result)

def bech32_polymod(values):
	generator = [0x3b6a57b2, 0x26508e6d, 0x1ea119fa, 0x3d4233dd, 0x2a1462b3]
	chk = 1
	for value in values:
		top = chk >> 25
		chk = (chk & 0x1ffffff) << 5 ^ value
		for i in range(5):
			chk ^= generator[i] if ((top >> i) & 1) else 0
	return chk

def bech32_hrp_expand(hrp):
	return [ord(x) >> 5 for x in hrp] + [0] + [ord(x) & 31 for x in hrp]

def bech32_create_checksum(hrp, data):
	values = bech32_hrp_expand(hrp) + data
	polymod = bech32_polymod(values + [0, 0, 0, 0, 0, 0]) ^ 1
	return [(polymod >> 5 * (5 - i)) & 31 for i in range(6)]

def bech32_encode(hrp, data):
	combined = data + bech32_create_checksum(hrp, data)
	return hrp + '1' + ''.join([CHARSET[d] for d in combined])

def convertbits(data, frombits, tobits, pad=True):
	acc = 0
	bits = 0
	ret = []
	maxv = (1 << tobits) - 1
	max_acc = (1 << (frombits + tobits - 1)) - 1
	for value in data:
		if value < 0 or (value >> frombits):
			return None
		acc = ((acc << frombits) | value) & max_acc
		bits += frombits
		while bits >= tobits:
			bits -= tobits
			ret.append((acc >> bits) & maxv)
	if pad:
		if bits:
			ret.append((acc << (tobits - bits)) & maxv)
	elif bits >= frombits or ((acc << (tobits - bits)) & maxv):
		return None
	return ret

def encode_bech32(hrp, witver, witprog):
	ret = bech32_encode(hrp, [witver] + convertbits(witprog, 8, 5))
	# if decode(hrp, ret) == (None, None):
	    # return None
	return ret

def p2pkh_script(address):
    h160=hash160(address)
    script_pub= b''.join([
        OP_DUP,
        OP_HASH160,
        bytes([len(h160)]),
        h160,
        OP_EQUALVERIFY,
        OP_CHECKSIG,
        ])
    script_pub_full=bytes([len(script_pub)])+script_pub
    return script_pub_full.hex()

def p2sh_script(address):
    h160=hash160(address)
    redeemscript=hash160(OP_0+bytes([len(h160)])+h160)
    script_pub= b''.join([
        OP_HASH160,
        bytes([len(redeemscript)]),
        redeemscript,
        OP_EQUAL,
        ])
    script_pub_full=bytes([len(script_pub)])+script_pub
    return script_pub_full.hex()

def p2wpkh_script(address):
    h160=hash160(address)
    script_pub= b''.join([
    	OP_0,
        bytes([len(h160)]),
        h160,
        ])
    script_pub_full=bytes([len(script_pub)])+script_pub
    return script_pub_full.hex()


def len_in_hex(item):
	length=len(item)
	if length > 4294967295:
		return b'\xFF' + (length).to_bytes(8, byteorder='little')
	elif length > 65535:
		return b'\xFE' + (length).to_bytes(4, byteorder='little')
	elif length > 252:
		return b'\xFD'+(length).to_bytes(2, byteorder='little')
	else:
		return length.to_bytes(1, byteorder='little')

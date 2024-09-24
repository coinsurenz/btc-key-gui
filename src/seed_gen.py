import hashlib
import hmac
import struct
import hashlib
import codecs
from ecdsa.ecdsa import int_to_string, string_to_int
from pbkdf2 import PBKDF2
from .ecdsa_functions import S256Point, G, CURVE_ORDER
from typing import List, Tuple
from .constants import AddressType
from .encoding import encode_base58, decode_xprv, decode_base58
from .crypto import hash160, hash256
from .address import convert_pubkey_to_pubdata, indv_priv_key, privkey_to_pubkey



def seed_to_master(
    seed: str,
    passphrase: str,
    derivation_path: List[int],
    hardened_items: List[bool],
    total_addresses: int,
    address_type: str,
    testnet: bool,
) -> List[str]:
    """
    Generate master keys and derive child keys based on the given seed and parameters.

    Args:
        seed (str): The seed phrase.
        passphrase (str): Additional passphrase for extra security.
        derivation_path (List[int]): The derivation path for child keys.
        hardened_items (List[bool]): List indicating which derivation steps are hardened.
        total_addresses (int): Number of addresses to generate.
        address_type (str): Type of address to generate (e.g., 'p2pkh', 'p2sh').
        testnet (bool): Whether to use testnet or mainnet.

    Returns:
        List[str]: List of derived key information.
    """
    seed_bytes = generate_seed(seed, passphrase)
    master_pk, master_cc = derive_master_keys(seed_bytes)
    master_pubkey = generate_master_pubkey(master_pk)

    return path_gen_keylist(
        master_cc,
        master_pk,
        master_pubkey,
        derivation_path,
        hardened_items,
        total_addresses,
        address_type,
        testnet,
    )


def generate_seed(seed: str, passphrase: str) -> bytes:
    """Generate a seed using PBKDF2."""
    return PBKDF2(
        seed,
        f"mnemonic{passphrase}",
        iterations=2048,
        macmodule=hmac,
        digestmodule=hashlib.sha512,
    ).read(64)


def derive_master_keys(seed_bytes: bytes) -> Tuple[bytes, bytes]:
    """Derive master private key and chain code."""
    hmac_hash = hmac.new(
        key=b"Bitcoin seed",
        msg=seed_bytes,
        digestmod=hashlib.sha512,
    ).digest()
    return hmac_hash[:32], hmac_hash[32:]


def generate_master_pubkey(master_pk: bytes) -> bytes:
    """Generate master public key."""
    return S256Point.sec(string_to_int(master_pk) * G)


class Keylevel:
    """
    Represents a key level in a hierarchical deterministic wallet.

    This class handles the derivation of child keys, generation of extended keys,
    and various operations related to Bitcoin key management.

    Attributes:
        HARDENED_THRESHOLD (int): The threshold for hardened key derivation.
    """

    HARDENED_THRESHOLD = 0x80000000

    def __init__(
        self,
        input_chaincode: bytes,
        input_priv_key: bytes,
        input_pub_key: bytes,
        index: int,
        hardened: bool,
        depth: int,
        input_fingerprint: bytes,
        address_type: AddressType,
        is_testnet: bool,
    ):
        """
        Initialize a Keylevel instance.

        Args:
            chaincode (bytes): The chain code for key derivation.
            priv_key (bytes): The private key.
            pub_key (bytes): The public key.
            index (int): The index of this key in the derivation path.
            hardened (bool): Whether this is a hardened derivation.
            depth (int): The depth of this key in the derivation path.
            fingerprint (bytes): The fingerprint of the parent key.
            address_type (AddressType): The type of address to generate.
            is_testnet (bool): Whether this is for the testnet.
        """
        self.input_chaincode = input_chaincode
        self.input_priv_key = input_priv_key
        self.input_pub_key = input_pub_key
        self.index = int(index)
        self.hardened = hardened
        self.depth = depth
        self.input_fingerprint = input_fingerprint
        self.address_type = AddressType(address_type).value
        self.testnet = is_testnet

    def _derive_child_key(self) -> Tuple[bytes, bytes]:
        """
        Derive a child key.

        Returns:
            Tuple[bytes, bytes]: A tuple containing the derived key and chain code.
        """
        if self.hardened:
            i = self.HARDENED_THRESHOLD + self.index
            data = b"\x00" + self.input_priv_key
        else:
            i = self.index
            data = self.input_pub_key
        i_bytes = struct.pack(">I", i & 0xFFFFFFFF)
        hmac_data = data + i_bytes
        child_key_hmac = hmac.new(
            key=self.input_chaincode, msg=hmac_data, digestmod=hashlib.sha512
        ).digest()

        return child_key_hmac[:32], child_key_hmac[32:]

    def CKDpriv(self) -> bytes:
        """
        Compute the Child Key Derivation for a private key.

        Returns:
            bytes: The derived child private key.
        """
        child_key, _ = self._derive_child_key()
        child_key_int = string_to_int(child_key)
        master_key_int = string_to_int(self.input_priv_key)
        new_key = (child_key_int + master_key_int) % CURVE_ORDER
        return int_to_string(new_key).rjust(32, b"\x00")

    def CKCpriv(self) -> bytes:
        """
        Compute the Child Key Chain code.

        Returns:
            bytes: The chain code for the child key.
        """
        _, chaincode = self._derive_child_key()
        return chaincode

    def pubkey(self) -> bytes:
        """
        Generate the public key from the private key.

        Returns:
            bytes: The public key.
        """
        pubpoint = int.from_bytes(self.CKDpriv(), byteorder="big") * G
        return bytes(S256Point.sec(pubpoint))

    def fingerprint(self) -> bytes:
        """
        Compute the fingerprint of the public key.

        Returns:
            bytes: The first 4 bytes of the hash160 of the public key.
        """
        return hash160(self.input_pub_key)[:4]

    def _get_version_bytes(self, is_private: bool) -> bytes:
        """
        Get the version bytes for extended keys based on address type and network.

        Args:
            is_private (bool): Whether this is for a private key.

        Returns:
            bytes: The version bytes.
        """
        version_bytes = {
            (AddressType.P2WPKH_P2SH.value, True, True): b"\x04\x4A\x4E\x28",
            (AddressType.P2WPKH_P2SH.value, True, False): b"\x04\x9D\x78\x78",
            (AddressType.P2WPKH_P2SH.value, False, True): b"\x04\x4A\x52\x62",
            (AddressType.P2WPKH_P2SH.value, False, False): b"\x04\x9D\x7C\xB2",
            (AddressType.P2WPKH.value, True, True): b"\x04\x5F\x18\xBC",
            (AddressType.P2WPKH.value, True, False): b"\x04\xB2\x43\x0C",
            (AddressType.P2WPKH.value, False, True): b"\x04\x5F\x1C\xF6",
            (AddressType.P2WPKH.value, False, False): b"\x04\xB2\x47\x46",
            (AddressType.P2WSH.value, True, True): b"\x02\x57\x50\x48",
            (AddressType.P2WSH.value, True, False): b"\x02\xAA\x7A\x99",
            (AddressType.P2WSH.value, False, True): b"\x02\x57\x54\x83",
            (AddressType.P2WSH.value, False, False): b"\x02\xAA\x7E\xD3",
            (AddressType.P2SH.value, True, True): b"\x04\x35\x83\x94",
            (AddressType.P2SH.value, True, False): b"\x04\x88\xAD\xE4",
            (AddressType.P2SH.value, False, True): b"\x04\x35\x83\x94",
            (AddressType.P2SH.value, False, False): b"\x04\x88\xB2\x1E",
            (AddressType.P2PKH.value, True, True): b"\x04\x35\x83\x94",
            (AddressType.P2PKH.value, True, False): b"\x04\x88\xAD\xE4",
            (AddressType.P2PKH.value, False, True): b"\x04\x35\x83\x94",
            (AddressType.P2PKH.value, False, False): b"\x04\x88\xB2\x1E",
        }

        return version_bytes.get(
            (self.address_type, is_private, self.testnet),
        )

    def _serialize_extended_key(self, is_private: bool) -> bytes:
        """
        Serialize an extended key.

        Args:
            is_private (bool): Whether this is for a private key.

        Returns:
            bytes: The serialized extended key.
        """
        version = self._get_version_bytes(is_private)
        i = self.HARDENED_THRESHOLD + self.index if self.hardened else self.index
        depth = bytes([self.depth])
        index = i.to_bytes(4, byteorder="big")
        chaincode = self.CKCpriv()
        fingerprint = self.fingerprint()
        key_data = b"\x00" + self.CKDpriv() if is_private else self.pubkey()
        return version + depth + fingerprint + index + chaincode + key_data

    def xprv(self) -> str:
        """
        Generate the extended private key.

        Returns:
            str: The base58-encoded extended private key.
        """
        prefix = self._get_version_bytes(True)
        if self.hardened:
            i = 2147483648 + self.index
        else:
            i = self.index
        xprvraw = (
            prefix
            + bytes([self.depth])
            + self.fingerprint()
            + bytes.fromhex(format(i, "x").rjust(8, "0"))
            + self.CKCpriv()
            + b"\x00"
            + self.CKDpriv()
        )
        checksum = hash256(xprvraw)[:4]
        xprvfull = xprvraw + checksum
        return encode_base58(xprvfull)

    def xpub(self) -> str:
        """
        Generate the extended public key.

        Returns:
            str: The base58-encoded extended public key.
        """
        prefix = self._get_version_bytes(False)
        if self.hardened:
            i = 2147483648 + self.index
        else:
            i = self.index
        xpubraw = (
            prefix
            + bytes([self.depth])
            + self.fingerprint()
            + bytes.fromhex(format(i, "x").rjust(8, "0"))
            + self.CKCpriv()
            + self.pubkey()
        )
        checksum = hash256(xpubraw)[:4]
        xpubfull = xpubraw + checksum
        return encode_base58(xpubfull)


def path_gen_keylist(
    master_cc,
    master_pk,
    master_pubkey,
    derivation_path,
    hardened_list,
    total_keys,
    address_type,
    is_testnet,
):
    """
    Generate a list of keys based on a derivation path.

    This function derives child keys from a master key according to the specified
    derivation path and generates a list of key information for each derived key.

    Args:
        master_cc (bytes): The master chain code.
        master_pk (bytes): The master private key.
        master_pubkey (bytes): The master public key.
        derivation_path (List[int]): The derivation path.
        hardened_list (List[bool]): List indicating which derivation steps are hardened.
        total_keys (int): The total number of keys to generate.
        address_type (str): The type of address to generate.
        is_testnet (bool): Whether this is for the testnet.

    Returns:
        List[str]: A list of strings, each containing information about a derived key.
    """
    depth = 1
    input_cc = master_cc
    input_pk = master_pk
    input_pub = master_pubkey
    input_fp = b"\x00\x00\x00\x00"
    xprv = b""
    xpub = b""
    account_extended_private_key = b""
    account_extended_public_key = b""

    hardened_list.insert(0, False)
    for index_str in derivation_path:
        is_hardened = hardened_list[depth]
        index_as_int = int(index_str)
        master_key_data = Keylevel(
            input_cc,
            input_pk,
            input_pub,
            index_as_int,
            is_hardened,
            depth,
            input_fp,
            address_type,
            is_testnet,
        )
        input_cc = master_key_data.CKCpriv()
        input_pk = master_key_data.CKDpriv()
        input_pub = master_key_data.pubkey()
        input_fp = master_key_data.fingerprint()
        account_extended_private_key = xprv
        account_extended_public_key = xpub
        xprv = master_key_data.xprv()
        xpub = master_key_data.xpub()
        depth += 1

        gen_fp = Keylevel(
            input_cc,
            input_pk,
            input_pub,
            index_as_int,
            is_hardened,
            depth,
            input_fp,
            address_type,
            is_testnet,
        )
        input_fp = gen_fp.fingerprint()

    key_index = 0
    key_result = []

    for key in range(total_keys):
        is_derived_key_hardened = hardened_list[depth - 1]
        index_key_data = Keylevel(
            input_cc,
            input_pk,
            input_pub,
            key,
            is_derived_key_hardened,
            depth,
            input_fp,
            address_type,
            is_testnet,
        )

        path_pubkey = index_key_data.pubkey()
        path_private = indv_priv_key(index_key_data.CKDpriv(), is_testnet)
        privatehex = index_key_data.CKDpriv().hex()

        public, script_pub, signscript = convert_pubkey_to_pubdata(
            path_pubkey, is_testnet, address_type
        )

        derivation_path_text = "m/" + "/".join(
            f"{item}{'h' if hardened else ''}"
            for item, hardened in zip(derivation_path, hardened_list[1:])
        )
        script_to_sign_results = ["p2sh", "p2wpkh-p2sh", "p2wsh", "p2wpkh"]
        common_text = (
            f"ACCOUNT EXTENDED PRV KEY={account_extended_private_key.decode('utf-8')}\n"
            f"ACCOUNT EXTENDED PUB KEY={account_extended_public_key.decode('utf-8')}\n"
            f"BIP32 XPRV={xprv.decode('utf-8')}\n"
            f"BIP32 XPUB={xpub.decode('utf-8')}\n"
            f"DERIVATION PATH={derivation_path_text} -KEY INDEX={key_index} HARDENED ADDRESS={hardened_list[-1:]}\n"
            f"privatekey={path_private.decode('utf-8')}\n"
            f"Private hex={privatehex}\n"
            f"Private scalar={string_to_int(index_key_data.CKDpriv())}\n"
            f"publickey={public}\n"
            f"public point={codecs.encode(path_pubkey, 'hex').decode('utf-8')}\n"
            f"Script Pubkey={script_pub}\n"
        )

        result_text = common_text + (
            f"Scriptpub to sign={signscript}\n"
            if address_type in script_to_sign_results
            else ""
        )
        key_index += 1
        key_result.append(result_text)
    return key_result

# TODO: write tests and adjust output when incorporated into gui
def generate_keys_from_xprv(xprv_string: str, total_keys: int, address_type: str, testnet: bool) -> List[Tuple[Keylevel, str]]:
    """
    Generate a list of keys from an xprv string.

    Args:
        xprv_string (str): The xprv string to use as a base.
        total_keys (int): The number of keys to generate.
        address_type (str): The type of address to generate.
        testnet (bool): Whether to use testnet or mainnet.

    Returns:
        List[Tuple[Keylevel, str]]: A list of tuples, each containing a Keylevel object and the corresponding private key.
    """
    chain_code, private_key = decode_xprv(xprv_string)

    xprv_bytes = decode_base58(xprv_string)
    depth = xprv_bytes[4]
    fingerprint = xprv_bytes[5:9]
    child_number = int.from_bytes(xprv_bytes[9:13], 'big')

    public_key = privkey_to_pubkey(private_key)

    base_key = Keylevel(
        chain_code,
        private_key,
        public_key,
        child_number,
        child_number >= 0x80000000,  # hardened 0x80000000needed here?
        depth,
        fingerprint,
        address_type,
        testnet
    )

    results = []
    for i in range(total_keys):

        testdepth = depth+1
        path_private = indv_priv_key(base_key.CKDpriv(), testnet)
        privatehex = base_key.CKDpriv().hex()
        index_key_data = Keylevel(chain_code, private_key, public_key, i, child_number >= 0x80000000, testdepth, base_key.fingerprint(), address_type, testnet)
        path_pubkey = index_key_data.pubkey()
        path_private = indv_priv_key(index_key_data.CKDpriv(), testnet)
        privatehex = index_key_data.CKDpriv().hex()
        public, script_pub, signscript = convert_pubkey_to_pubdata(path_pubkey, testnet, address_type)
        results.append((path_private, privatehex, public, script_pub, signscript))

    return results

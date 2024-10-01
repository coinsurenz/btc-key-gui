"""Address related functions"""

import hashlib
from .constants import NetworkType, AddressPrefix, OpCode
from .crypto import create_checksum, hash160
from .encoding import encode_base58, encode_bech32
from .ecdsa_functions import S256Point, G

def convert_pubkey_to_pubdata(pubkey, is_testnet, address_type):
    """
    Convert a public key to various address formats and their corresponding scripts.

    Args:
        pubkey (bytes): The public key to convert.
        is_testnet (bool): Whether to use testnet or mainnet.
        address_type (str): The type of address to generate ('p2pkh', 'p2sh', 'p2wpkh-p2sh', 'p2wpkh', or 'p2wsh').

    Returns:
        tuple: A tuple containing (address, script_pub, redeemscript).
        The contents vary based on the address_type.
    """
    address_functions = {
        "p2pkh": lambda: (
            indv_P2PKH_pub_key(pubkey, is_testnet),
            p2pkh_script(pubkey),
            None,
        ),
        "p2sh": lambda: (
            indv_P2SH_pub_key(redeemscript := p2sh_redeemscript(pubkey), is_testnet),
            p2sh_script(redeemscript),
            (bytes([len(redeemscript)]) + redeemscript).hex(),
        ),
        "p2wpkh-p2sh": lambda: (
            indv_P2WPKH_P2SH_pub_key(pubkey, is_testnet),
            p2sh_script(pubkey),
            "1976a9" + p2wpkh_p2sh_redeemscript(pubkey)[6:] + "88ac",
        ),
        "p2wpkh": lambda: (
            indv_P2WPKH_pub_key(pubkey, is_testnet),
            script_pub := p2wpkh_script(pubkey),
            "1976a9" + script_pub[4:] + "88ac",
        ),
        "p2wsh": lambda: (
            indv_P2WSH_pub_key(redeemscript := p2sh_redeemscript(pubkey), is_testnet),
            p2sh_script(pubkey),
            (bytes([len(redeemscript)]) + redeemscript).hex(),
        ),
    }
    return address_functions[address_type]()


def get_address_prefix(address_type: str, network: NetworkType) -> bytes:
    """
    Get the address prefix based on the address type and network.

    Args:
        address_type (str): The type of address ('p2pkh', 'p2sh', or 'wif').
        network (NetworkType): The network type (TESTNET or MAINNET).

    Returns:
        bytes: The address prefix as bytes.
    """
    prefix_map = {
        ("p2pkh", NetworkType.TESTNET.value): AddressPrefix.P2PKH_TESTNET.value,
        ("p2pkh", NetworkType.MAINNET.value): AddressPrefix.P2PKH_MAINNET.value,
        ("p2sh", NetworkType.TESTNET.value): AddressPrefix.P2SH_TESTNET.value,
        ("p2sh", NetworkType.MAINNET.value): AddressPrefix.P2SH_MAINNET.value,
        ("wif", NetworkType.TESTNET.value): AddressPrefix.WIF_TESTNET.value,
        ("wif", NetworkType.MAINNET.value): AddressPrefix.WIF_MAINNET.value,
    }
    return prefix_map.get(
        (address_type, network)
    )


def create_address(prefix: bytes, data: bytes) -> str:
    """
    Create a Bitcoin address from a prefix and data.

    Args:
        prefix (bytes): The address prefix.
        data (bytes): The address data.

    Returns:
        str: The encoded Bitcoin address.
    """
    raw = prefix + data
    checksum = create_checksum(raw)
    return encode_base58(raw + checksum)


def indv_priv_key(
    secret: bytes, network: NetworkType = NetworkType.TESTNET.value
) -> str:
    """
    Generate a Wallet Import Format (WIF) private key.

    Args:
        secret (bytes): The private key secret.
        network (NetworkType): The network type (testnet or mainnet).

    Returns:
        str: The WIF private key.
    """
    prefix = get_address_prefix("wif", network)
    return create_address(prefix, secret + b"\x01")


def indv_P2PKH_pub_key(
    pubkey: bytes, network: NetworkType = NetworkType.TESTNET.value
) -> str:
    """
    Generate a Pay-to-Public-Key-Hash (P2PKH) address.

    Args:
        pubkey (bytes): The public key.
        network (NetworkType): The network type (testnet or mainnet).

    Returns:
        str: The P2PKH address.
    """
    prefix = get_address_prefix("p2pkh", network)
    addr = create_address(prefix, hash160(pubkey))
    return str(addr, "utf-8")


def indv_P2WPKH_P2SH_pub_key(
    pubkey: bytes, network: NetworkType = NetworkType.TESTNET.value
) -> str:
    """
    Generate a Pay-to-Witness-Public-Key-Hash nested in Pay-to-Script-Hash (P2WPKH-P2SH) address.

    Args:
        pubkey (bytes): The public key.
        network (NetworkType): The network type (testnet or mainnet).

    Returns:
        str: The P2WPKH-P2SH address.
    """
    prefix = get_address_prefix("p2sh", network)
    redeemscript = hash160(b"\x00\x14" + hash160(pubkey))
    addr = create_address(prefix, redeemscript)
    return str(addr, "utf-8")


def indv_P2SH_pub_key(
    pubkey: bytes, network: NetworkType = NetworkType.TESTNET.value
) -> str:
    """
    Generate a Pay-to-Script-Hash (P2SH) address.

    Args:
        pubkey (bytes): The public key.
        network (NetworkType): The network type (testnet or mainnet).

    Returns:
        str: The P2SH address.
    """
    prefix = get_address_prefix("p2sh", network)
    addr = create_address(prefix, hash160(pubkey))
    return str(addr, "utf-8")


def indv_P2WPKH_pub_key(
    pubkey: bytes, network: NetworkType = NetworkType.TESTNET.value
) -> str:
    """
    Generate a Pay-to-Witness-Public-Key-Hash (P2WPKH) address.

    Args:
        pubkey (bytes): The public key.
        network (NetworkType): The network type (testnet or mainnet).

    Returns:
        str: The P2WPKH address.
    """
    h160 = hash160(pubkey)
    hrp = "tb" if network == NetworkType.TESTNET.value else "bc"
    return encode_bech32(hrp, 0, h160)


def indv_P2WSH_pub_key(
    pubkey: bytes, network: NetworkType = NetworkType.TESTNET.value
) -> str:
    """
    Generate a Pay-to-Witness-Script-Hash (P2WSH) address.

    Args:
        pubkey (bytes): The public key.
        network (NetworkType): The network type (testnet or mainnet).

    Returns:
        str: The P2WSH address.
    """
    witnessprog = hashlib.sha256(pubkey).digest()
    hrp = "tb" if network == NetworkType.TESTNET.value else "bc"
    return encode_bech32(hrp, 0, witnessprog)


def p2wpkh_p2sh_redeemscript(pubkey):
    """
    Generate a P2WPKH-P2SH (Pay-to-Witness-Public-Key-Hash nested in Pay-to-Script-Hash) redeem script.

    This function creates a redeem script for a P2WPKH-P2SH address, which allows backward
    compatibility of segregated witness transactions with older Bitcoin software.

    Args:
        pubkey (bytes): The public key for which to create the redeem script.

    Returns:
        str: The hexadecimal representation of the P2WPKH-P2SH redeem script.
    """
    h160 = hash160(pubkey)
    redeemscript_raw = OpCode.OP_0.value + bytes([len(h160)]) + h160
    redeemscript_full = bytes([len(redeemscript_raw)]) + redeemscript_raw
    redeemscript_plus_len = bytes([len(redeemscript_full)]) + redeemscript_full
    tx_redeemscript = redeemscript_plus_len.hex()

    return tx_redeemscript


def p2sh_redeemscript(pubkey):
    """
    Generate a Pay-to-Script-Hash (P2SH) redeem script.

    This function creates a redeem script for a P2SH address using the provided public key.
    The resulting script is a standard P2PK (Pay-to-Public-Key) script wrapped in a P2SH structure.

    Args:
        pubkey (bytes): The public key to be used in the redeem script.

    Returns:
        bytes: The P2SH redeem script as raw bytes.
    """
    tx_redeemscript = b"".join(
        [
            bytes([len(pubkey)]),
            pubkey,
            OpCode.OP_CHECKSIG.value,
        ]
    )
    return tx_redeemscript


def p2pkh_script(address: bytes) -> str:
    """
    Generate a Pay-to-Public-Key-Hash (P2PKH) script.

    Args:
        address (bytes): The public key hash.

    Returns:
        str: The hexadecimal representation of the P2PKH script.
    """
    h160 = hash160(address)
    script_pub = b"".join(
        [
            OpCode.OP_DUP.value,
            OpCode.OP_HASH160.value,
            bytes([len(h160)]),
            h160,
            OpCode.OP_EQUALVERIFY.value,
            OpCode.OP_CHECKSIG.value,
        ]
    )
    return (bytes([len(script_pub)]) + script_pub).hex()


def p2sh_script(address: bytes) -> str:
    """
    Generate a Pay-to-Script-Hash (P2SH) script.

    Args:
        address (bytes): The script hash.

    Returns:
        str: The hexadecimal representation of the P2SH script.
    """
    h160 = hash160(address)
    redeemscript = hash160(OpCode.OP_0.value + bytes([len(h160)]) + h160)
    script_pub = b"".join(
        [
            OpCode.OP_HASH160.value,
            bytes([len(redeemscript)]),
            redeemscript,
            OpCode.OP_EQUAL.value,
        ]
    )
    return (bytes([len(script_pub)]) + script_pub).hex()


def p2wpkh_script(address: bytes) -> str:
    """
    Generate a Pay-to-Witness-Public-Key-Hash (P2WPKH) script.

    Args:
        address (bytes): The public key hash.

    Returns:
        str: The hexadecimal representation of the P2WPKH script.
    """
    h160 = hash160(address)
    script_pub = b"".join(
        [
            OpCode.OP_0.value,
            bytes([len(h160)]),
            h160,
        ]
    )
    return (bytes([len(script_pub)]) + script_pub).hex()

def privkey_to_pubkey(privkey: bytes) -> bytes:
    """Convert a private key to a public key."""
    pubpoint = int.from_bytes(privkey, byteorder="big") * G
    return bytes(S256Point.sec(pubpoint))

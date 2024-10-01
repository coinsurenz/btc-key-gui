"""Constants for address encoding."""
from enum import Enum


BASE58 = b"123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
CHARSET = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"

class OpCode(Enum):
    OP_DUP = b"\x76"
    OP_EQUALVERIFY = b"\x88"
    OP_HASH160 = b"\xa9"
    OP_CHECKSIG = b"\xac"
    OP_EQUAL = b"\x87"
    OP_0 = b"\x00"

class NetworkType(Enum):
    TESTNET = True
    MAINNET = False

class AddressPrefix(Enum):
    P2PKH_TESTNET = b"\x6F"
    P2PKH_MAINNET = b"\x00"
    P2SH_TESTNET = b"\xC4"
    P2SH_MAINNET = b"\x05"
    WIF_TESTNET = b"\xEF"
    WIF_MAINNET = b"\x80"

class AddressType(Enum):
    P2PKH = "p2pkh"
    P2SH = "p2sh"
    P2WPKH_P2SH = "p2wpkh-p2sh"
    P2WPKH = "p2wpkh"
    P2WSH = "p2wsh"

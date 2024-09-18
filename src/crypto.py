"""Cryptographic utils."""

import hashlib


def hash256(secret):
    """
    Perform a double SHA256 hash on the input data.

    Args:
        data (bytes): The input data to be hashed.

    Returns:
        bytes: The resulting double SHA256 hash.
    """
    return hashlib.sha256(hashlib.sha256(secret).digest()).digest()


def hash160(secret):
    """
    Perform a SHA256 hash followed by a RIPEMD160 hash on the input data.

    Args:
        data (bytes): The input data to be hashed.

    Returns:
        bytes: The resulting RIPEMD160(SHA256(data)) hash.
    """
    return hashlib.new("ripemd160", hashlib.sha256(secret).digest()).digest()


def create_checksum(data: bytes) -> bytes:
    return hash256(data)[:4]

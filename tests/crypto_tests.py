"""Tests for crypto functions"""

import pytest
import binascii
from src.crypto import hash256, hash160, create_checksum


# Test vectors from https://en.bitcoin.it/wiki/Protocol_documentation#Hashes
def test_hash256():
    data = "hello".encode("utf-8")
    expected = "9595c9df90075148eb06860365df33584b75bff782a510c6cd4883a419833d50"
    assert hash256(data) == binascii.unhexlify(expected.encode("utf8"))


def test_hash160():
    data = "hello".encode("utf-8")
    expected = "b6a9c8c230722b7c748331a8b450f05566dc7d0f"
    assert hash160(data) == binascii.unhexlify(expected.encode("utf8"))


def test_create_checksum():
    data = "hello".encode("utf-8")
    expected = "9595c9df"
    assert create_checksum(data) == binascii.unhexlify(expected.encode("utf8"))

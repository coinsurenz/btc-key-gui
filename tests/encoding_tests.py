"""Tests for encoding functions"""

import pytest
from src.encoding import (
    encode_base58,
    bech32_polymod,
    bech32_hrp_expand,
    bech32_create_checksum,
    bech32_encode,
    convertbits,
    decode_xprv,
    decode_base58
)
from src.constants import BASE58, CHARSET
from .test_constants import TEST_PUBKEY_HASH, TEST_CHECKSUM, TEST_PREFIX


def test_encode_base58():
    test_bytes = b"\x00" + TEST_PUBKEY_HASH + TEST_CHECKSUM
    encoded = encode_base58(test_bytes)
    assert encoded == (b"18g5SfgpLxtFSRikqrk4wYu1WAP7A81gSS")
    assert len(encoded) == 34


def test_bech32_polymod():
    assert (
        bech32_polymod(
            [
                3,
                3,
                0,
                2,
                3,
                0,
                5,
                0,
                23,
                20,
                16,
                0,
                15,
                15,
                0,
                14,
                6,
                5,
                3,
                29,
                2,
                9,
                17,
                13,
                28,
                12,
                16,
                29,
                13,
                18,
                9,
                28,
                24,
                6,
                14,
                22,
                19,
                26,
                0,
                0,
                0,
                0,
                0,
                0,
            ]
        )
        == 168568672
    )


def test_bech32_hrp_expand():
    assert bech32_hrp_expand("bc") == [3, 3, 0, 2, 3]


def test_bech32_create_checksum():
    hrp = "bc"
    data = [
        0,
        5,
        0,
        23,
        20,
        16,
        0,
        15,
        15,
        0,
        14,
        6,
        5,
        3,
        29,
        2,
        9,
        17,
        13,
        28,
        12,
        16,
        29,
        13,
        18,
        9,
        28,
        24,
        6,
        14,
        22,
        19,
        26,
    ]
    checksum = bech32_create_checksum(hrp, data)
    assert checksum == [5, 0, 24, 9, 27, 1]


def test_bech32_encode():
    hrp = "bc"
    data = [
        0,
        5,
        0,
        23,
        20,
        16,
        0,
        15,
        15,
        0,
        14,
        6,
        5,
        3,
        29,
        2,
        9,
        17,
        13,
        28,
        12,
        16,
        29,
        13,
        18,
        9,
        28,
        24,
        6,
        14,
        22,
        19,
        26,
    ]
    encoded = bech32_encode(hrp, data)
    assert encoded == "bc1q9qh5sq00qwx9razf3duvsadjfucxwkn69qcfmp"


def test_convertbits():
    assert convertbits(b"(/H\x01\xef\x03\x8cQ\xf4I\x8bx\xc8u\xb2O0gZz", 8, 5, True) == [
        5,
        0,
        23,
        20,
        16,
        0,
        15,
        15,
        0,
        14,
        6,
        5,
        3,
        29,
        2,
        9,
        17,
        13,
        28,
        12,
        16,
        29,
        13,
        18,
        9,
        28,
        24,
        6,
        14,
        22,
        19,
        26,
    ]


def test_convertbits_invalid_input():
    assert convertbits([-1], 8, 5) is None
    assert convertbits([256], 8, 5) is None


def test_bech32_encode_charset():
    hrp = "test"
    data = list(range(32))
    encoded = bech32_encode(hrp, data)
    assert all(c in CHARSET for c in encoded[5:])


def test_encode_base58_charset():
    test_bytes = bytes(range(58))
    encoded = encode_base58(test_bytes)
    assert all(c in BASE58 for c in encoded)

def test_decode_xprv():
    xprv = "xprv9s21ZrQH143K3QTDL4LXw2F7HEK3wJUD2nW2nRk4stbPy6cq3jPPqjiChkVvvNKmPGJxWUtg6LnF5kejMRNNU3TGtRBeJgk33yuGBxrMPHi"
    expected_chain_code = bytes.fromhex("873dff81c02f525623fd1fe5167eac3a55a049de3d314bb42ee227ffed37d508")
    expected_private_key = bytes.fromhex("e8f32e723decf4051aefac8e2c93c9c5b214313817cdb01a1494b917c8436b35")

    chain_code, private_key = decode_xprv(xprv)

    assert chain_code == expected_chain_code
    assert private_key == expected_private_key

def test_decode_xprv_invalid_length():
    with pytest.raises(ValueError):
        decode_xprv("xprv9s21ZrQH143K")

def test_decode_xprv_invalid_checksum():
    invalid_xprv = "xprv9s21ZrQH143K3QTDL4LXw2F7HEK3wJUD2nW2nRk4stbPy6cq3jPPqjiChkVvvNKmPGJxWUtg6LnF5kejMRNNU3TGtRBeJgk33yuGBxrMPHj"
    with pytest.raises(ValueError):
        decode_xprv(invalid_xprv)

def test_decode_base58():
    encoded = "18g5SfgpLxtFSRikqrk4wYu1WAP7A81gSS"
    expected = TEST_PREFIX + TEST_PUBKEY_HASH + TEST_CHECKSUM
    result = decode_base58(encoded)

    assert result == expected

def test_decode_base58_invalid_character():
    with pytest.raises(ValueError):
        decode_base58("invalid!")

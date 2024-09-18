import pytest
from src.encoding import (
    encode_base58,
    bech32_polymod,
    bech32_hrp_expand,
    bech32_create_checksum,
    bech32_encode,
    convertbits,
)
from src.constants import BASE58, CHARSET
from .test_constants import TEST_PUBKEY_HASH, TEST_CHECKSUM


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

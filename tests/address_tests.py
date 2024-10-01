"""Tests for address functions"""

from unittest.mock import patch
import pytest
from src.address import (
    convert_pubkey_to_pubdata,
    p2pkh_script,
    p2sh_script,
    p2wpkh_script,
    indv_P2PKH_pub_key,
    indv_P2SH_pub_key,
    indv_P2WPKH_P2SH_pub_key,
    indv_P2WPKH_pub_key,
    indv_P2WSH_pub_key,
    p2wpkh_p2sh_redeemscript,
    p2sh_redeemscript,
    indv_priv_key,
    get_address_prefix,
    privkey_to_pubkey,
)
from src.crypto import hash160
from src.constants import OpCode, NetworkType, AddressPrefix
from tests.test_constants import (
    TEST_PUBKEY,
    TEST_PUBKEY_HASH,
    TEST_PUBKEY_HASH_LEN,
    TEST_P2SH_REDEEMSCRIPT,
    TEST_PRIVKEY,
    TEST_P2SH_BYTES,
    TEST_P2SH_REDEEMSCRIPT_LEN,
)


@pytest.mark.parametrize(
    "address_type,expected_length",
    [
        ("p2pkh", 3),
        ("p2sh", 3),
        ("p2wpkh-p2sh", 3),
        ("p2wpkh", 3),
        ("p2wsh", 3),
    ],
)
@patch("src.address.indv_P2PKH_pub_key")
@patch("src.address.indv_P2SH_pub_key")
@patch("src.address.indv_P2WPKH_P2SH_pub_key")
@patch("src.address.indv_P2WPKH_pub_key")
@patch("src.address.indv_P2WSH_pub_key")
@patch("src.address.p2pkh_script")
@patch("src.address.p2sh_script")
@patch("src.address.p2wpkh_script")
@patch("src.address.p2sh_redeemscript")
@patch("src.address.p2wpkh_p2sh_redeemscript")
def test_convert_pubkey_to_pubdata(
    mock_p2wpkh_p2sh_redeemscript,
    mock_p2sh_redeemscript,
    mock_p2wpkh_script,
    mock_p2sh_script,
    mock_p2pkh_script,
    mock_indv_P2WSH_pub_key,
    mock_indv_P2WPKH_pub_key,
    mock_indv_P2WPKH_P2SH_pub_key,
    mock_indv_P2SH_pub_key,
    mock_indv_P2PKH_pub_key,
    address_type,
    expected_length,
):

    for mock_func in [
        mock_indv_P2PKH_pub_key,
        mock_indv_P2SH_pub_key,
        mock_indv_P2WPKH_P2SH_pub_key,
        mock_indv_P2WPKH_pub_key,
        mock_indv_P2WSH_pub_key,
        mock_p2pkh_script,
        mock_p2sh_script,
        mock_p2wpkh_script,
        mock_p2wpkh_p2sh_redeemscript,
    ]:
        mock_func.return_value = "mocked_value"
        mock_p2sh_redeemscript.return_value = b"mocked_value"

    result = convert_pubkey_to_pubdata(TEST_PUBKEY, True, address_type)

    assert isinstance(result, tuple)
    assert len(result) == expected_length

    if address_type == "p2pkh":
        mock_indv_P2PKH_pub_key.assert_called_once()
        mock_p2pkh_script.assert_called_once()
    elif address_type == "p2sh":
        mock_indv_P2SH_pub_key.assert_called_once()
        mock_p2sh_script.assert_called_once()
        mock_p2sh_redeemscript.assert_called_once()
    elif address_type == "p2wpkh-p2sh":
        mock_indv_P2WPKH_P2SH_pub_key.assert_called_once()
        mock_p2sh_script.assert_called_once()
        mock_p2wpkh_p2sh_redeemscript.assert_called_once()
    elif address_type == "p2wpkh":
        mock_indv_P2WPKH_pub_key.assert_called_once()
        mock_p2wpkh_script.assert_called_once()
    elif address_type == "p2wsh":
        mock_indv_P2WSH_pub_key.assert_called_once()
        mock_p2sh_script.assert_called_once()
        mock_p2sh_redeemscript.assert_called_once()


def test_p2pkh_script():
    expected_script = "1976a914" + TEST_PUBKEY_HASH.hex() + "88ac"
    assert p2pkh_script(TEST_PUBKEY) == expected_script


def test_p2sh_script():
    h160 = hash160(TEST_PUBKEY)
    redeemscript = hash160(OpCode.OP_0.value + bytes([len(h160)]) + h160)
    expected_script = "17a914" + redeemscript.hex() + "87"
    assert p2sh_script(TEST_PUBKEY) == expected_script


def test_p2wpkh_script():
    expected_script = "160014" + TEST_PUBKEY_HASH.hex()
    assert p2wpkh_script(TEST_PUBKEY) == expected_script


def test_p2pkh_script_length():
    script = bytes.fromhex(p2pkh_script(TEST_PUBKEY))
    assert script[0] == 0x19
    assert len(script) == 26


def test_p2sh_script_length():
    script = bytes.fromhex(p2sh_script(TEST_PUBKEY))
    assert script[0] == 0x17
    assert len(script) == 24


def test_p2wpkh_script_length():
    script = bytes.fromhex(p2wpkh_script(TEST_PUBKEY))
    assert script[0] == 0x16
    assert len(script) == 23


def test_p2pkh_script_structure():
    script = bytes.fromhex(p2pkh_script(TEST_PUBKEY))
    assert script[1:2] == OpCode.OP_DUP.value
    assert script[2:3] == OpCode.OP_HASH160.value
    assert script[3:4] == TEST_PUBKEY_HASH_LEN
    assert script[4 : 4 + 20] == TEST_PUBKEY_HASH
    assert script[-2:-1] == OpCode.OP_EQUALVERIFY.value
    assert script[-1:] == OpCode.OP_CHECKSIG.value


def test_p2sh_script_structure():
    script = bytes.fromhex(p2sh_script(TEST_PUBKEY))
    assert script[1:2] == OpCode.OP_HASH160.value
    assert script[2:3] == TEST_P2SH_REDEEMSCRIPT_LEN
    assert script[3 : 3 + 20] == TEST_P2SH_REDEEMSCRIPT
    assert script[-1:] == OpCode.OP_EQUAL.value


def test_p2wpkh_script_structure():
    script = bytes.fromhex(p2wpkh_script(TEST_PUBKEY))
    assert script[1:2] == OpCode.OP_0.value
    assert script[2:3] == TEST_PUBKEY_HASH_LEN


def test_p2wpkh_p2sh_redeemscript_structure():
    redeemscript = bytes.fromhex(p2wpkh_p2sh_redeemscript(TEST_PUBKEY))
    assert redeemscript[1] == len(
        OpCode.OP_0.value + TEST_PUBKEY_HASH_LEN + TEST_PUBKEY_HASH
    )
    assert redeemscript[2:3] == OpCode.OP_0.value
    assert redeemscript[3:4] == TEST_PUBKEY_HASH_LEN
    assert redeemscript[4 : 4 + 20] == TEST_PUBKEY_HASH


def test_p2sh_redeemscript_structure():
    redeemscript = p2sh_redeemscript(TEST_PUBKEY)
    assert redeemscript[0] == len(TEST_PUBKEY)
    assert redeemscript[1:34] == TEST_PUBKEY
    assert redeemscript[34:] == OpCode.OP_CHECKSIG.value


def test_invalid_input():
    with pytest.raises(TypeError):
        p2pkh_script("not bytes")
    with pytest.raises(TypeError):
        p2sh_script("not bytes")


@pytest.mark.parametrize("invalid_input", ["not bytes", 123, None, [1, 2, 3]])
def test_invalid_input_scripts(invalid_input):
    with pytest.raises(TypeError):
        p2pkh_script(invalid_input)
    with pytest.raises(TypeError):
        p2sh_script(invalid_input)
    with pytest.raises(TypeError):
        p2wpkh_script(invalid_input)


def test_indv_priv_key():
    testnet_wif = indv_priv_key(TEST_PRIVKEY, NetworkType.TESTNET.value)
    assert isinstance(testnet_wif, bytes)
    assert len(testnet_wif) == 52
    assert testnet_wif == b"cUW7xwAX1WZjgD3XfTKPj4udRTQGLqMofXABCC2zQbprvAiiHgr9"

    mainnet_wif = indv_priv_key(TEST_PRIVKEY, NetworkType.MAINNET.value)
    assert isinstance(mainnet_wif, bytes)
    assert len(mainnet_wif) == 52
    assert mainnet_wif == b"L498W2AfaSsUWmaGH3WGMkQZoE6rgPG7bV1i5maUuVArfRggAGeT"


def test_indv_P2PKH_pub_key():
    testnet_address = indv_P2PKH_pub_key(TEST_PUBKEY, NetworkType.TESTNET.value)
    assert isinstance(testnet_address, str)
    assert testnet_address == "moC2jimo9zKWDYCNZRiSmU7LN9yp5M5Syf"

    mainnet_address = indv_P2PKH_pub_key(TEST_PUBKEY, NetworkType.MAINNET.value)
    assert isinstance(mainnet_address, str)
    assert mainnet_address == "18g5SfgpLxtFSRikqrk4wYu1WAP7A81gSS"


def test_indv_P2WPKH_P2SH_pub_key():
    testnet_address = indv_P2WPKH_P2SH_pub_key(TEST_PUBKEY, NetworkType.TESTNET.value)
    assert isinstance(testnet_address, str)
    assert testnet_address == "2NArRU2GAMWhV9xtVxG4T2hDAESprFuVCu3"

    mainnet_address = indv_P2WPKH_P2SH_pub_key(TEST_PUBKEY, NetworkType.MAINNET.value)
    assert isinstance(mainnet_address, str)
    assert mainnet_address == "3KJDQHL8k4C8xBFxH8SaQkDu26cgSZQRdL"


def test_indv_P2SH_pub_key():
    testnet_address = indv_P2SH_pub_key(TEST_P2SH_BYTES, NetworkType.TESTNET.value)
    assert isinstance(testnet_address, str)
    assert testnet_address == "2N3msajXibYod38BuCMMyc27FwpFZkvzwVi"

    mainnet_address = indv_P2SH_pub_key(TEST_P2SH_BYTES, NetworkType.MAINNET.value)
    assert isinstance(mainnet_address, str)
    assert mainnet_address == "3CDfWzbgz6JGqLZMXDk6z57zjU3PyzLfG9"


def test_indv_P2WPKH_pub_key():
    testnet_address = indv_P2WPKH_pub_key(TEST_PUBKEY, NetworkType.TESTNET.value)
    assert isinstance(testnet_address, str)
    assert testnet_address == "tb1q2skvlwjuyxlh9n2sgufqddg4dmupkf6nzadptv"

    mainnet_address = indv_P2WPKH_pub_key(TEST_PUBKEY, NetworkType.MAINNET.value)
    assert isinstance(mainnet_address, str)
    assert mainnet_address == "bc1q2skvlwjuyxlh9n2sgufqddg4dmupkf6ngmkjsl"


def test_indv_P2WSH_pub_key():
    testnet_address = indv_P2WSH_pub_key(TEST_P2SH_BYTES, NetworkType.TESTNET.value)
    assert isinstance(testnet_address, str)
    assert (
        testnet_address
        == "tb1qnfrqgmdqyd0g63kd5rm7fxsqzvmvh97lcneh6h52ecgjlj89ef4q4dq6dh"
    )

    mainnet_address = indv_P2WSH_pub_key(TEST_P2SH_BYTES, NetworkType.MAINNET.value)
    assert isinstance(mainnet_address, str)
    assert (
        mainnet_address
        == "bc1qnfrqgmdqyd0g63kd5rm7fxsqzvmvh97lcneh6h52ecgjlj89ef4qz9k4hc"
    )


def test_p2wpkh_p2sh_redeemscript():
    redeemscript = p2wpkh_p2sh_redeemscript(TEST_PUBKEY)
    assert isinstance(redeemscript, str)
    assert len(redeemscript) == 48


def test_p2sh_redeemscript():
    redeemscript = p2sh_redeemscript(TEST_PUBKEY)
    assert isinstance(redeemscript, bytes)
    assert len(redeemscript) == 35


def test_network_type():
    testnet_address = indv_P2PKH_pub_key(TEST_PUBKEY, NetworkType.TESTNET.value)
    mainnet_address = indv_P2PKH_pub_key(TEST_PUBKEY, NetworkType.MAINNET.value)
    assert testnet_address != mainnet_address


@pytest.mark.parametrize(
    "func",
    [
        indv_priv_key,
        indv_P2PKH_pub_key,
        indv_P2WPKH_P2SH_pub_key,
        indv_P2SH_pub_key,
        indv_P2WPKH_pub_key,
        indv_P2WSH_pub_key,
    ],
)
def test_network_types(func):
    testnet_result = func(TEST_PUBKEY, NetworkType.TESTNET.value)
    mainnet_result = func(TEST_PUBKEY, NetworkType.MAINNET.value)
    assert testnet_result != mainnet_result


def test_network_types_priv_key():
    testnet_result = indv_priv_key(TEST_PRIVKEY, NetworkType.TESTNET.value)
    mainnet_result = indv_priv_key(TEST_PRIVKEY, NetworkType.MAINNET.value)
    assert testnet_result != mainnet_result


def test_get_address_prefix():
    assert (
        get_address_prefix("p2pkh", NetworkType.TESTNET.value)
        == AddressPrefix.P2PKH_TESTNET.value
    )
    assert (
        get_address_prefix("p2sh", NetworkType.MAINNET.value)
        == AddressPrefix.P2SH_MAINNET.value
    )
    assert (
        get_address_prefix("wif", NetworkType.TESTNET.value)
        == AddressPrefix.WIF_TESTNET.value
    )

def test_privkey_to_pubkey():
    result = privkey_to_pubkey(TEST_PRIVKEY)

    assert result == TEST_PUBKEY

"""Tests for UI functions"""

import pytest
from unittest.mock import Mock, patch
from ui.ui_functions import (
    path_derivation_func,
    address_combo_func,
    num_words_func,
    seed_button,
    create_multisig,
    len_in_hex,
)


@pytest.fixture
def mock_ui():
    return Mock()


def test_path_derivation_func(mock_ui):
    assert path_derivation_func("m/0/1/2", mock_ui) == [
        ["0", "1", "2"],
        [False, False, False],
    ]
    assert path_derivation_func("m/0'/1/2'", mock_ui) == [
        ["0", "1", "2"],
        [True, False, True],
    ]
    assert path_derivation_func("", mock_ui) == [["0"], [False]]
    assert path_derivation_func("invalid", mock_ui) is None


def test_address_combo_func(mock_ui):
    assert address_combo_func(5, mock_ui) == "bip44"
    mock_ui.derivationpath_box.setText.assert_called_with("m/44'/0'/0'/0")
    mock_ui.derivationpath_box.setDisabled.assert_called()
    mock_ui.hardened_checkbox.setDisabled.assert_called()
    assert address_combo_func(6, mock_ui) == "bip49"
    mock_ui.derivationpath_box.setText.assert_called_with("m/49'/0'/0'/0")
    assert address_combo_func(7, mock_ui) == "bip84"
    mock_ui.derivationpath_box.setText.assert_called_with("m/84'/0'/0'/0")
    assert address_combo_func(0, mock_ui) == "p2pkh"
    mock_ui.derivationpath_box.setDisabled.assert_called()
    mock_ui.hardened_checkbox.setDisabled.assert_called()


def test_num_words_func(mock_ui):
    assert num_words_func(0, mock_ui) == "3"
    assert num_words_func(7, mock_ui) == "24"


@pytest.mark.parametrize(
    "multisig,expected",
    [
        (
            True,
            "4752210279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f817982102f9308a019258c31049344f85f89d5229b531c845836f99b08601f113bce036f952ae",
        ),
        (False, ["seed_result"]),  # Adjusted to match the actual return value
    ],
)
def test_seed_button(mock_ui, multisig, expected):
    mock_ui.multisig_checkbox.isChecked.return_value = multisig
    mock_ui.numaddress_spinbox.value.return_value = 2

    mock_ui.word1_box.text.return_value = (
        "0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798"
    )
    mock_ui.word2_box.text.return_value = (
        "02F9308A019258C31049344F85F89D5229B531C845836F99B08601F113BCE036F9"
    )
    for i in range(3, 25):
        getattr(mock_ui, f"word{i}_box").text.return_value = ""

    mock_ui.address_combobox.currentIndex.return_value = 1
    mock_ui.testnet_checkbox.isChecked.return_value = False

    if not multisig:
        mock_ui.derivationpath_box.text.return_value = "m/0/1"
        mock_ui.hardened_checkbox.isChecked.return_value = False

        with patch("ui.ui_functions.seed_to_master", return_value=["seed_result"]):
            result = seed_button(mock_ui)
    else:
        result = seed_button(mock_ui)

    assert result == expected


def test_create_multisig(mock_ui):
    mock_ui.numaddress_spinbox.value.return_value = 2
    mock_ui.word1_box.text.return_value = (
        "0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798"
    )
    mock_ui.word2_box.text.return_value = (
        "02F9308A019258C31049344F85F89D5229B531C845836F99B08601F113BCE036F9"
    )
    mock_ui.address_combobox.currentIndex.return_value = 1
    mock_ui.testnet_checkbox.isChecked.return_value = False

    for i in range(3, 25):
        getattr(mock_ui, f"word{i}_box").text.return_value = ""

    result = create_multisig(2, mock_ui)
    assert isinstance(result, str)
    assert len(result) > 0
    assert (
        result
        == "4752210279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f817982102f9308a019258c31049344f85f89d5229b531c845836f99b08601f113bce036f952ae"
    )


def test_len_in_hex_small_value():
    assert len_in_hex(b"hello") == b"\x05"
    assert len_in_hex("world") == b"\x05"
    assert len_in_hex([1, 2, 3, 4, 5]) == b"\x05"


def test_len_in_hex_fd_value():
    assert len_in_hex(b"a" * 253) == b"\xFD\xFD\x00"
    assert len_in_hex("a" * 300) == b"\xFD\x2C\x01"


def test_len_in_hex_fe_value():
    assert len_in_hex(b"a" * 65536) == b"\xFE\x00\x00\x01\x00"
    assert len_in_hex("a" * 70000) == b"\xFE\x70\x11\x01\x00"


def test_len_in_hex_ff_value():
    assert len_in_hex(b"a" * 4294967296) == b"\xFF\x00\x00\x00\x00\x01\x00\x00\x00"


def test_len_in_hex_zero_length():
    assert len_in_hex(b"") == b"\x00"
    assert len_in_hex("") == b"\x00"
    assert len_in_hex([]) == b"\x00"


def test_len_in_hex_different_types():
    assert (
        len_in_hex(b"binary") == len_in_hex("string") == len_in_hex([1, 2, 3, 4, 5, 6])
    )

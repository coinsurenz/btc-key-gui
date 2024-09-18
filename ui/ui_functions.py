"""UI functions"""

import datetime
from typing import List, Union
from src.seed_gen import seed_to_master
from src.address import indv_P2SH_pub_key, indv_P2WSH_pub_key


def path_derivation_func(path_string: str, ui):
    hardened_item = []
    if path_string == "":
        path_string = "m/0"
        ui.derivationpath_box.setText("m/")
    valid_char = ["m", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "'"]
    for char in path_string:
        if char not in valid_char:
            ui.output_textbrowser.setText(
                "Invalid derivation path- example of correct format is m/1/2'/3"
            )
            return None
    path_output_raw = path_string.replace("m", "")
    path_output_items = path_output_raw.strip("/").split("/")

    for item in path_output_items:
        hardened_item.append("'" in item)
    derivation_path = [item.strip("'") for item in path_output_items]

    if derivation_path == [""]:
        derivation_path = [0]
    return [derivation_path, hardened_item]


def address_combo_func(data: int, ui):
    address_data = [
        "p2pkh",
        "p2sh",
        "p2wpkh-p2sh",
        "p2wpkh",
        "p2wsh",
        "bip44",
        "bip49",
        "bip84",
        "bip141",
    ]
    selection = address_data[data]
    if selection in ["bip44", "bip49", "bip84"]:
        ui.derivationpath_box.setDisabled(True)
        ui.derivationpath_box.setText(f"m/{selection[3:]}'/0'/0'/0")
        ui.hardened_checkbox.setDisabled(True)
        ui.hardened_checkbox.setChecked(False)
    elif selection == "bip141":
        ui.hardened_checkbox.setDisabled(True)
        ui.hardened_checkbox.setChecked(False)
    else:
        ui.derivationpath_box.setDisabled(False)
        ui.hardened_checkbox.setDisabled(False)
    return selection


def num_words_func(data: int, ui):
    address_data = ["3", "6", "9", "12", "15", "18", "21", "24"]
    selection = address_data[data]
    words = [getattr(ui, f"word{i}_box") for i in range(1, 25)]

    for i, wordbox in enumerate(words):
        wordbox.setDisabled(i >= int(selection))
    return selection


def seed_button(ui):
    if ui.multisig_checkbox.isChecked():
        return create_multisig(ui.numaddress_spinbox.value(), ui)

    words = [getattr(ui, f"word{i}_box").text() for i in range(1, 25)]
    words_list = [item for item in words if item != ""]
    seed = " ".join(words_list)
    passphrase = ui.bip39pass_box.text()
    derivation_path_data = path_derivation_func(ui.derivationpath_box.text(), ui)
    if not derivation_path_data:
        return
    derivation_path, hardened_items = derivation_path_data

    total_addresses = ui.numaddress_spinbox.value()
    address_type = address_combo_func(ui.address_combobox.currentIndex(), ui)
    testnet = ui.testnet_checkbox.isChecked()
    hardened_items.append(ui.hardened_checkbox.isChecked())

    if address_type in ["bip44", "bip49", "bip84"]:
        derivation_path = [int(address_type[3:]), 0, 0, 0]
        address_type = (
            "p2pkh"
            if address_type == "bip44"
            else "p2wpkh-p2sh" if address_type == "bip49" else "p2wpkh"
        )
        hardened_items = [True, True, True, False]
    elif address_type == "bip141":
        address_type = "p2wpkh-p2sh"
        hardened_items[-1] = False

    result = seed_to_master(
        seed,
        passphrase,
        derivation_path,
        hardened_items,
        total_addresses,
        address_type,
        testnet,
    )
    result_data = f"{result[0][:234]}\n"
    for key_data in result:
        result_data += f"{key_data[234:]}\n\n"
    ui.output_textbrowser.setText(result_data)

    if ui.textfile_CheckBox.isChecked():
        with open("data.txt", "a") as wallet:
            wallet.write(
                f"\n**NEW WALLET KEYS ADDED**- {datetime.datetime.now()}\n SEED={seed} PASSPHRASE={passphrase}\n{result_data[:234]}\n\n"
            )
            for key_data in result:
                wallet.write(f"{key_data[234:]}\n\n")
    return result


msig_opcodes = [
    0,
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59",
    "5a",
    "5b",
    "5c",
    "5d",
    "5e",
    "5f",
    "60",
]


def create_multisig(sig_total: int, ui):
    pubkeys = [getattr(ui, f"word{i}_box").text() for i in range(1, 25)]
    try:
        input_pubkeys = [bytes.fromhex(item) for item in pubkeys if item != ""]
    except ValueError:
        ui.output_textbrowser.setText("Error- Please check multisig field inputs")
        return

    pubkeylist = [(bytes([len(item)]) + item).hex() for item in input_pubkeys]
    total_pubs = len(pubkeylist)
    if total_pubs > 16:
        ui.output_textbrowser.setText("Maximum of 16 public keys allowed ")
        return
    elif sig_total > total_pubs:
        ui.output_textbrowser.setText(
            "Total Signatures Required must not be more than Total Signatures"
        )
        return

    pubkey_string = " ".join(pubkeylist)
    redeemscript_pre = bytes.fromhex(
        msig_opcodes[sig_total] + pubkey_string + msig_opcodes[total_pubs] + "ae"
    )
    redeemscript = len_in_hex(redeemscript_pre) + redeemscript_pre

    if ui.address_combobox.currentIndex() == 1:
        address = indv_P2SH_pub_key(redeemscript_pre, ui.testnet_checkbox.isChecked())
    elif ui.address_combobox.currentIndex() == 4:
        address = indv_P2WSH_pub_key(redeemscript_pre, ui.testnet_checkbox.isChecked())
    else:
        ui.output_textbrowser.setText("Select either P2SH or P2WSH address type")
        return

    result_text = f"REDEEMSCRIPT={redeemscript.hex()}\n\nADDRESS={address}"
    ui.output_textbrowser.setText(result_text)
    return redeemscript.hex()


def len_in_hex(item: Union[bytes, str, List]) -> bytes:
    length = len(item)
    if length < 0 or length > 18446744073709551615:
        raise ValueError("Length must be between 0 and 2^64 - 1")
    if length > 4294967295:
        return b"\xFF" + length.to_bytes(8, byteorder="little")
    elif length > 65535:
        return b"\xFE" + length.to_bytes(4, byteorder="little")
    elif length > 252:
        return b"\xFD" + length.to_bytes(2, byteorder="little")
    else:
        return length.to_bytes(1, byteorder="little")

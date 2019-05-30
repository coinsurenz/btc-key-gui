# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bip39-qdv1finalui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!



from address_functions import seed_to_master
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

class Ui_Bip39Tool(object):
    def setupUi(self, Bip39Tool):
        Bip39Tool.setObjectName("Bip39Tool")
        Bip39Tool.resize(1063, 1004)
        self.word20_label = QtWidgets.QLabel(Bip39Tool)
        self.word20_label.setGeometry(QtCore.QRect(570, 340, 62, 20))
        self.word20_label.setObjectName("word20_label")
        self.word19_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word19_box.setGeometry(QtCore.QRect(640, 290, 341, 32))
        self.word19_box.setObjectName("word19_box")
        self.word5_label = QtWidgets.QLabel(Bip39Tool)
        self.word5_label.setGeometry(QtCore.QRect(130, 220, 62, 20))
        self.word5_label.setObjectName("word5_label")
        self.word23_label = QtWidgets.QLabel(Bip39Tool)
        self.word23_label.setGeometry(QtCore.QRect(570, 460, 62, 20))
        self.word23_label.setObjectName("word23_label")
        self.derivationpath_box = QtWidgets.QLineEdit(Bip39Tool)
        self.derivationpath_box.setGeometry(QtCore.QRect(280, 680, 241, 32))
        self.derivationpath_box.setProperty("path_input", "")
        self.derivationpath_box.setObjectName("derivationpath_box")
        self.word6_label = QtWidgets.QLabel(Bip39Tool)
        self.word6_label.setGeometry(QtCore.QRect(130, 260, 62, 20))
        self.word6_label.setObjectName("word6_label")
        self.hardened_checkbox = QtWidgets.QCheckBox(Bip39Tool)
        self.hardened_checkbox.setGeometry(QtCore.QRect(530, 690, 191, 25))
        self.hardened_checkbox.setProperty("hardened_addresses", False)
        self.hardened_checkbox.setObjectName("hardened_checkbox")
        self.address_combobox = QtWidgets.QComboBox(Bip39Tool)
        self.address_combobox.setGeometry(QtCore.QRect(190, 680, 78, 30))
        self.address_combobox.setObjectName("address_combobox")
        self.address_combobox.addItems(['0','1','2','3','4','5','6','7'])
        self.address_combobox.activated.connect(address_combo_func)
        self.bip39pass_label = QtWidgets.QLabel(Bip39Tool)
        self.bip39pass_label.setGeometry(QtCore.QRect(190, 530, 111, 20))
        self.bip39pass_label.setObjectName("bip39pass_label")
        self.word8_label = QtWidgets.QLabel(Bip39Tool)
        self.word8_label.setGeometry(QtCore.QRect(130, 340, 62, 20))
        self.word8_label.setObjectName("word8_label")
        self.word7_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word7_box.setGeometry(QtCore.QRect(190, 290, 341, 32))
        self.word7_box.setObjectName("word7_box")
        self.numwords_combobox = QtWidgets.QComboBox(Bip39Tool)
        self.numwords_combobox.setGeometry(QtCore.QRect(30, 50, 71, 30))
        self.numwords_combobox.setObjectName("numwords_combobox")
        self.numwords_combobox.addItems(['0','1','2','3','4','5','6','7'])
        self.word13_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word13_box.setGeometry(QtCore.QRect(640, 50, 341, 32))
        self.word13_box.setObjectName("word13_box")
        self.output_textbrowser = QtWidgets.QTextBrowser(Bip39Tool)
        self.output_textbrowser.setGeometry(QtCore.QRect(20, 720, 1001, 231))
        self.output_textbrowser.setObjectName("output_textBrowser")
        self.word12_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word12_box.setGeometry(QtCore.QRect(190, 490, 341, 32))
        self.word12_box.setObjectName("word12_box")
        self.word10_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word10_box.setGeometry(QtCore.QRect(190, 410, 341, 32))
        self.word10_box.setObjectName("word10_box")
        self.numaddress_spinbox = QtWidgets.QSpinBox(Bip39Tool)
        self.numaddress_spinbox.setGeometry(QtCore.QRect(190, 620, 62, 32))
        self.numaddress_spinbox.setMinimum(1)
        self.numaddress_spinbox.setProperty("total_addresses_str", "")
        self.numaddress_spinbox.setObjectName("spinBox")
        self.numwords_combobox.currentIndexChanged.connect(num_words_func)
        self.word10_label = QtWidgets.QLabel(Bip39Tool)
        self.word10_label.setGeometry(QtCore.QRect(130, 420, 62, 20))
        self.word10_label.setObjectName("word10_label")
        self.word15_label = QtWidgets.QLabel(Bip39Tool)
        self.word15_label.setGeometry(QtCore.QRect(570, 140, 62, 20))
        self.word15_label.setObjectName("word15_label")
        self.word17_label = QtWidgets.QLabel(Bip39Tool)
        self.word17_label.setGeometry(QtCore.QRect(570, 220, 62, 20))
        self.word17_label.setObjectName("word17_label")
        self.word14_label = QtWidgets.QLabel(Bip39Tool)
        self.word14_label.setGeometry(QtCore.QRect(570, 100, 62, 20))
        self.word14_label.setObjectName("word14_label")
        self.word2_label = QtWidgets.QLabel(Bip39Tool)
        self.word2_label.setGeometry(QtCore.QRect(130, 100, 62, 20))
        self.word2_label.setObjectName("word2_label")
        self.title_label = QtWidgets.QLabel(Bip39Tool)
        self.title_label.setGeometry(QtCore.QRect(470, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.word22_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word22_box.setGeometry(QtCore.QRect(640, 410, 341, 32))
        self.word22_box.setObjectName("word22_box")
        self.word11_label = QtWidgets.QLabel(Bip39Tool)
        self.word11_label.setGeometry(QtCore.QRect(130, 460, 62, 20))
        self.word11_label.setObjectName("word11_label")
        self.word4_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word4_box.setGeometry(QtCore.QRect(190, 170, 341, 32))
        self.word4_box.setObjectName("word4_box")
        self.word24_label = QtWidgets.QLabel(Bip39Tool)
        self.word24_label.setGeometry(QtCore.QRect(570, 500, 62, 20))
        self.word24_label.setObjectName("word24_label")
        self.word16_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word16_box.setGeometry(QtCore.QRect(640, 170, 341, 32))
        self.word16_box.setObjectName("word16_box")
        self.word19_label = QtWidgets.QLabel(Bip39Tool)
        self.word19_label.setGeometry(QtCore.QRect(570, 300, 62, 20))
        self.word19_label.setObjectName("word19_label")
        self.numwords_label = QtWidgets.QLabel(Bip39Tool)
        self.numwords_label.setGeometry(QtCore.QRect(10, 30, 121, 20))
        self.numwords_label.setObjectName("numwords_label")
        self.word3_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word3_box.setGeometry(QtCore.QRect(190, 130, 341, 32))
        self.word3_box.setObjectName("word3_box")
        self.bip39pass_box = QtWidgets.QLineEdit(Bip39Tool)
        self.bip39pass_box.setGeometry(QtCore.QRect(190, 550, 791, 32))
        self.bip39pass_box.setProperty("bip39_passphrase", "")
        self.bip39pass_box.setObjectName("bip39pass_box")
        self.word23_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word23_box.setGeometry(QtCore.QRect(640, 450, 341, 32))
        self.word23_box.setObjectName("word23_box")
        self.word6_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word6_box.setGeometry(QtCore.QRect(190, 250, 341, 32))
        self.word6_box.setObjectName("word6_box")
        self.word15_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word15_box.setGeometry(QtCore.QRect(640, 130, 341, 32))
        self.word15_box.setObjectName("word15_box")
        self.word2_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word2_box.setGeometry(QtCore.QRect(190, 90, 341, 32))
        self.word2_box.setObjectName("word2_box")
        self.word18_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word18_box.setGeometry(QtCore.QRect(640, 250, 341, 32))
        self.word18_box.setObjectName("word18_box")
        self.word18_label = QtWidgets.QLabel(Bip39Tool)
        self.word18_label.setGeometry(QtCore.QRect(570, 260, 62, 20))
        self.word18_label.setObjectName("word18_label")
        self.word1_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word1_box.setGeometry(QtCore.QRect(190, 50, 341, 32))
        self.word1_box.setObjectName("word1_box")
        self.word12_label = QtWidgets.QLabel(Bip39Tool)
        self.word12_label.setGeometry(QtCore.QRect(130, 500, 62, 20))
        self.word12_label.setObjectName("word12_label")
        self.word4_label = QtWidgets.QLabel(Bip39Tool)
        self.word4_label.setGeometry(QtCore.QRect(130, 180, 62, 20))
        self.word4_label.setObjectName("word4_label")
        self.word21_label = QtWidgets.QLabel(Bip39Tool)
        self.word21_label.setGeometry(QtCore.QRect(570, 380, 62, 20))
        self.word21_label.setObjectName("word21_label")
        self.testnet_checkbox = QtWidgets.QCheckBox(Bip39Tool)
        self.testnet_checkbox.setGeometry(QtCore.QRect(530, 670, 93, 25))
        self.testnet_checkbox.setProperty("testnet", False)
        self.testnet_checkbox.setObjectName("testnet_checkbox")
        self.word1_label = QtWidgets.QLabel(Bip39Tool)
        self.word1_label.setGeometry(QtCore.QRect(130, 60, 62, 20))
        self.word1_label.setObjectName("word1_label")
        self.word16_label = QtWidgets.QLabel(Bip39Tool)
        self.word16_label.setGeometry(QtCore.QRect(570, 180, 62, 20))
        self.word16_label.setObjectName("word16_label")
        self.word9_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word9_box.setGeometry(QtCore.QRect(190, 370, 341, 32))
        self.word9_box.setObjectName("word9_box")
        self.word9_label = QtWidgets.QLabel(Bip39Tool)
        self.word9_label.setGeometry(QtCore.QRect(130, 380, 62, 20))
        self.word9_label.setObjectName("word9_label")
        self.numaddresses_label = QtWidgets.QLabel(Bip39Tool)
        self.numaddresses_label.setGeometry(QtCore.QRect(190, 590, 151, 20))
        self.numaddresses_label.setObjectName("numaddresses_label")
        self.okbutton_box = QtWidgets.QPushButton(Bip39Tool)
        self.okbutton_box.setGeometry(QtCore.QRect(940, 690, 80, 28))
        self.okbutton_box.setObjectName("okbutton_box")
        self.okbutton_box.clicked.connect(seed_button)
        self.word22_label = QtWidgets.QLabel(Bip39Tool)
        self.word22_label.setGeometry(QtCore.QRect(570, 420, 62, 20))
        self.word22_label.setObjectName("word22_label")
        self.word8_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word8_box.setGeometry(QtCore.QRect(190, 330, 341, 32))
        self.word8_box.setObjectName("word8_box")
        self.word21_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word21_box.setGeometry(QtCore.QRect(640, 370, 341, 32))
        self.word21_box.setObjectName("word21_box")
        self.word14_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word14_box.setGeometry(QtCore.QRect(640, 90, 341, 32))
        self.word14_box.setObjectName("word14_box")
        self.word13_label = QtWidgets.QLabel(Bip39Tool)
        self.word13_label.setGeometry(QtCore.QRect(570, 60, 62, 20))
        self.word13_label.setObjectName("word13_label")
        self.word11_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word11_box.setGeometry(QtCore.QRect(190, 450, 341, 32))
        self.word11_box.setObjectName("word11_box")
        self.word7_label = QtWidgets.QLabel(Bip39Tool)
        self.word7_label.setGeometry(QtCore.QRect(130, 300, 62, 20))
        self.word7_label.setObjectName("word7_label")
        self.word24_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word24_box.setGeometry(QtCore.QRect(640, 490, 341, 32))
        self.word24_box.setObjectName("word24_box")
        self.bip39_checkbox = QtWidgets.QCheckBox(Bip39Tool)
        self.bip39_checkbox.setGeometry(QtCore.QRect(850, 530, 151, 25))
        self.bip39_checkbox.setProperty("passphrase_option", False)
        self.bip39_checkbox.setObjectName("bip39_checkbox")
        self.bip39_checkbox.stateChanged.connect(lambda checked: 
            self.bip39pass_box.setEnabled(checked))
        self.bip39pass_box.setDisabled(True)
        self.word3_label = QtWidgets.QLabel(Bip39Tool)
        self.word3_label.setGeometry(QtCore.QRect(130, 140, 62, 20))
        self.word3_label.setObjectName("word3_label")
        self.word17_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word17_box.setGeometry(QtCore.QRect(640, 210, 341, 32))
        self.word17_box.setObjectName("word17_box")
        self.output_label = QtWidgets.QLabel(Bip39Tool)
        self.output_label.setGeometry(QtCore.QRect(20, 700, 62, 20))
        self.output_label.setObjectName("output_label")
        self.derivationpath_label = QtWidgets.QLabel(Bip39Tool)
        self.derivationpath_label.setGeometry(QtCore.QRect(290, 660, 121, 20))
        self.derivationpath_label.setObjectName("derivationpath_label")
        self.word5_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word5_box.setGeometry(QtCore.QRect(190, 210, 341, 32))
        self.word5_box.setObjectName("word5_box")
        self.word20_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word20_box.setGeometry(QtCore.QRect(640, 330, 341, 32))
        self.word20_box.setObjectName("word20_box")
        self.word4_box.setDisabled(True)  
        self.word5_box.setDisabled(True)  
        self.word6_box.setDisabled(True)
        self.word7_box.setDisabled(True)
        self.word8_box.setDisabled(True)  
        self.word9_box.setDisabled(True)  
        self.word10_box.setDisabled(True)  
        self.word11_box.setDisabled(True)  
        self.word12_box.setDisabled(True)  
        self.word13_box.setDisabled(True)
        self.word14_box.setDisabled(True)  
        self.word15_box.setDisabled(True)  
        self.word16_box.setDisabled(True)  
        self.word17_box.setDisabled(True)  
        self.word18_box.setDisabled(True)  
        self.word19_box.setDisabled(True)
        self.word20_box.setDisabled(True)  
        self.word21_box.setDisabled(True)  
        self.word22_box.setDisabled(True)  
        self.word23_box.setDisabled(True)  
        self.word24_box.setDisabled(True)  

        self.retranslateUi(Bip39Tool)
        QtCore.QMetaObject.connectSlotsByName(Bip39Tool)
        Bip39Tool.setTabOrder(self.numwords_combobox, self.word1_box)
        Bip39Tool.setTabOrder(self.word1_box, self.word2_box)
        Bip39Tool.setTabOrder(self.word2_box, self.word3_box)
        Bip39Tool.setTabOrder(self.word3_box, self.word4_box)
        Bip39Tool.setTabOrder(self.word4_box, self.word5_box)
        Bip39Tool.setTabOrder(self.word5_box, self.word6_box)
        Bip39Tool.setTabOrder(self.word6_box, self.word7_box)
        Bip39Tool.setTabOrder(self.word7_box, self.word8_box)
        Bip39Tool.setTabOrder(self.word8_box, self.word9_box)
        Bip39Tool.setTabOrder(self.word9_box, self.word10_box)
        Bip39Tool.setTabOrder(self.word10_box, self.word11_box)
        Bip39Tool.setTabOrder(self.word11_box, self.word12_box)
        Bip39Tool.setTabOrder(self.word12_box, self.word13_box)
        Bip39Tool.setTabOrder(self.word13_box, self.word14_box)
        Bip39Tool.setTabOrder(self.word14_box, self.word15_box)
        Bip39Tool.setTabOrder(self.word15_box, self.word16_box)
        Bip39Tool.setTabOrder(self.word16_box, self.word17_box)
        Bip39Tool.setTabOrder(self.word17_box, self.word18_box)
        Bip39Tool.setTabOrder(self.word18_box, self.word19_box)
        Bip39Tool.setTabOrder(self.word19_box, self.word20_box)
        Bip39Tool.setTabOrder(self.word20_box, self.word21_box)
        Bip39Tool.setTabOrder(self.word21_box, self.word22_box)
        Bip39Tool.setTabOrder(self.word22_box, self.word23_box)
        Bip39Tool.setTabOrder(self.word23_box, self.word24_box)
        Bip39Tool.setTabOrder(self.word24_box, self.bip39_checkbox)
        Bip39Tool.setTabOrder(self.bip39_checkbox, self.bip39pass_box)
        Bip39Tool.setTabOrder(self.bip39pass_box, self.numaddress_spinbox)
        Bip39Tool.setTabOrder(self.numaddress_spinbox, self.address_combobox)
        Bip39Tool.setTabOrder(self.address_combobox, self.derivationpath_box)
        Bip39Tool.setTabOrder(self.derivationpath_box, self.testnet_checkbox)
        Bip39Tool.setTabOrder(self.testnet_checkbox, self.hardened_checkbox)
        Bip39Tool.setTabOrder(self.hardened_checkbox, self.okbutton_box)
        Bip39Tool.setTabOrder(self.okbutton_box, self.output_textbrowser)

    def retranslateUi(self, Bip39Tool):
        _translate = QtCore.QCoreApplication.translate
        Bip39Tool.setWindowTitle(_translate("Bip39Tool", "Bip 39 Tool"))
        self.okbutton_box.setText(_translate("Dialog", "Generate"))
        self.word20_label.setText(_translate("Bip39Tool", "Word 20"))
        self.word5_label.setText(_translate("Bip39Tool", "Word 5"))
        self.word23_label.setText(_translate("Bip39Tool", "Word 23"))
        self.word6_label.setText(_translate("Bip39Tool", "Word 6"))
        self.hardened_checkbox.setText(_translate("Bip39Tool", "Hardened Addresses"))
        self.address_combobox.setItemText(0, _translate("Bip39Tool", "P2PKH"))
        self.address_combobox.setItemText(1, _translate("Bip39Tool", "P2SH"))
        self.address_combobox.setItemText(2, _translate("Bip39Tool", "P2WPKH"))
        self.address_combobox.setItemText(3, _translate("Bip39Tool", "P2WSH"))
        self.address_combobox.setItemText(4, _translate("Bip39Tool", "BIP44"))
        self.address_combobox.setItemText(5, _translate("Bip39Tool", "BIP49"))
        self.address_combobox.setItemText(6, _translate("Bip39Tool", "BIP84"))
        self.address_combobox.setItemText(7, _translate("Bip39Tool", "BIP141"))
        self.bip39pass_label.setText(_translate("Bip39Tool", "BIP39 Password"))
        self.word8_label.setText(_translate("Bip39Tool", "Word 8"))
        self.numwords_combobox.setItemText(0, _translate("Bip39Tool", "3"))
        self.numwords_combobox.setItemText(1, _translate("Bip39Tool", "6"))
        self.numwords_combobox.setItemText(2, _translate("Bip39Tool", "9"))
        self.numwords_combobox.setItemText(3, _translate("Bip39Tool", "12"))
        self.numwords_combobox.setItemText(4, _translate("Bip39Tool", "15"))
        self.numwords_combobox.setItemText(5, _translate("Bip39Tool", "18"))
        self.numwords_combobox.setItemText(6, _translate("Bip39Tool", "21"))
        self.numwords_combobox.setItemText(7, _translate("Bip39Tool", "24"))
        self.word10_label.setText(_translate("Bip39Tool", "Word 10"))
        self.word15_label.setText(_translate("Bip39Tool", "Word 15"))
        self.word17_label.setText(_translate("Bip39Tool", "Word 17"))
        self.word14_label.setText(_translate("Bip39Tool", "Word 14"))
        self.word2_label.setText(_translate("Bip39Tool", "Word 2"))
        self.title_label.setText(_translate("Bip39Tool", "BIP39 Key Tool"))
        self.word11_label.setText(_translate("Bip39Tool", "Word 11"))
        self.word24_label.setText(_translate("Bip39Tool", "Word 24"))
        self.word19_label.setText(_translate("Bip39Tool", "Word 19"))
        self.numwords_label.setText(_translate("Bip39Tool", "Number of Words"))
        self.word18_label.setText(_translate("Bip39Tool", "Word 18"))
        self.word12_label.setText(_translate("Bip39Tool", "Word 12"))
        self.word4_label.setText(_translate("Bip39Tool", "Word 4"))
        self.word21_label.setText(_translate("Bip39Tool", "Word 21"))
        self.testnet_checkbox.setText(_translate("Bip39Tool", "Testnet"))
        self.word1_label.setText(_translate("Bip39Tool", "Word 1"))
        self.word16_label.setText(_translate("Bip39Tool", "Word 16"))
        self.word9_label.setText(_translate("Bip39Tool", "Word 9"))
        self.numaddresses_label.setText(_translate("Bip39Tool", "Number of Addresses"))
        self.word22_label.setText(_translate("Bip39Tool", "Word 22"))
        self.word13_label.setText(_translate("Bip39Tool", "Word 13"))
        self.word7_label.setText(_translate("Bip39Tool", "Word 7"))
        self.bip39_checkbox.setText(_translate("Bip39Tool", "Use BIP39 Pass"))
        self.word3_label.setText(_translate("Bip39Tool", "Word 3"))
        self.output_label.setText(_translate("Bip39Tool", "Output"))
        self.derivationpath_label.setText(_translate("Bip39Tool", "Derivation Path"))


def path_derivation_func(path_string):
    hardened_item = [False, ]
    if path_string=='':
        path_string='m/0'
        ui.derivationpath_box.setText('m/')
    valid_char=['m','/','0','1','2','3','4','5','6','7','8','9', "'"]
    for char in path_string:
        if char not in valid_char:
            ui.output_textbrowser.setText("Invalid derivation path- example of correct format is m/1/2'/3")
            return 
    path_output_raw = path_string.replace('m', "")
    path_output_items = path_output_raw.strip('/').split('/')

    for item in path_output_items:
        if "'" in item:
            hardened_item.append(True)
        else:
            hardened_item.append(False)
    derivation_path = [(item.strip("'")) for item in path_output_items]

    if derivation_path==['']:
        derivation_path=[0]
    result=[derivation_path, hardened_item]
    return result

def address_combo_func(data):
    address_data=['p2pkh','p2sh','p2wpkh','p2wsh','bip44','bip49', 'bip84', 'bip141']
    selection=address_data[data]
    if selection=='bip44':
        ui.derivationpath_box.setDisabled(True)
        ui.derivationpath_box.setText("m/44'/0'/0'/0")
        ui.hardened_checkbox.setDisabled(True)
        ui.hardened_checkbox.setChecked(False)
    elif selection=='bip49':
        ui.derivationpath_box.setDisabled(True)
        ui.derivationpath_box.setText("m/49'/0'/0'/0")
        ui.hardened_checkbox.setDisabled(True)
        ui.hardened_checkbox.setChecked(False)
    elif selection=='bip84':
        ui.derivationpath_box.setDisabled(True)
        ui.derivationpath_box.setText("m/84'/0'/0'/0")
        ui.hardened_checkbox.setDisabled(True)
        ui.hardened_checkbox.setChecked(False)
    else:
        ui.derivationpath_box.setDisabled(False)
        ui.hardened_checkbox.setDisabled(False)
    return selection
    

def num_words_func(data):
    address_data=['3','6','9','12','15','18', '21', '24']
    selection=address_data[data]
    words=[ui.word1_box,ui.word2_box,ui.word3_box,ui.word4_box,ui.word5_box,
    ui.word6_box,ui.word7_box,ui.word8_box,ui.word9_box,ui.word10_box,
    ui.word11_box,ui.word12_box,ui.word13_box,ui.word14_box,ui.word15_box,
    ui.word16_box,ui.word17_box,ui.word18_box,ui.word19_box,ui.word20_box,
    ui.word21_box,ui.word22_box,ui.word23_box,ui.word24_box]

    if selection=='3':
        for wordbox in words[3:]:
            wordbox.setDisabled(True)
            for wordbox in words[:3]:
                wordbox.setDisabled(False)
    elif selection=='6':
        for wordbox in words[6:]:
            wordbox.setDisabled(True)
            for wordbox in words[:6]:
                wordbox.setDisabled(False)
    elif selection=='9':
        for wordbox in words[9:]:
            wordbox.setDisabled(True)
            for wordbox in words[:9]:
                wordbox.setDisabled(False)
    elif selection=='12':
        for wordbox in words[12:]:
            wordbox.setDisabled(True)
            for wordbox in words[:12]:
                wordbox.setDisabled(False)
    elif selection=='15':
        for wordbox in words[15:]:
            wordbox.setDisabled(True)
            for wordbox in words[:15]:
                wordbox.setDisabled(False)
    elif selection=='18':
        for wordbox in words[18:]:
            wordbox.setDisabled(True)
            for wordbox in words[:18]:
                wordbox.setDisabled(False)
    elif selection=='21':
        for wordbox in words[21:]:
            wordbox.setDisabled(True)
            for wordbox in words[:21]:
                wordbox.setDisabled(False)
    elif selection=='24':
        for wordbox in words:
            wordbox.setDisabled(False)
    return selection
    

def seed_button():
        words=[ui.word1_box.text(),ui.word2_box.text(),ui.word3_box.text(),ui.word4_box.text(),
        ui.word5_box.text(),ui.word6_box.text(),ui.word7_box.text(),ui.word8_box.text(),
        ui.word9_box.text(),ui.word10_box.text(),ui.word11_box.text(),ui.word12_box.text(),
        ui.word13_box.text(),ui.word14_box.text(),ui.word15_box.text(),ui.word16_box.text(),
        ui.word17_box.text(),ui.word18_box.text(),ui.word19_box.text(),ui.word20_box.text(),
        ui.word21_box.text(),ui.word22_box.text(),ui.word23_box.text(),ui.word24_box.text()]
        words_list=[(item) for item in words if item is not ""]
        seed=" ".join(words_list)
        passphrase=ui.bip39pass_box.text()
        derivation_path_data=path_derivation_func(ui.derivationpath_box.text())
        try:
            derivation_path=derivation_path_data[0]
        except TypeError:
            return
        hardened_items=derivation_path_data[1]
        if hardened_items is not type(list):
            hardened_items=[item for item in hardened_items]
        total_addresses=ui.numaddress_spinbox.value()
        address_type=address_combo_func(ui.address_combobox.currentIndex())
        testnet=ui.testnet_checkbox.isChecked()
        if ui.hardened_checkbox.isChecked()== True:
            hardened_items.append(True)
        else:
            hardened_items.append(False)
        if address_type=='bip44':
            address_type='p2pkh'
            hardened_items = [False, True, True, True, False, False]
            derivation_path = [44, 0, 0, 0, ]
        elif address_type=='bip49':
            address_type='p2sh'
            hardened_items = [False, True, True, True, False, False]
            derivation_path = [49, 0, 0, 0, ]
        elif address_type=='bip84':
            address_type='p2wpkh'
            hardened_items = [False, True, True, True, False, False]
            derivation_path = [84, 0, 0, 0, ]
        elif address_type=='bip141':
            address_type='p2sh' 
            hardened_items[-1]=False
        result=seed_to_master(seed, passphrase, derivation_path, 
            hardened_items, total_addresses, address_type, testnet)
        result_data=''
        for key_data in result:
            result_data+=(key_data)
            result_data+=('\n')
            result_data+=('\n')
            ui.output_textbrowser.setText(result_data)
        wallet = open("wallet.txt","a")
        wallet.writelines(['\n','**NEW WALLET KEYS ADDED**- ',
            str(datetime.datetime.now()),'\n',' SEED=',seed, 
            ' PASSPHRASE=',passphrase,'\n',result_data[:123],'\n','\n'])
        for key_data in result:
            wallet.writelines([key_data, '\n','\n'])
        wallet.close() 
        return result




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bip39Tool = QtWidgets.QDialog()
    ui = Ui_Bip39Tool()
    ui.setupUi(Bip39Tool)
    Bip39Tool.show()
    sys.exit(app.exec_())


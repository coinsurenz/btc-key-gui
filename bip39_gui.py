# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bip39-qdv2finalui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import datetime

from address_functions import seed_to_master, indv_P2SH_pub_key, indv_P2WSH_pub_key
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Bip39Tool(object):
    def setupUi(self, Bip39Tool):
        Bip39Tool.setObjectName("Bip39Tool")
        Bip39Tool.resize(1450, 750)
        self.gridLayout = QtWidgets.QGridLayout(Bip39Tool)
        self.gridLayout.setObjectName("gridLayout")
        self.hardened_checkbox = QtWidgets.QCheckBox(Bip39Tool)
        self.hardened_checkbox.setProperty("hardened_addresses", False)
        self.hardened_checkbox.setObjectName("hardened_checkbox")
        self.gridLayout.addWidget(self.hardened_checkbox, 17, 5, 1, 1)
        self.word2_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word2_box.sizePolicy().hasHeightForWidth())
        self.word2_box.setSizePolicy(sizePolicy)
        self.word2_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word2_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word2_box.setObjectName("word2_box")
        self.gridLayout.addWidget(self.word2_box, 3, 4, 1, 1)
        self.bip39pass_label = QtWidgets.QLabel(Bip39Tool)
        self.bip39pass_label.setObjectName("bip39pass_label")
        self.gridLayout.addWidget(self.bip39pass_label, 14, 4, 1, 1)
        self.output_textbrowser = QtWidgets.QTextBrowser(Bip39Tool)
        self.output_textbrowser.setMinimumSize(QtCore.QSize(0, 600))
        self.output_textbrowser.setObjectName("output_textbrowser")
        self.gridLayout.addWidget(self.output_textbrowser, 2, 6, 15, 2)
        self.word5_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word5_box.sizePolicy().hasHeightForWidth())
        self.word5_box.setSizePolicy(sizePolicy)
        self.word5_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word5_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word5_box.setObjectName("word5_box")
        self.gridLayout.addWidget(self.word5_box, 6, 4, 1, 1)
        self.address_combobox = QtWidgets.QComboBox(Bip39Tool)
        self.address_combobox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.address_combobox.setObjectName("address_combobox")
        self.address_combobox.addItems(['0','1','2','3','4','5','6','7','8'])
        self.gridLayout.addWidget(self.address_combobox, 20, 4, 1, 1)
        self.address_combobox.activated.connect(address_combo_func)
        self.derivationpath_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.derivationpath_box.sizePolicy().hasHeightForWidth())
        self.derivationpath_box.setSizePolicy(sizePolicy)
        self.derivationpath_box.setMinimumSize(QtCore.QSize(0, 35))
        self.derivationpath_box.setMaximumSize(QtCore.QSize(500, 16777215))
        self.derivationpath_box.setProperty("path_input", "")
        self.derivationpath_box.setObjectName("derivationpath_box")
        self.gridLayout.addWidget(self.derivationpath_box, 19, 4, 1, 1)
        self.word21_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word21_box.sizePolicy().hasHeightForWidth())
        self.word21_box.setSizePolicy(sizePolicy)
        self.word21_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word21_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word21_box.setObjectName("word21_box")
        self.gridLayout.addWidget(self.word21_box, 10, 5, 1, 1)
        self.word18_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word18_box.sizePolicy().hasHeightForWidth())
        self.word18_box.setSizePolicy(sizePolicy)
        self.word18_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word18_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word18_box.setObjectName("word18_box")
        self.gridLayout.addWidget(self.word18_box, 7, 5, 1, 1)
        self.word17_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word17_box.sizePolicy().hasHeightForWidth())
        self.word17_box.setSizePolicy(sizePolicy)
        self.word17_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word17_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word17_box.setObjectName("word17_box")
        self.gridLayout.addWidget(self.word17_box, 6, 5, 1, 1)
        self.word1_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word1_box.sizePolicy().hasHeightForWidth())
        self.word1_box.setSizePolicy(sizePolicy)
        self.word1_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word1_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word1_box.setObjectName("word1_box")
        self.gridLayout.addWidget(self.word1_box, 2, 4, 1, 1)
        self.word14_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word14_box.sizePolicy().hasHeightForWidth())
        self.word14_box.setSizePolicy(sizePolicy)
        self.word14_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word14_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word14_box.setObjectName("word14_box")
        self.gridLayout.addWidget(self.word14_box, 3, 5, 1, 1)
        self.word20_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word20_box.sizePolicy().hasHeightForWidth())
        self.word20_box.setSizePolicy(sizePolicy)
        self.word20_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word20_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word20_box.setObjectName("word20_box")
        self.gridLayout.addWidget(self.word20_box, 9, 5, 1, 1)
        self.word19_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word19_box.sizePolicy().hasHeightForWidth())
        self.word19_box.setSizePolicy(sizePolicy)
        self.word19_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word19_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word19_box.setObjectName("word19_box")
        self.gridLayout.addWidget(self.word19_box, 8, 5, 1, 1)
        self.word15_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word15_box.sizePolicy().hasHeightForWidth())
        self.word15_box.setSizePolicy(sizePolicy)
        self.word15_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word15_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word15_box.setObjectName("word15_box")
        self.gridLayout.addWidget(self.word15_box, 4, 5, 1, 1)
        self.word4_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word4_box.sizePolicy().hasHeightForWidth())
        self.word4_box.setSizePolicy(sizePolicy)
        self.word4_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word4_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word4_box.setObjectName("word4_box")
        self.gridLayout.addWidget(self.word4_box, 5, 4, 1, 1)
        self.word22_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word22_box.sizePolicy().hasHeightForWidth())
        self.word22_box.setSizePolicy(sizePolicy)
        self.word22_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word22_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word22_box.setObjectName("word22_box")
        self.gridLayout.addWidget(self.word22_box, 11, 5, 1, 1)
        self.word23_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word23_box.sizePolicy().hasHeightForWidth())
        self.word23_box.setSizePolicy(sizePolicy)
        self.word23_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word23_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word23_box.setObjectName("word23_box")
        self.gridLayout.addWidget(self.word23_box, 12, 5, 1, 1)
        self.word24_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word24_box.sizePolicy().hasHeightForWidth())
        self.word24_box.setSizePolicy(sizePolicy)
        self.word24_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word24_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word24_box.setObjectName("word24_box")
        self.gridLayout.addWidget(self.word24_box, 13, 5, 1, 1)
        self.word16_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word16_box.sizePolicy().hasHeightForWidth())
        self.word16_box.setSizePolicy(sizePolicy)
        self.word16_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word16_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word16_box.setObjectName("word16_box")
        self.gridLayout.addWidget(self.word16_box, 5, 5, 1, 1)
        self.word6_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word6_box.sizePolicy().hasHeightForWidth())
        self.word6_box.setSizePolicy(sizePolicy)
        self.word6_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word6_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word6_box.setObjectName("word6_box")
        self.gridLayout.addWidget(self.word6_box, 7, 4, 1, 1)
        self.word7_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word7_box.sizePolicy().hasHeightForWidth())
        self.word7_box.setSizePolicy(sizePolicy)
        self.word7_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word7_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word7_box.setObjectName("word7_box")
        self.gridLayout.addWidget(self.word7_box, 8, 4, 1, 1)
        self.title_label = QtWidgets.QLabel(Bip39Tool)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.gridLayout.addWidget(self.title_label, 0, 5, 1, 1)
        self.word13_box = QtWidgets.QLineEdit(Bip39Tool)
        self.word13_box.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word13_box.sizePolicy().hasHeightForWidth())
        self.word13_box.setSizePolicy(sizePolicy)
        self.word13_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word13_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word13_box.setObjectName("word13_box")
        self.gridLayout.addWidget(self.word13_box, 2, 5, 1, 1)
        self.numaddress_spinbox = QtWidgets.QSpinBox(Bip39Tool)
        self.numaddress_spinbox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.numaddress_spinbox.setMinimum(1)
        self.numaddress_spinbox.setProperty("total_addresses_str", "")
        self.numaddress_spinbox.setObjectName("numaddress_spinbox")
        self.gridLayout.addWidget(self.numaddress_spinbox, 20, 5, 1, 1)
        self.derivationpath_label = QtWidgets.QLabel(Bip39Tool)
        self.derivationpath_label.setObjectName("derivationpath_label")
        self.gridLayout.addWidget(self.derivationpath_label, 18, 4, 1, 1)
        self.word9_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word9_box.sizePolicy().hasHeightForWidth())
        self.word9_box.setSizePolicy(sizePolicy)
        self.word9_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word9_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word9_box.setObjectName("word9_box")
        self.gridLayout.addWidget(self.word9_box, 10, 4, 1, 1)
        self.testnet_checkbox = QtWidgets.QCheckBox(Bip39Tool)
        self.testnet_checkbox.setProperty("testnet", False)
        self.testnet_checkbox.setObjectName("testnet_checkbox")
        self.gridLayout.addWidget(self.testnet_checkbox, 18, 5, 1, 1)
        self.word3_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word3_box.sizePolicy().hasHeightForWidth())
        self.word3_box.setSizePolicy(sizePolicy)
        self.word3_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word3_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word3_box.setObjectName("word3_box")
        self.gridLayout.addWidget(self.word3_box, 4, 4, 1, 1)
        self.textfile_CheckBox = QtWidgets.QCheckBox(Bip39Tool)
        self.textfile_CheckBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.textfile_CheckBox, 19, 6, 1, 1)
        self.word8_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word8_box.sizePolicy().hasHeightForWidth())
        self.word8_box.setSizePolicy(sizePolicy)
        self.word8_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word8_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word8_box.setObjectName("word8_box")
        self.gridLayout.addWidget(self.word8_box, 9, 4, 1, 1)
        self.word12_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word12_box.sizePolicy().hasHeightForWidth())
        self.word12_box.setSizePolicy(sizePolicy)
        self.word12_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word12_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word12_box.setObjectName("word12_box")
        self.gridLayout.addWidget(self.word12_box, 13, 4, 1, 1)
        self.word10_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word10_box.sizePolicy().hasHeightForWidth())
        self.word10_box.setSizePolicy(sizePolicy)
        self.word10_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word10_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word10_box.setObjectName("word10_box")
        self.gridLayout.addWidget(self.word10_box, 11, 4, 1, 1)
        self.word11_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word11_box.sizePolicy().hasHeightForWidth())
        self.word11_box.setSizePolicy(sizePolicy)
        self.word11_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word11_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word11_box.setObjectName("word11_box")
        self.gridLayout.addWidget(self.word11_box, 12, 4, 1, 1)
        self.numaddresses_label = QtWidgets.QLabel(Bip39Tool)
        self.numaddresses_label.setObjectName("numaddresses_label")
        self.gridLayout.addWidget(self.numaddresses_label, 19, 5, 1, 1)
        self.numwords_label = QtWidgets.QLabel(Bip39Tool)
        self.numwords_label.setObjectName("numwords_label")
        self.gridLayout.addWidget(self.numwords_label, 0, 4, 1, 1)
        self.numwords_combobox = QtWidgets.QComboBox(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numwords_combobox.sizePolicy().hasHeightForWidth())
        self.numwords_combobox.setSizePolicy(sizePolicy)
        self.numwords_combobox.setObjectName("numwords_combobox")
        self.numwords_combobox.addItems(['0','1','2','3','4','5','6','7'])
        self.numwords_combobox.currentIndexChanged.connect(num_words_func)
        self.gridLayout.addWidget(self.numwords_combobox, 1, 4, 1, 1)
        self.okbutton_box = QtWidgets.QPushButton(Bip39Tool)
        self.okbutton_box.setText("Generate")
        self.okbutton_box.setObjectName("okbutton_box")
        self.okbutton_box.clicked.connect(seed_button)
        self.gridLayout.addWidget(self.okbutton_box, 19, 7, 1, 1)
        self.bip39_checkbox = QtWidgets.QCheckBox(Bip39Tool)
        self.bip39_checkbox.setProperty("passphrase_option", False)
        self.bip39_checkbox.setObjectName("bip39_checkbox")
        self.gridLayout.addWidget(self.bip39_checkbox, 14, 5, 1, 1)
        self.bip39_checkbox.stateChanged.connect(lambda checked:
            self.bip39pass_box.setEnabled(checked)) 
        self.bip39pass_box = QtWidgets.QLineEdit(Bip39Tool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.bip39pass_box.sizePolicy().hasHeightForWidth())
        self.bip39pass_box.setSizePolicy(sizePolicy)
        self.bip39pass_box.setMinimumSize(QtCore.QSize(20, 35))
        self.bip39pass_box.setProperty("bip39_passphrase", "")
        self.bip39pass_box.setObjectName("bip39pass_box")
        self.bip39pass_box.setDisabled(True)
        self.gridLayout.addWidget(self.bip39pass_box, 15, 4, 1, 2)
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
        Bip39Tool.setTabOrder(self.word24_box, self.bip39pass_box)
        Bip39Tool.setTabOrder(self.bip39pass_box, self.bip39_checkbox)
        Bip39Tool.setTabOrder(self.bip39_checkbox, self.hardened_checkbox)
        Bip39Tool.setTabOrder(self.hardened_checkbox, self.testnet_checkbox)
        Bip39Tool.setTabOrder(self.testnet_checkbox, self.derivationpath_box)
        Bip39Tool.setTabOrder(self.derivationpath_box, self.address_combobox)
        Bip39Tool.setTabOrder(self.address_combobox, self.numaddress_spinbox)
        Bip39Tool.setTabOrder(self.numaddress_spinbox, self.textfile_CheckBox)
        Bip39Tool.setTabOrder(self.textfile_CheckBox, self.okbutton_box)
        Bip39Tool.setTabOrder(self.okbutton_box, self.output_textbrowser)

    def retranslateUi(self, Bip39Tool):
        _translate = QtCore.QCoreApplication.translate
        Bip39Tool.setWindowTitle(_translate("Bip39Tool", "Bip 39 Tool"))
        self.hardened_checkbox.setText(_translate("Bip39Tool", "Hardened Addresses"))
        self.word2_box.setPlaceholderText(_translate("Bip39Tool", "Word2"))
        self.bip39pass_label.setText(_translate("Bip39Tool", "BIP39 Password"))
        self.word5_box.setPlaceholderText(_translate("Bip39Tool", "Word5"))
        self.address_combobox.setItemText(0, _translate("Bip39Tool", "P2PKH"))
        self.address_combobox.setItemText(1, _translate("Bip39Tool", "P2SH"))
        self.address_combobox.setItemText(2, _translate("Bip39Tool", "P2WPKH-P2SH"))
        self.address_combobox.setItemText(3, _translate("Bip39Tool", "P2WPKH"))
        self.address_combobox.setItemText(4, _translate("Bip39Tool", "P2WSH"))
        self.address_combobox.setItemText(5, _translate("Bip39Tool", "BIP44"))
        self.address_combobox.setItemText(6, _translate("Bip39Tool", "BIP49"))
        self.address_combobox.setItemText(7, _translate("Bip39Tool", "BIP84"))
        self.address_combobox.setItemText(8, _translate("Bip39Tool", "BIP141"))
        self.derivationpath_box.setPlaceholderText(_translate("Bip39Tool", "m/0 etc..."))
        self.word21_box.setPlaceholderText(_translate("Bip39Tool", "Word21"))
        self.word18_box.setPlaceholderText(_translate("Bip39Tool", "Word18"))
        self.word17_box.setPlaceholderText(_translate("Bip39Tool", "Word17"))
        self.word1_box.setPlaceholderText(_translate("Bip39Tool", "Word1"))
        self.word14_box.setPlaceholderText(_translate("Bip39Tool", "Word14"))
        self.word20_box.setPlaceholderText(_translate("Bip39Tool", "Word20"))
        self.word19_box.setPlaceholderText(_translate("Bip39Tool", "Word19"))
        self.word15_box.setPlaceholderText(_translate("Bip39Tool", "Word15"))
        self.word4_box.setPlaceholderText(_translate("Bip39Tool", "Word4"))
        self.word22_box.setPlaceholderText(_translate("Bip39Tool", "Word22"))
        self.word23_box.setPlaceholderText(_translate("Bip39Tool", "Word23"))
        self.word24_box.setPlaceholderText(_translate("Bip39Tool", "Word24"))
        self.word16_box.setPlaceholderText(_translate("Bip39Tool", "Word16"))
        self.word6_box.setPlaceholderText(_translate("Bip39Tool", "Word6"))
        self.word7_box.setPlaceholderText(_translate("Bip39Tool", "Word7"))
        self.title_label.setText(_translate("Bip39Tool", "BIP39 Key Tool"))
        self.word13_box.setPlaceholderText(_translate("Bip39Tool", "Word13"))
        self.derivationpath_label.setText(_translate("Bip39Tool", "Derivation Path"))
        self.word9_box.setPlaceholderText(_translate("Bip39Tool", "Word9"))
        self.testnet_checkbox.setText(_translate("Bip39Tool", "Testnet"))
        self.word3_box.setPlaceholderText(_translate("Bip39Tool", "Word3"))
        self.textfile_CheckBox.setText(_translate("Bip39Tool", "Output to Textfile"))
        self.word8_box.setPlaceholderText(_translate("Bip39Tool", "Word8"))
        self.word12_box.setPlaceholderText(_translate("Bip39Tool", "Word12"))
        self.word10_box.setPlaceholderText(_translate("Bip39Tool", "Word10"))
        self.word11_box.setPlaceholderText(_translate("Bip39Tool", "Word11"))
        self.numaddresses_label.setText(_translate("Bip39Tool", "Number of Addresses"))
        self.numwords_label.setText(_translate("Bip39Tool", "Number of Words"))
        self.numwords_combobox.setItemText(0, _translate("Bip39Tool", "3"))
        self.numwords_combobox.setItemText(1, _translate("Bip39Tool", "6"))
        self.numwords_combobox.setItemText(2, _translate("Bip39Tool", "9"))
        self.numwords_combobox.setItemText(3, _translate("Bip39Tool", "12"))
        self.numwords_combobox.setItemText(4, _translate("Bip39Tool", "15"))
        self.numwords_combobox.setItemText(5, _translate("Bip39Tool", "18"))
        self.numwords_combobox.setItemText(6, _translate("Bip39Tool", "21"))
        self.numwords_combobox.setItemText(7, _translate("Bip39Tool", "24"))
        self.bip39_checkbox.setText(_translate("Bip39Tool", "Use BIP39 Pass"))


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
    # address_data=['p2pkh','p2sh','p2wpkh','p2wsh','bip44','bip49', 'bip84', 'bip141']
    address_data=['p2pkh','p2sh','p2wpkh-p2sh','p2wpkh','p2wsh','bip44','bip49', 'bip84', 'bip141']
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

    # if ui.textfile_CheckBox.isChecked()== True:
    #     create_multisig(ui.numaddress_spinbox.value())
    #     pass


    # else:

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
    result_data+=(result[0])[:234]
    result_data+='\n'
    for key_data in result:
        result_data+=key_data[234:]
        result_data+='\n'
        result_data+='\n'
        ui.output_textbrowser.setText(result_data)
    if ui.textfile_CheckBox.isChecked()== False:
        pass
    else:
        wallet = open("data.txt","a")
        wallet.writelines(['\n','**NEW WALLET KEYS ADDED**- ',
            str(datetime.datetime.now()),'\n',' SEED=',seed, 
            ' PASSPHRASE=',passphrase,'\n',result_data[:234],'\n','\n'])            
        for key_data in result:
            wallet.writelines([key_data[234:],'\n','\n'])
        wallet.close() 
    return result


msig_opcodes=[0, '51', '52', '53', '54' , '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60']

def create_multisig(sig_total):
    pubkeys=[ui.word1_box.text(),ui.word2_box.text(),ui.word3_box.text(),ui.word4_box.text(),
    ui.word5_box.text(),ui.word6_box.text(),ui.word7_box.text(),ui.word8_box.text(),
    ui.word9_box.text(),ui.word10_box.text(),ui.word11_box.text(),ui.word12_box.text(),
    ui.word13_box.text(),ui.word14_box.text(),ui.word15_box.text(),ui.word16_box.text(),
    ui.word17_box.text(),ui.word18_box.text(),ui.word19_box.text(),ui.word20_box.text(),
    ui.word21_box.text(),ui.word22_box.text(),ui.word23_box.text(),ui.word24_box.text()]
    input_pubkeys=[(bytes.fromhex(item)) for item in pubkeys if item is not ""]
    pubkeylist=[(bytes([len(item)])+item).hex() for item in input_pubkeys]
    total_pubs=len(pubkeylist)
    if total_pubs > 16:
        ui.output_textbrowser.setText('Maximum of 16 public keys allowed ')
        return
    elif sig_total > total_pubs:
        ui.output_textbrowser.setText('Total Signatures Required must not be more than Total Signatures')
        return

    pubkey_string=" ".join(pubkeylist)
    redeemscript_pre=bytes.fromhex(msig_opcodes[sig_total]+pubkey_string+msig_opcodes[total_pubs]+'ae')
    redeemscript=bytes([len(redeemscript_pre)])+redeemscript_pre
    if ui.address_combobox.currentIndex()==1:
        address=indv_P2SH_pub_key(redeemscript_pre, ui.testnet_checkbox.isChecked())

    elif ui.address_combobox.currentIndex()==4 :
        address=indv_P2WSH_pub_key(redeemscript_pre, ui.testnet_checkbox.isChecked())

    else:
        ui.output_textbrowser.setText('Select either P2SH or P2WSH address type')
        return
    result_text='REDEEMSCRIPT='+redeemscript.hex()+'\n'+'\n'+'ADDRESS='+address
    ui.output_textbrowser.setText(result_text)

    return redeemscript.hex()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('app_icon.png'))
    Bip39Tool = QtWidgets.QDialog()
    ui = Ui_Bip39Tool()
    ui.setupUi(Bip39Tool)
    Bip39Tool.show()
    sys.exit(app.exec_())



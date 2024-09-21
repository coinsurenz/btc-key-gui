# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bip39-qdv2finalui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QDesktopWidget

from ui.ui_functions import address_combo_func, num_words_func, seed_button


class Ui_Bip39Tool(object):
    def setupUi(self, Bip39Tool):
        Bip39Tool.setObjectName("Bip39Tool")

        # Get the screen size
        screen = QDesktopWidget().screenNumber(QDesktopWidget().cursor().pos())
        screen_size = QDesktopWidget().screenGeometry(screen)

        # Set the window size to 90% of the screen size
        width = int(screen_size.width() * 0.9)
        height = int(screen_size.height() * 0.9)
        Bip39Tool.resize(width, height)

        # Create a scroll area
        self.scrollArea = QScrollArea(Bip39Tool)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        # Create a widget to hold the content
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # Create a vertical layout for the content
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        # Create a widget to hold the grid layout
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.verticalLayout.addWidget(self.gridLayoutWidget)

        # Create the grid layout
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")

        self.word1_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word1_box.sizePolicy().hasHeightForWidth())
        self.word1_box.setSizePolicy(sizePolicy)
        self.word1_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word1_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word1_box.setObjectName("word1_box")
        self.gridLayout.addWidget(self.word1_box, 3, 4, 1, 1)
        self.word12_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word12_box.sizePolicy().hasHeightForWidth())
        self.word12_box.setSizePolicy(sizePolicy)
        self.word12_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word12_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word12_box.setObjectName("word12_box")
        self.gridLayout.addWidget(self.word12_box, 14, 4, 1, 1)
        self.textfile_CheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(13)
        self.textfile_CheckBox.setFont(font)
        self.textfile_CheckBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.textfile_CheckBox, 20, 5, 1, 1)
        self.derivationpath_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(13)
        self.derivationpath_label.setFont(font)
        self.derivationpath_label.setObjectName("derivationpath_label")
        self.gridLayout.addWidget(self.derivationpath_label, 17, 4, 1, 1)
        self.address_combobox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.address_combobox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.address_combobox.setObjectName("address_combobox")
        self.gridLayout.addWidget(self.address_combobox, 20, 4, 1, 1)
        self.word8_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word8_box.sizePolicy().hasHeightForWidth())
        self.word8_box.setSizePolicy(sizePolicy)
        self.word8_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word8_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word8_box.setObjectName("word8_box")
        self.gridLayout.addWidget(self.word8_box, 10, 4, 1, 1)
        self.numwords_combobox = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.numwords_combobox.sizePolicy().hasHeightForWidth()
        )
        self.numwords_combobox.setSizePolicy(sizePolicy)
        self.numwords_combobox.setObjectName("numwords_combobox")
        self.gridLayout.addWidget(self.numwords_combobox, 2, 4, 1, 1)
        self.okbutton_box = QtWidgets.QDialogButtonBox(self.gridLayoutWidget)
        self.okbutton_box.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok
        )
        self.okbutton_box.setObjectName("okbutton_box")
        self.gridLayout.addWidget(self.okbutton_box, 21, 7, 1, 1)
        self.word3_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word3_box.sizePolicy().hasHeightForWidth())
        self.word3_box.setSizePolicy(sizePolicy)
        self.word3_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word3_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word3_box.setObjectName("word3_box")
        self.gridLayout.addWidget(self.word3_box, 5, 4, 1, 1)
        self.bip39pass_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(13)
        self.bip39pass_label.setFont(font)
        self.bip39pass_label.setObjectName("bip39pass_label")
        self.gridLayout.addWidget(self.bip39pass_label, 15, 4, 1, 1)
        self.word18_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word18_box.sizePolicy().hasHeightForWidth())
        self.word18_box.setSizePolicy(sizePolicy)
        self.word18_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word18_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word18_box.setObjectName("word18_box")
        self.gridLayout.addWidget(self.word18_box, 8, 5, 1, 1)
        self.hardened_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(13)
        self.hardened_checkbox.setFont(font)
        self.hardened_checkbox.setProperty("hardened_addresses", False)
        self.hardened_checkbox.setObjectName("hardened_checkbox")
        self.gridLayout.addWidget(self.hardened_checkbox, 17, 5, 1, 1)
        self.word17_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word17_box.sizePolicy().hasHeightForWidth())
        self.word17_box.setSizePolicy(sizePolicy)
        self.word17_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word17_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word17_box.setObjectName("word17_box")
        self.gridLayout.addWidget(self.word17_box, 7, 5, 1, 1)
        self.word23_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word23_box.sizePolicy().hasHeightForWidth())
        self.word23_box.setSizePolicy(sizePolicy)
        self.word23_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word23_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word23_box.setObjectName("word23_box")
        self.gridLayout.addWidget(self.word23_box, 13, 5, 1, 1)
        self.word24_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word24_box.sizePolicy().hasHeightForWidth())
        self.word24_box.setSizePolicy(sizePolicy)
        self.word24_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word24_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word24_box.setObjectName("word24_box")
        self.gridLayout.addWidget(self.word24_box, 14, 5, 1, 1)
        self.testnet_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(13)
        self.testnet_checkbox.setFont(font)
        self.testnet_checkbox.setProperty("testnet", False)
        self.testnet_checkbox.setObjectName("testnet_checkbox")
        self.gridLayout.addWidget(self.testnet_checkbox, 19, 5, 1, 1)
        self.word10_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word10_box.sizePolicy().hasHeightForWidth())
        self.word10_box.setSizePolicy(sizePolicy)
        self.word10_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word10_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word10_box.setObjectName("word10_box")
        self.gridLayout.addWidget(self.word10_box, 12, 4, 1, 1)
        self.word9_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word9_box.sizePolicy().hasHeightForWidth())
        self.word9_box.setSizePolicy(sizePolicy)
        self.word9_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word9_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word9_box.setObjectName("word9_box")
        self.gridLayout.addWidget(self.word9_box, 11, 4, 1, 1)
        self.numwords_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.numwords_label.setMaximumSize(QtCore.QSize(250, 20))
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(13)
        self.numwords_label.setFont(font)
        self.numwords_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        self.numwords_label.setObjectName("numwords_label")
        self.gridLayout.addWidget(self.numwords_label, 1, 4, 1, 1)
        self.word2_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word2_box.sizePolicy().hasHeightForWidth())
        self.word2_box.setSizePolicy(sizePolicy)
        self.word2_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word2_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word2_box.setObjectName("word2_box")
        self.gridLayout.addWidget(self.word2_box, 4, 4, 1, 1)
        self.word5_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word5_box.sizePolicy().hasHeightForWidth())
        self.word5_box.setSizePolicy(sizePolicy)
        self.word5_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word5_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word5_box.setObjectName("word5_box")
        self.gridLayout.addWidget(self.word5_box, 7, 4, 1, 1)
        self.bip39pass_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(
            self.bip39pass_box.sizePolicy().hasHeightForWidth()
        )
        self.bip39pass_box.setSizePolicy(sizePolicy)
        self.bip39pass_box.setMinimumSize(QtCore.QSize(20, 35))
        self.bip39pass_box.setStyleSheet(
            "QLineEdit#bip39pass_box{\n" "color: red\n" "}"
        )
        self.bip39pass_box.setProperty("bip39_passphrase", "")
        self.bip39pass_box.setObjectName("bip39pass_box")
        self.gridLayout.addWidget(self.bip39pass_box, 16, 4, 1, 2)
        self.word13_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word13_box.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word13_box.sizePolicy().hasHeightForWidth())
        self.word13_box.setSizePolicy(sizePolicy)
        self.word13_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word13_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word13_box.setObjectName("word13_box")
        self.gridLayout.addWidget(self.word13_box, 3, 5, 1, 1)
        self.numaddresses_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(13)
        self.numaddresses_label.setFont(font)
        self.numaddresses_label.setObjectName("numaddresses_label")
        self.gridLayout.addWidget(self.numaddresses_label, 19, 6, 1, 1)
        self.multisig_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.multisig_checkbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.multisig_checkbox.setObjectName("multisig_checkbox")
        self.gridLayout.addWidget(self.multisig_checkbox, 19, 7, 1, 1)
        self.word21_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word21_box.sizePolicy().hasHeightForWidth())
        self.word21_box.setSizePolicy(sizePolicy)
        self.word21_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word21_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word21_box.setObjectName("word21_box")
        self.gridLayout.addWidget(self.word21_box, 11, 5, 1, 1)
        self.derivationpath_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.derivationpath_box.sizePolicy().hasHeightForWidth()
        )
        self.derivationpath_box.setSizePolicy(sizePolicy)
        self.derivationpath_box.setMinimumSize(QtCore.QSize(0, 35))
        self.derivationpath_box.setMaximumSize(QtCore.QSize(500, 16777215))
        self.derivationpath_box.setProperty("path_input", "")
        self.derivationpath_box.setObjectName("derivationpath_box")
        self.gridLayout.addWidget(self.derivationpath_box, 19, 4, 1, 1)
        self.word20_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word20_box.sizePolicy().hasHeightForWidth())
        self.word20_box.setSizePolicy(sizePolicy)
        self.word20_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word20_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word20_box.setObjectName("word20_box")
        self.gridLayout.addWidget(self.word20_box, 10, 5, 1, 1)
        self.word11_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word11_box.sizePolicy().hasHeightForWidth())
        self.word11_box.setSizePolicy(sizePolicy)
        self.word11_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word11_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word11_box.setObjectName("word11_box")
        self.gridLayout.addWidget(self.word11_box, 13, 4, 1, 1)
        self.bip39_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(13)
        self.bip39_checkbox.setFont(font)
        self.bip39_checkbox.setProperty("passphrase_option", False)
        self.bip39_checkbox.setObjectName("bip39_checkbox")
        self.gridLayout.addWidget(self.bip39_checkbox, 15, 5, 1, 1)
        self.word4_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word4_box.sizePolicy().hasHeightForWidth())
        self.word4_box.setSizePolicy(sizePolicy)
        self.word4_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word4_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word4_box.setObjectName("word4_box")
        self.gridLayout.addWidget(self.word4_box, 6, 4, 1, 1)
        self.word22_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word22_box.sizePolicy().hasHeightForWidth())
        self.word22_box.setSizePolicy(sizePolicy)
        self.word22_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word22_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word22_box.setObjectName("word22_box")
        self.gridLayout.addWidget(self.word22_box, 12, 5, 1, 1)
        self.word19_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word19_box.sizePolicy().hasHeightForWidth())
        self.word19_box.setSizePolicy(sizePolicy)
        self.word19_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word19_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word19_box.setObjectName("word19_box")
        self.gridLayout.addWidget(self.word19_box, 9, 5, 1, 1)
        self.word14_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word14_box.sizePolicy().hasHeightForWidth())
        self.word14_box.setSizePolicy(sizePolicy)
        self.word14_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word14_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word14_box.setObjectName("word14_box")
        self.gridLayout.addWidget(self.word14_box, 4, 5, 1, 1)
        self.word15_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word15_box.sizePolicy().hasHeightForWidth())
        self.word15_box.setSizePolicy(sizePolicy)
        self.word15_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word15_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word15_box.setObjectName("word15_box")
        self.gridLayout.addWidget(self.word15_box, 5, 5, 1, 1)
        self.word7_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word7_box.sizePolicy().hasHeightForWidth())
        self.word7_box.setSizePolicy(sizePolicy)
        self.word7_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word7_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word7_box.setObjectName("word7_box")
        self.gridLayout.addWidget(self.word7_box, 9, 4, 1, 1)
        self.word16_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word16_box.sizePolicy().hasHeightForWidth())
        self.word16_box.setSizePolicy(sizePolicy)
        self.word16_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word16_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word16_box.setObjectName("word16_box")
        self.gridLayout.addWidget(self.word16_box, 6, 5, 1, 1)
        self.word6_box = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word6_box.sizePolicy().hasHeightForWidth())
        self.word6_box.setSizePolicy(sizePolicy)
        self.word6_box.setMinimumSize(QtCore.QSize(250, 35))
        self.word6_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.word6_box.setObjectName("word6_box")
        self.gridLayout.addWidget(self.word6_box, 8, 4, 1, 1)
        self.title_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.gridLayout.addWidget(self.title_label, 2, 5, 1, 2)
        self.icon = QtWidgets.QLabel(self.gridLayoutWidget)
        self.icon.setMinimumSize(QtCore.QSize(60, 60))
        self.icon.setMaximumSize(QtCore.QSize(60, 60))
        self.icon.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.icon.setAutoFillBackground(False)
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap(":/images/keycode.png"))
        self.icon.setScaledContents(True)
        self.icon.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.icon.setObjectName("icon")
        self.gridLayout.addWidget(self.icon, 2, 7, 1, 1)
        self.output_textbrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.output_textbrowser.setMinimumSize(QtCore.QSize(0, 600))
        self.output_textbrowser.setObjectName("output_textbrowser")
        self.gridLayout.addWidget(self.output_textbrowser, 3, 6, 15, 2)
        self.numaddress_spinbox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.numaddress_spinbox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.numaddress_spinbox.setMinimum(1)
        self.numaddress_spinbox.setProperty("total_addresses_str", "")
        self.numaddress_spinbox.setObjectName("numaddress_spinbox")
        self.gridLayout.addWidget(self.numaddress_spinbox, 20, 6, 1, 1)
        self.decode_xprv_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(13)
        self.decode_xprv_label.setFont(font)  # Use the same font as other labels
        self.decode_xprv_label.setObjectName("decode_xprv_label")
        self.gridLayout.addWidget(self.decode_xprv_label, 21, 4, 1, 1)

        # Adjust the position of the cancel and ok buttons
        self.gridLayout.addWidget(self.okbutton_box, 21, 7, 1, 1)

        # Set the scroll area widget
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # Create a layout for the main window
        self.mainLayout = QVBoxLayout(Bip39Tool)
        self.mainLayout.addWidget(self.scrollArea)

        self.address_combobox.activated.connect(
            lambda data: address_combo_func(data, self)
        )
        self.numwords_combobox.currentIndexChanged.connect(
            lambda data: num_words_func(data, self)
        )
        self.okbutton_box.clicked.connect(self.map_ok_button_box)
        self.bip39_checkbox.stateChanged.connect(
            lambda checked: self.bip39pass_box.setEnabled(checked)
        )
        self.numwords_combobox.addItems(["0", "1", "2", "3", "4", "5", "6", "7"])
        self.address_combobox.addItems(["0", "1", "2", "3", "4", "5", "6", "7", "8"])

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
        Bip39Tool.setTabOrder(self.bip39_checkbox, self.testnet_checkbox)
        Bip39Tool.setTabOrder(self.testnet_checkbox, self.output_textbrowser)

    def retranslateUi(self, Bip39Tool):
        _translate = QtCore.QCoreApplication.translate
        Bip39Tool.setWindowTitle(_translate("Bip39Tool", "Bip 39 Tool"))
        self.word1_box.setPlaceholderText(
            _translate("Bip39Tool", "Word1 / Multisig Pubkey 1")
        )
        self.word12_box.setPlaceholderText(
            _translate("Bip39Tool", "Word12 / Multisig Pubkey 12")
        )
        self.textfile_CheckBox.setText(_translate("Bip39Tool", "Output to Textfile"))
        self.derivationpath_label.setText(_translate("Bip39Tool", "Derivation Path"))
        self.address_combobox.setItemText(0, _translate("Bip39Tool", "P2PKH"))
        self.address_combobox.setItemText(1, _translate("Bip39Tool", "P2SH"))
        self.address_combobox.setItemText(2, _translate("Bip39Tool", "P2WPKH-P2SH"))
        self.address_combobox.setItemText(3, _translate("Bip39Tool", "P2WPKH"))
        self.address_combobox.setItemText(4, _translate("Bip39Tool", "P2WSH"))
        self.address_combobox.setItemText(5, _translate("Bip39Tool", "BIP44"))
        self.address_combobox.setItemText(6, _translate("Bip39Tool", "BIP49"))
        self.address_combobox.setItemText(7, _translate("Bip39Tool", "BIP84"))
        self.address_combobox.setItemText(8, _translate("Bip39Tool", "BIP141"))

        self.word8_box.setPlaceholderText(
            _translate("Bip39Tool", "Word8 / Multisig Pubkey 8")
        )
        self.numwords_combobox.setItemText(0, _translate("Bip39Tool", "3"))
        self.numwords_combobox.setItemText(1, _translate("Bip39Tool", "6"))
        self.numwords_combobox.setItemText(2, _translate("Bip39Tool", "9"))
        self.numwords_combobox.setItemText(3, _translate("Bip39Tool", "12"))
        self.numwords_combobox.setItemText(4, _translate("Bip39Tool", "15"))
        self.numwords_combobox.setItemText(5, _translate("Bip39Tool", "18"))
        self.numwords_combobox.setItemText(6, _translate("Bip39Tool", "21"))
        self.numwords_combobox.setItemText(7, _translate("Bip39Tool", "24"))
        self.word3_box.setPlaceholderText(
            _translate("Bip39Tool", "Word3 / Multisig Pubkey 3")
        )
        self.bip39pass_label.setText(_translate("Bip39Tool", "BIP39 Password"))
        self.word18_box.setPlaceholderText(_translate("Bip39Tool", "Word18"))
        self.hardened_checkbox.setText(_translate("Bip39Tool", "Hardened Addresses"))
        self.word17_box.setPlaceholderText(_translate("Bip39Tool", "Word17"))
        self.word23_box.setPlaceholderText(_translate("Bip39Tool", "Word23"))
        self.word24_box.setPlaceholderText(_translate("Bip39Tool", "Word24"))
        self.testnet_checkbox.setText(_translate("Bip39Tool", "Testnet"))
        self.word10_box.setPlaceholderText(
            _translate("Bip39Tool", "Word10 / Multisig Pubkey 10")
        )
        self.word9_box.setPlaceholderText(
            _translate("Bip39Tool", "Word9 / Multisig Pubkey 9")
        )
        self.numwords_label.setText(
            _translate("Bip39Tool", "Number of Words / Pubkeys")
        )
        self.word2_box.setPlaceholderText(
            _translate("Bip39Tool", "Word2 / Multisig Pubkey 2")
        )
        self.word5_box.setPlaceholderText(
            _translate("Bip39Tool", "Word5 / Multisig Pubkey 5")
        )
        self.word13_box.setPlaceholderText(
            _translate("Bip39Tool", "Word13 / Multisig Pubkey 13")
        )
        self.numaddresses_label.setText(
            _translate("Bip39Tool", "Number of Addresses/M-sig sigs Required")
        )
        self.multisig_checkbox.setText(
            _translate("Bip39Tool", "Create Multisig Address")
        )
        self.word21_box.setPlaceholderText(_translate("Bip39Tool", "Word21"))
        self.derivationpath_box.setPlaceholderText(
            _translate("Bip39Tool", "m/0 etc...")
        )
        self.word20_box.setPlaceholderText(_translate("Bip39Tool", "Word20"))
        self.word11_box.setPlaceholderText(
            _translate("Bip39Tool", "Word11 / Multisig Pubkey 11")
        )
        self.bip39_checkbox.setText(_translate("Bip39Tool", "Use BIP39 Pass"))
        self.word4_box.setPlaceholderText(
            _translate("Bip39Tool", "Word4 / Multisig Pubkey 4")
        )
        self.word22_box.setPlaceholderText(_translate("Bip39Tool", "Word22"))
        self.word19_box.setPlaceholderText(_translate("Bip39Tool", "Word19"))
        self.word14_box.setPlaceholderText(
            _translate("Bip39Tool", "Word14 / Multisig Pubkey 14")
        )
        self.word15_box.setPlaceholderText(
            _translate("Bip39Tool", "Word15 / Multisig Pubkey 15")
        )
        self.word7_box.setPlaceholderText(
            _translate("Bip39Tool", "Word7 / Multisig Pubkey 7")
        )
        self.word16_box.setPlaceholderText(
            _translate("Bip39Tool", "Word16 / Multisig Pubkey 16")
        )
        self.word6_box.setPlaceholderText(
            _translate("Bip39Tool", "Word6 / Multisig Pubkey 6")
        )
        self.title_label.setText(_translate("Bip39Tool", "BIP39 Key Tool"))
        self.address_combobox.activated.connect(
            lambda data: address_combo_func(data, self)
        )
        self.numwords_combobox.currentIndexChanged.connect(
            lambda data: num_words_func(data, self)
        )
        self.okbutton_box.clicked.connect(self.map_ok_button_box)

    def map_ok_button_box(self, button):
        if (
            self.okbutton_box.buttonRole(button)
            == QtWidgets.QDialogButtonBox.AcceptRole
        ):
            seed_button(self, True)
        elif (
            self.okbutton_box.buttonRole(button)
            == QtWidgets.QDialogButtonBox.RejectRole
        ):
            seed_button(self, False)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("app_icon.png"))
    Bip39Tool = QtWidgets.QDialog()
    ui = Ui_Bip39Tool()
    ui.setupUi(Bip39Tool)
    Bip39Tool.show()
    sys.exit(app.exec_())

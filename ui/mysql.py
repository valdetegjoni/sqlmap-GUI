# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mysql_new.ui'
#
# Created: Tue Oct 11 21:57:41 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FormMysql(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(899, 656)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(130, 0, 441, 51))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ostake_checkBox = QtGui.QCheckBox(self.groupBox)
        self.ostake_checkBox.setAutoExclusive(True)
        self.ostake_checkBox.setObjectName(_fromUtf8("ostake_checkBox"))
        self.gridLayout.addWidget(self.ostake_checkBox, 0, 2, 1, 1)
        self.fsa_checkBox = QtGui.QCheckBox(self.groupBox)
        self.fsa_checkBox.setAutoExclusive(True)
        self.fsa_checkBox.setObjectName(_fromUtf8("fsa_checkBox"))
        self.gridLayout.addWidget(self.fsa_checkBox, 0, 1, 1, 1)
        self.enum_checkBox = QtGui.QCheckBox(self.groupBox)
        self.enum_checkBox.setAutoExclusive(True)
        self.enum_checkBox.setObjectName(_fromUtf8("enum_checkBox"))
        self.gridLayout.addWidget(self.enum_checkBox, 0, 0, 1, 1)
        self.udfi_checkBox = QtGui.QCheckBox(self.groupBox)
        self.udfi_checkBox.setAutoExclusive(True)
        self.udfi_checkBox.setObjectName(_fromUtf8("udfi_checkBox"))
        self.gridLayout.addWidget(self.udfi_checkBox, 0, 3, 1, 1)
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(10, 60, 755, 125)) #10, 60, 755, 125
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 789, 159))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "", None))
        self.ostake_checkBox.setText(_translate("Form", "OSTakeover", None))
        self.fsa_checkBox.setText(_translate("Form", "File System Access", None))
        self.enum_checkBox.setText(_translate("Form", "Enumeration", None))
        self.udfi_checkBox.setText(_translate("Form", "UDFI", None))


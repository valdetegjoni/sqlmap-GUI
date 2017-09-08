# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mssqlserver.ui'
#
# Created: Tue Oct 11 22:10:53 2016
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

class Ui_FormMssqlserver(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(899, 656)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(185, 0, 360, 51)) #10, 0, 791, 200 
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mssql_enum_checkBox = QtGui.QCheckBox(self.groupBox)
        self.mssql_enum_checkBox.setAutoExclusive(True)
        self.mssql_enum_checkBox.setObjectName(_fromUtf8("mssql_enum_checkBox"))
        self.gridLayout.addWidget(self.mssql_enum_checkBox, 0, 0, 1, 1)
        self.mssql_fsa_checkBox = QtGui.QCheckBox(self.groupBox)
        self.mssql_fsa_checkBox.setAutoExclusive(True)
        self.mssql_fsa_checkBox.setObjectName(_fromUtf8("mssql_fsa_checkBox"))
        self.gridLayout.addWidget(self.mssql_fsa_checkBox, 0, 1, 1, 1)
        self.mssql_ostake_checkBox = QtGui.QCheckBox(self.groupBox)
        self.mssql_ostake_checkBox.setAutoExclusive(True)
        self.mssql_ostake_checkBox.setObjectName(_fromUtf8("mssql_ostake_checkBox"))
        self.gridLayout.addWidget(self.mssql_ostake_checkBox, 0, 2, 1, 1)
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(10, 60, 755, 125)) #10, 0, 785, 185
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 755, 130))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "", None))
        self.mssql_enum_checkBox.setText(_translate("Form", "Enumeration", None))
        self.mssql_fsa_checkBox.setText(_translate("Form", "File System Access", None))
        self.mssql_ostake_checkBox.setText(_translate("Form", "OSTakeover", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mssqlfing.ui'
#
# Created: Mon Oct 10 15:02:36 2016
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

class Ui_FormMssFing(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(899, 656)
        self.groupBox_13 = QtGui.QGroupBox(Form)
        self.groupBox_13.setGeometry(QtCore.QRect(10, 10, 751, 80))
        self.groupBox_13.setTitle(_fromUtf8(""))
        self.groupBox_13.setObjectName(_fromUtf8("groupBox_13"))
        self.mssql_fingerprint_checkBox = QtGui.QCheckBox(self.groupBox_13)
        self.mssql_fingerprint_checkBox.setGeometry(QtCore.QRect(10, 30, 281, 17))
        self.mssql_fingerprint_checkBox.setObjectName(_fromUtf8("mssql_fingerprint_checkBox"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.mssql_fingerprint_checkBox.setText(_translate("Form", "Extensive database management system fingerprint", None))


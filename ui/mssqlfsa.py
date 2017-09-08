# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mssqlfsa.ui'
#
# Created: Mon Oct 10 15:01:59 2016
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

class Ui_FormMssFsa(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(899, 656)
        self.groupBox_12 = QtGui.QGroupBox(Form)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 10, 751, 111))
        self.groupBox_12.setTitle(_fromUtf8(""))
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.mssql_fsa_write_radioButton = QtGui.QRadioButton(self.groupBox_12)
        self.mssql_fsa_write_radioButton.setGeometry(QtCore.QRect(10, 20, 261, 17))
        self.mssql_fsa_write_radioButton.setObjectName(_fromUtf8("mssql_fsa_write_radioButton"))
        self.mssql_fsa_write_lineEdit = QtGui.QLineEdit(self.groupBox_12)
        self.mssql_fsa_write_lineEdit.setGeometry(QtCore.QRect(280, 20, 431, 20))
        self.mssql_fsa_write_lineEdit.setObjectName(_fromUtf8("mssql_fsa_write_lineEdit"))
        self.mssql_fsa_write_filepath_lineEdit = QtGui.QLineEdit(self.groupBox_12)
        self.mssql_fsa_write_filepath_lineEdit.setGeometry(QtCore.QRect(280, 50, 431, 20))
        self.mssql_fsa_write_filepath_lineEdit.setObjectName(_fromUtf8("mssql_fsa_write_filepath_lineEdit"))
        self.label_10 = QtGui.QLabel(self.groupBox_12)
        self.label_10.setGeometry(QtCore.QRect(20, 50, 221, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.mssql_fsa_read_radioButton = QtGui.QRadioButton(self.groupBox_12)
        self.mssql_fsa_read_radioButton.setGeometry(QtCore.QRect(10, 80, 251, 17))
        self.mssql_fsa_read_radioButton.setObjectName(_fromUtf8("mssql_fsa_read_radioButton"))
        self.mssql_fsa_read_lineEdit = QtGui.QLineEdit(self.groupBox_12)
        self.mssql_fsa_read_lineEdit.setGeometry(QtCore.QRect(280, 80, 431, 20))
        self.mssql_fsa_read_lineEdit.setObjectName(_fromUtf8("mssql_fsa_read_lineEdit"))
        self.mssql_fsa_write_file_toolButton = QtGui.QToolButton(self.groupBox_12)
        self.mssql_fsa_write_file_toolButton.setGeometry(QtCore.QRect(720, 20, 25, 19))
        self.mssql_fsa_write_file_toolButton.setText(_fromUtf8(""))
        self.mssql_fsa_write_file_toolButton.setObjectName(_fromUtf8("mssql_fsa_write_file_toolButton"))
        self.mssql_fsa_write_path_toolButton = QtGui.QToolButton(self.groupBox_12)
        self.mssql_fsa_write_path_toolButton.setGeometry(QtCore.QRect(720, 50, 25, 19))
        self.mssql_fsa_write_path_toolButton.setText(_fromUtf8(""))
        self.mssql_fsa_write_path_toolButton.setObjectName(_fromUtf8("mssql_fsa_write_path_toolButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.mssql_fsa_write_radioButton.setText(_translate("Form", "Write a local file on the back-end DBMS file system", None))
        self.label_10.setText(_translate("Form", "Back-end DBMS absolute filepath to write to", None))
        self.mssql_fsa_read_radioButton.setText(_translate("Form", "Read a file from the back-end DBMS file system", None))


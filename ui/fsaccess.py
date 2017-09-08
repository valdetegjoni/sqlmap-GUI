# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fsaccess.ui'
#
# Created: Mon Oct 10 04:50:52 2016
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

class Ui_FormFSA(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(899, 656)
        self.groupBox_16 = QtGui.QGroupBox(Form)
        self.groupBox_16.setGeometry(QtCore.QRect(10, 10, 751, 101))
        self.groupBox_16.setTitle(_fromUtf8(""))
        self.groupBox_16.setObjectName(_fromUtf8("groupBox_16"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_16)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.fsa_write_radioButton = QtGui.QRadioButton(self.groupBox_16)
        self.fsa_write_radioButton.setObjectName(_fromUtf8("fsa_write_radioButton"))
        self.gridLayout_3.addWidget(self.fsa_write_radioButton, 0, 0, 1, 1)
        self.fsa_write_lineEdit = QtGui.QLineEdit(self.groupBox_16)
        self.fsa_write_lineEdit.setObjectName(_fromUtf8("fsa_write_lineEdit"))
        self.gridLayout_3.addWidget(self.fsa_write_lineEdit, 0, 1, 1, 1)
        self.fsa_write_file_toolButton = QtGui.QToolButton(self.groupBox_16)
        self.fsa_write_file_toolButton.setText(_fromUtf8(""))
        self.fsa_write_file_toolButton.setObjectName(_fromUtf8("fsa_write_file_toolButton"))
        self.gridLayout_3.addWidget(self.fsa_write_file_toolButton, 0, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_16)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)
        self.fsa_write_filepath_lineEdit = QtGui.QLineEdit(self.groupBox_16)
        self.fsa_write_filepath_lineEdit.setObjectName(_fromUtf8("fsa_write_filepath_lineEdit"))
        self.gridLayout_3.addWidget(self.fsa_write_filepath_lineEdit, 1, 1, 1, 1)
        self.fsa_write_path_toolButton = QtGui.QToolButton(self.groupBox_16)
        self.fsa_write_path_toolButton.setText(_fromUtf8(""))
        self.fsa_write_path_toolButton.setObjectName(_fromUtf8("fsa_write_path_toolButton"))
        self.gridLayout_3.addWidget(self.fsa_write_path_toolButton, 1, 2, 1, 1)
        self.fsa_read_radioButton = QtGui.QRadioButton(self.groupBox_16)
        self.fsa_read_radioButton.setObjectName(_fromUtf8("fsa_read_radioButton"))
        self.gridLayout_3.addWidget(self.fsa_read_radioButton, 2, 0, 1, 1)
        self.fsa_read_lineEdit = QtGui.QLineEdit(self.groupBox_16)
        self.fsa_read_lineEdit.setObjectName(_fromUtf8("fsa_read_lineEdit"))
        self.gridLayout_3.addWidget(self.fsa_read_lineEdit, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.fsa_write_radioButton.setText(_translate("Form", "Write a local file on the back-end DBMS file system", None))
        self.label_12.setText(_translate("Form", "Back-end DBMS absolute filepath to write to", None))
        self.fsa_read_radioButton.setText(_translate("Form", "Read a file from the back-end DBMS file system", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'udfi.ui'
#
# Created: Mon Oct 10 04:49:26 2016
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

class Ui_FormUDFI(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(899, 656)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 761, 111))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayoutWidget_38 = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget_38.setGeometry(QtCore.QRect(10, 10, 701, 80))
        self.gridLayoutWidget_38.setObjectName(_fromUtf8("gridLayoutWidget_38"))
        self.gridLayout_38 = QtGui.QGridLayout(self.gridLayoutWidget_38)
        self.gridLayout_38.setMargin(0)
        self.gridLayout_38.setObjectName(_fromUtf8("gridLayout_38"))
        self.label_13 = QtGui.QLabel(self.gridLayoutWidget_38)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_38.addWidget(self.label_13, 2, 0, 1, 1)
        self.udfi_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_38)
        self.udfi_lineEdit.setObjectName(_fromUtf8("udfi_lineEdit"))
        self.gridLayout_38.addWidget(self.udfi_lineEdit, 2, 1, 1, 1)
        self.udfi_toolButton = QtGui.QToolButton(self.gridLayoutWidget_38)
        self.udfi_toolButton.setObjectName(_fromUtf8("udfi_toolButton"))
        self.gridLayout_38.addWidget(self.udfi_toolButton, 2, 2, 1, 1)
        self.udfi_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_38)
        self.udfi_checkBox.setObjectName(_fromUtf8("udfi_checkBox"))
        self.gridLayout_38.addWidget(self.udfi_checkBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_13.setText(_translate("Form", "Local path of the shared library", None))
        self.udfi_toolButton.setText(_translate("Form", "Open", None))
        self.udfi_checkBox.setText(_translate("Form", "Inject custom user-defined functions", None))


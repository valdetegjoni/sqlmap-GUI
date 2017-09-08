# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'custominj.ui'
#
# Created: Tue Oct 11 18:15:46 2016
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

class Ui_FormCustom(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(899, 656)
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 711, 80))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_12 = QtGui.QGroupBox(self.gridLayoutWidget)
        self.groupBox_12.setTitle(_fromUtf8(""))
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_12)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.prefix_checkBox = QtGui.QCheckBox(self.groupBox_12)
        self.prefix_checkBox.setObjectName(_fromUtf8("prefix_checkBox"))
        self.gridLayout.addWidget(self.prefix_checkBox, 0, 0, 1, 1)
        self.prefix_lineEdit = QtGui.QLineEdit(self.groupBox_12)
        self.prefix_lineEdit.setObjectName(_fromUtf8("prefix_lineEdit"))
        self.gridLayout.addWidget(self.prefix_lineEdit, 0, 1, 1, 1)
        self.suffix_checkBox = QtGui.QCheckBox(self.groupBox_12)
        self.suffix_checkBox.setObjectName(_fromUtf8("suffix_checkBox"))
        self.gridLayout.addWidget(self.suffix_checkBox, 1, 0, 1, 1)
        self.suffix_lineEdit = QtGui.QLineEdit(self.groupBox_12)
        self.suffix_lineEdit.setObjectName(_fromUtf8("suffix_lineEdit"))
        self.gridLayout.addWidget(self.suffix_lineEdit, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_12, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.prefix_checkBox.setText(_translate("Form", "Injection payload prefix string", None))
        self.suffix_checkBox.setText(_translate("Form", "Injection payload suffix string", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ostakeover.ui'
#
# Created: Mon Oct 10 04:50:21 2016
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

class Ui_FormOSTakeover(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(899, 656)
        self.tabWidget_22 = QtGui.QTabWidget(Form)
        self.tabWidget_22.setGeometry(QtCore.QRect(0, 0, 751, 111))
        self.tabWidget_22.setObjectName(_fromUtf8("tabWidget_22"))
        self.tab_92 = QtGui.QWidget()
        self.tab_92.setObjectName(_fromUtf8("tab_92"))
        self.os_cmd_groupBox_4 = QtGui.QGroupBox(self.tab_92)
        self.os_cmd_groupBox_4.setGeometry(QtCore.QRect(10, 0, 701, 71))
        self.os_cmd_groupBox_4.setCheckable(False)
        self.os_cmd_groupBox_4.setChecked(False)
        self.os_cmd_groupBox_4.setObjectName(_fromUtf8("os_cmd_groupBox_4"))
        self.os_cmd_lineEdit = QtGui.QLineEdit(self.os_cmd_groupBox_4)
        self.os_cmd_lineEdit.setGeometry(QtCore.QRect(260, 20, 391, 20))
        self.os_cmd_lineEdit.setObjectName(_fromUtf8("os_cmd_lineEdit"))
        self.os_cmd_checkBox = QtGui.QCheckBox(self.os_cmd_groupBox_4)
        self.os_cmd_checkBox.setGeometry(QtCore.QRect(10, 20, 211, 20))
        self.os_cmd_checkBox.setObjectName(_fromUtf8("os_cmd_checkBox"))
        self.os_shell_checkBox = QtGui.QCheckBox(self.os_cmd_groupBox_4)
        self.os_shell_checkBox.setGeometry(QtCore.QRect(10, 40, 251, 20))
        self.os_shell_checkBox.setObjectName(_fromUtf8("os_shell_checkBox"))
        self.tabWidget_22.addTab(self.tab_92, _fromUtf8(""))
        self.tab_93 = QtGui.QWidget()
        self.tab_93.setObjectName(_fromUtf8("tab_93"))
        self.meterpreter_groupBox_4 = QtGui.QGroupBox(self.tab_93)
        self.meterpreter_groupBox_4.setGeometry(QtCore.QRect(10, 0, 731, 71))
        self.meterpreter_groupBox_4.setCheckable(False)
        self.meterpreter_groupBox_4.setChecked(False)
        self.meterpreter_groupBox_4.setObjectName(_fromUtf8("meterpreter_groupBox_4"))
        self.gridLayoutWidget_39 = QtGui.QWidget(self.meterpreter_groupBox_4)
        self.gridLayoutWidget_39.setGeometry(QtCore.QRect(10, 20, 711, 48))
        self.gridLayoutWidget_39.setObjectName(_fromUtf8("gridLayoutWidget_39"))
        self.gridLayout_39 = QtGui.QGridLayout(self.gridLayoutWidget_39)
        self.gridLayout_39.setMargin(0)
        self.gridLayout_39.setObjectName(_fromUtf8("gridLayout_39"))
        self.msf_path_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_39)
        self.msf_path_checkBox.setObjectName(_fromUtf8("msf_path_checkBox"))
        self.gridLayout_39.addWidget(self.msf_path_checkBox, 1, 0, 1, 1)
        self.msf_path_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_39)
        self.msf_path_lineEdit.setObjectName(_fromUtf8("msf_path_lineEdit"))
        self.gridLayout_39.addWidget(self.msf_path_lineEdit, 1, 1, 1, 1)
        self.os_pwn_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_39)
        self.os_pwn_checkBox.setObjectName(_fromUtf8("os_pwn_checkBox"))
        self.gridLayout_39.addWidget(self.os_pwn_checkBox, 0, 0, 1, 1)
        self.tabWidget_22.addTab(self.tab_93, _fromUtf8(""))
        self.tab_94 = QtGui.QWidget()
        self.tab_94.setObjectName(_fromUtf8("tab_94"))
        self.gridLayoutWidget_40 = QtGui.QWidget(self.tab_94)
        self.gridLayoutWidget_40.setGeometry(QtCore.QRect(10, 10, 731, 71))
        self.gridLayoutWidget_40.setObjectName(_fromUtf8("gridLayoutWidget_40"))
        self.gridLayout_40 = QtGui.QGridLayout(self.gridLayoutWidget_40)
        self.gridLayout_40.setMargin(0)
        self.gridLayout_40.setObjectName(_fromUtf8("gridLayout_40"))
        self.reg_value_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_40)
        self.reg_value_checkBox.setObjectName(_fromUtf8("reg_value_checkBox"))
        self.gridLayout_40.addWidget(self.reg_value_checkBox, 1, 2, 1, 1)
        self.reg_type_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_40)
        self.reg_type_lineEdit.setObjectName(_fromUtf8("reg_type_lineEdit"))
        self.gridLayout_40.addWidget(self.reg_type_lineEdit, 2, 3, 1, 1)
        self.reg_key_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_40)
        self.reg_key_checkBox.setObjectName(_fromUtf8("reg_key_checkBox"))
        self.gridLayout_40.addWidget(self.reg_key_checkBox, 1, 0, 1, 1)
        self.reg_data_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_40)
        self.reg_data_checkBox.setObjectName(_fromUtf8("reg_data_checkBox"))
        self.gridLayout_40.addWidget(self.reg_data_checkBox, 2, 0, 1, 1)
        self.reg_key_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_40)
        self.reg_key_lineEdit.setObjectName(_fromUtf8("reg_key_lineEdit"))
        self.gridLayout_40.addWidget(self.reg_key_lineEdit, 1, 1, 1, 1)
        self.reg_value_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_40)
        self.reg_value_lineEdit.setObjectName(_fromUtf8("reg_value_lineEdit"))
        self.gridLayout_40.addWidget(self.reg_value_lineEdit, 1, 3, 1, 1)
        self.reg_data_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_40)
        self.reg_data_lineEdit.setObjectName(_fromUtf8("reg_data_lineEdit"))
        self.gridLayout_40.addWidget(self.reg_data_lineEdit, 2, 1, 1, 1)
        self.reg_type_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_40)
        self.reg_type_checkBox.setObjectName(_fromUtf8("reg_type_checkBox"))
        self.gridLayout_40.addWidget(self.reg_type_checkBox, 2, 2, 1, 1)
        self.reg_add_radioButton = QtGui.QRadioButton(self.gridLayoutWidget_40)
        self.reg_add_radioButton.setObjectName(_fromUtf8("reg_add_radioButton"))
        self.gridLayout_40.addWidget(self.reg_add_radioButton, 0, 0, 1, 1)
        self.reg_read_radioButton = QtGui.QRadioButton(self.gridLayoutWidget_40)
        self.reg_read_radioButton.setObjectName(_fromUtf8("reg_read_radioButton"))
        self.gridLayout_40.addWidget(self.reg_read_radioButton, 0, 1, 1, 1)
        self.reg_del_radioButton = QtGui.QRadioButton(self.gridLayoutWidget_40)
        self.reg_del_radioButton.setObjectName(_fromUtf8("reg_del_radioButton"))
        self.gridLayout_40.addWidget(self.reg_del_radioButton, 0, 2, 1, 1)
        self.tabWidget_22.addTab(self.tab_94, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget_22.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.os_cmd_groupBox_4.setTitle(_translate("Form", "run arbitrary commands on the database server\'s underlying operating system", None))
        self.os_cmd_checkBox.setText(_translate("Form", "Execute an operating system command", None))
        self.os_shell_checkBox.setText(_translate("Form", "Prompt  interactive operating system shell", None))
        self.tabWidget_22.setTabText(self.tabWidget_22.indexOf(self.tab_92), _translate("Form", "Run arbitrary operating system command", None))
        self.meterpreter_groupBox_4.setTitle(_translate("Form", "Out-of-band stateful connection: Meterpreter", None))
        self.msf_path_checkBox.setText(_translate("Form", "Local path where Metasploit Framework is installed", None))
        self.os_pwn_checkBox.setText(_translate("Form", "Prompt for an OOB shell, Meterpreter or VNC", None))
        self.tabWidget_22.setTabText(self.tabWidget_22.indexOf(self.tab_93), _translate("Form", "Out-of-band stateful connection", None))
        self.reg_value_checkBox.setText(_translate("Form", "Windows registry key value", None))
        self.reg_key_checkBox.setText(_translate("Form", "Windows registry key path", None))
        self.reg_data_checkBox.setText(_translate("Form", "Windows registry key value data", None))
        self.reg_type_checkBox.setText(_translate("Form", "Windows registry key value type", None))
        self.reg_add_radioButton.setText(_translate("Form", "Write a  key value data", None))
        self.reg_read_radioButton.setText(_translate("Form", "Read a registry key value", None))
        self.reg_del_radioButton.setText(_translate("Form", "Delete a  registry key value", None))
        self.tabWidget_22.setTabText(self.tabWidget_22.indexOf(self.tab_94), _translate("Form", "Windows registry access", None))


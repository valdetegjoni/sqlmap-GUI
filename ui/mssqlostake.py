# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mssqlostake.ui'
#
# Created: Mon Oct 10 23:22:36 2016
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

class Ui_FormMssOSTake(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(899, 656)
        self.tabWidget_18 = QtGui.QTabWidget(Form)
        self.tabWidget_18.setGeometry(QtCore.QRect(0, 0, 771, 121))
        self.tabWidget_18.setObjectName(_fromUtf8("tabWidget_18"))
        self.tab_74 = QtGui.QWidget()
        self.tab_74.setObjectName(_fromUtf8("tab_74"))
        self.os_cmd_groupBox_2 = QtGui.QGroupBox(self.tab_74)
        self.os_cmd_groupBox_2.setGeometry(QtCore.QRect(10, 10, 711, 71))
        self.os_cmd_groupBox_2.setCheckable(False)
        self.os_cmd_groupBox_2.setChecked(False)
        self.os_cmd_groupBox_2.setObjectName(_fromUtf8("os_cmd_groupBox_2"))
        self.mssql_os_cmd_lineEdit = QtGui.QLineEdit(self.os_cmd_groupBox_2)
        self.mssql_os_cmd_lineEdit.setGeometry(QtCore.QRect(260, 20, 391, 20))
        self.mssql_os_cmd_lineEdit.setObjectName(_fromUtf8("mssql_os_cmd_lineEdit"))
        self.mssql_os_cmd_checkBox = QtGui.QCheckBox(self.os_cmd_groupBox_2)
        self.mssql_os_cmd_checkBox.setGeometry(QtCore.QRect(10, 20, 211, 20))
        self.mssql_os_cmd_checkBox.setObjectName(_fromUtf8("mssql_os_cmd_checkBox"))
        self.mssql_os_shell_checkBox = QtGui.QCheckBox(self.os_cmd_groupBox_2)
        self.mssql_os_shell_checkBox.setGeometry(QtCore.QRect(10, 40, 251, 20))
        self.mssql_os_shell_checkBox.setObjectName(_fromUtf8("mssql_os_shell_checkBox"))
        self.tabWidget_18.addTab(self.tab_74, _fromUtf8(""))
        self.tab_75 = QtGui.QWidget()
        self.tab_75.setObjectName(_fromUtf8("tab_75"))
        self.meterpreter_groupBox_2 = QtGui.QGroupBox(self.tab_75)
        self.meterpreter_groupBox_2.setGeometry(QtCore.QRect(10, 10, 741, 71))
        self.meterpreter_groupBox_2.setCheckable(False)
        self.meterpreter_groupBox_2.setChecked(False)
        self.meterpreter_groupBox_2.setObjectName(_fromUtf8("meterpreter_groupBox_2"))
        self.gridLayoutWidget_30 = QtGui.QWidget(self.meterpreter_groupBox_2)
        self.gridLayoutWidget_30.setGeometry(QtCore.QRect(10, 20, 711, 48))
        self.gridLayoutWidget_30.setObjectName(_fromUtf8("gridLayoutWidget_30"))
        self.gridLayout_30 = QtGui.QGridLayout(self.gridLayoutWidget_30)
        self.gridLayout_30.setMargin(0)
        self.gridLayout_30.setObjectName(_fromUtf8("gridLayout_30"))
        self.mssql_os_pwn_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_30)
        self.mssql_os_pwn_checkBox.setObjectName(_fromUtf8("mssql_os_pwn_checkBox"))
        self.gridLayout_30.addWidget(self.mssql_os_pwn_checkBox, 0, 0, 1, 1)
        self.mssql_msf_path_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_30)
        self.mssql_msf_path_lineEdit.setObjectName(_fromUtf8("mssql_msf_path_lineEdit"))
        self.gridLayout_30.addWidget(self.mssql_msf_path_lineEdit, 1, 1, 1, 1)
        self.mssql_msf_path_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_30)
        self.mssql_msf_path_checkBox.setObjectName(_fromUtf8("mssql_msf_path_checkBox"))
        self.gridLayout_30.addWidget(self.mssql_msf_path_checkBox, 1, 0, 1, 1)
        self.mssqlos_msf_toolButton = QtGui.QToolButton(self.gridLayoutWidget_30)
        self.mssqlos_msf_toolButton.setText(_fromUtf8(""))
        self.mssqlos_msf_toolButton.setObjectName(_fromUtf8("mssqlos_msf_toolButton"))
        self.gridLayout_30.addWidget(self.mssqlos_msf_toolButton, 1, 2, 1, 1)
        self.tabWidget_18.addTab(self.tab_75, _fromUtf8(""))
        self.tab_76 = QtGui.QWidget()
        self.tab_76.setObjectName(_fromUtf8("tab_76"))
        self.reg_groupBox_2 = QtGui.QGroupBox(self.tab_76)
        self.reg_groupBox_2.setGeometry(QtCore.QRect(0, 0, 831, 91))
        self.reg_groupBox_2.setCheckable(False)
        self.reg_groupBox_2.setChecked(False)
        self.reg_groupBox_2.setObjectName(_fromUtf8("reg_groupBox_2"))
        self.gridLayoutWidget_31 = QtGui.QWidget(self.reg_groupBox_2)
        self.gridLayoutWidget_31.setGeometry(QtCore.QRect(10, 40, 811, 48))
        self.gridLayoutWidget_31.setObjectName(_fromUtf8("gridLayoutWidget_31"))
        self.gridLayout_31 = QtGui.QGridLayout(self.gridLayoutWidget_31)
        self.gridLayout_31.setMargin(0)
        self.gridLayout_31.setObjectName(_fromUtf8("gridLayout_31"))
        self.mssql_reg_value_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_31)
        self.mssql_reg_value_checkBox.setObjectName(_fromUtf8("mssql_reg_value_checkBox"))
        self.gridLayout_31.addWidget(self.mssql_reg_value_checkBox, 0, 2, 1, 1)
        self.mssql_reg_type_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_31)
        self.mssql_reg_type_lineEdit.setObjectName(_fromUtf8("mssql_reg_type_lineEdit"))
        self.gridLayout_31.addWidget(self.mssql_reg_type_lineEdit, 1, 3, 1, 1)
        self.mssql_reg_value_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_31)
        self.mssql_reg_value_lineEdit.setObjectName(_fromUtf8("mssql_reg_value_lineEdit"))
        self.gridLayout_31.addWidget(self.mssql_reg_value_lineEdit, 0, 3, 1, 1)
        self.mssql_reg_key_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_31)
        self.mssql_reg_key_checkBox.setObjectName(_fromUtf8("mssql_reg_key_checkBox"))
        self.gridLayout_31.addWidget(self.mssql_reg_key_checkBox, 0, 0, 1, 1)
        self.mssql_reg_data_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_31)
        self.mssql_reg_data_checkBox.setObjectName(_fromUtf8("mssql_reg_data_checkBox"))
        self.gridLayout_31.addWidget(self.mssql_reg_data_checkBox, 1, 0, 1, 1)
        self.mssql_reg_key_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_31)
        self.mssql_reg_key_lineEdit.setObjectName(_fromUtf8("mssql_reg_key_lineEdit"))
        self.gridLayout_31.addWidget(self.mssql_reg_key_lineEdit, 0, 1, 1, 1)
        self.mssql_reg_data_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_31)
        self.mssql_reg_data_lineEdit.setObjectName(_fromUtf8("mssql_reg_data_lineEdit"))
        self.gridLayout_31.addWidget(self.mssql_reg_data_lineEdit, 1, 1, 1, 1)
        self.mssql_reg_type_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_31)
        self.mssql_reg_type_checkBox.setObjectName(_fromUtf8("mssql_reg_type_checkBox"))
        self.gridLayout_31.addWidget(self.mssql_reg_type_checkBox, 1, 2, 1, 1)
        self.mssql_reg_add_radioButton = QtGui.QRadioButton(self.reg_groupBox_2)
        self.mssql_reg_add_radioButton.setGeometry(QtCore.QRect(10, 20, 180, 17))
        self.mssql_reg_add_radioButton.setObjectName(_fromUtf8("mssql_reg_add_radioButton"))
        self.mssql_reg_read_radioButton = QtGui.QRadioButton(self.reg_groupBox_2)
        self.mssql_reg_read_radioButton.setGeometry(QtCore.QRect(250, 20, 216, 17))
        self.mssql_reg_read_radioButton.setObjectName(_fromUtf8("mssql_reg_read_radioButton"))
        self.mssql_reg_del_radioButton = QtGui.QRadioButton(self.reg_groupBox_2)
        self.mssql_reg_del_radioButton.setGeometry(QtCore.QRect(550, 20, 180, 17))
        self.mssql_reg_del_radioButton.setObjectName(_fromUtf8("mssql_reg_del_radioButton"))
        self.tabWidget_18.addTab(self.tab_76, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget_18.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.os_cmd_groupBox_2.setTitle(_translate("Form", "run arbitrary commands on the database server\'s underlying operating system", None))
        self.mssql_os_cmd_checkBox.setText(_translate("Form", "Execute an operating system command", None))
        self.mssql_os_shell_checkBox.setText(_translate("Form", "Prompt  interactive operating system shell", None))
        self.tabWidget_18.setTabText(self.tabWidget_18.indexOf(self.tab_74), _translate("Form", "Run arbitrary operating system command", None))
        self.meterpreter_groupBox_2.setTitle(_translate("Form", "Out-of-band stateful connection: Meterpreter", None))
        self.mssql_os_pwn_checkBox.setText(_translate("Form", "Prompt for an OOB shell, Meterpreter or VNC", None))
        self.mssql_msf_path_checkBox.setText(_translate("Form", "Local path where Metasploit Framework is installed", None))
        self.tabWidget_18.setTabText(self.tabWidget_18.indexOf(self.tab_75), _translate("Form", "Out-of-band stateful connection", None))
        self.reg_groupBox_2.setTitle(_translate("Form", "Windows registry access", None))
        self.mssql_reg_value_checkBox.setText(_translate("Form", "Windows registry key value", None))
        self.mssql_reg_key_checkBox.setText(_translate("Form", "Windows registry key path", None))
        self.mssql_reg_data_checkBox.setText(_translate("Form", "Windows registry key value data", None))
        self.mssql_reg_type_checkBox.setText(_translate("Form", "Windows registry key value type", None))
        self.mssql_reg_add_radioButton.setText(_translate("Form", "Write a  key value data", None))
        self.mssql_reg_read_radioButton.setText(_translate("Form", "Read a registry key value", None))
        self.mssql_reg_del_radioButton.setText(_translate("Form", "Delete a  registry key value", None))
        self.tabWidget_18.setTabText(self.tabWidget_18.indexOf(self.tab_76), _translate("Form", "Windows registry access", None))


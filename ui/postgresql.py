# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'postgresql.ui'
#
# Created: Mon Oct 10 04:06:42 2016
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

class Ui_FormPostgreSql(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(899, 656)
        self.tabWidget_19 = QtGui.QTabWidget(Form)
        self.tabWidget_19.setGeometry(QtCore.QRect(0, 0, 781, 151))
        self.tabWidget_19.setObjectName(_fromUtf8("tabWidget_19"))
        self.tab_78 = QtGui.QWidget()
        self.tab_78.setObjectName(_fromUtf8("tab_78"))
        self.tabWidget_20 = QtGui.QTabWidget(self.tab_78)
        self.tabWidget_20.setGeometry(QtCore.QRect(0, 0, 771, 121))
        self.tabWidget_20.setObjectName(_fromUtf8("tabWidget_20"))
        self.tab_79 = QtGui.QWidget()
        self.tab_79.setObjectName(_fromUtf8("tab_79"))
        self.gridLayoutWidget_33 = QtGui.QWidget(self.tab_79)
        self.gridLayoutWidget_33.setGeometry(QtCore.QRect(10, 10, 741, 61))
        self.gridLayoutWidget_33.setObjectName(_fromUtf8("gridLayoutWidget_33"))
        self.gridLayout_33 = QtGui.QGridLayout(self.gridLayoutWidget_33)
        self.gridLayout_33.setMargin(0)
        self.gridLayout_33.setObjectName(_fromUtf8("gridLayout_33"))
        self.psql_current_user_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_33)
        self.psql_current_user_checkBox.setObjectName(_fromUtf8("psql_current_user_checkBox"))
        self.gridLayout_33.addWidget(self.psql_current_user_checkBox, 0, 0, 1, 1)
        self.psql_passwords_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_33)
        self.psql_passwords_checkBox.setObjectName(_fromUtf8("psql_passwords_checkBox"))
        self.gridLayout_33.addWidget(self.psql_passwords_checkBox, 1, 0, 1, 1)
        self.psql_privileges_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_33)
        self.psql_privileges_checkBox.setObjectName(_fromUtf8("psql_privileges_checkBox"))
        self.gridLayout_33.addWidget(self.psql_privileges_checkBox, 1, 1, 1, 1)
        self.psql_roles_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_33)
        self.psql_roles_checkBox.setObjectName(_fromUtf8("psql_roles_checkBox"))
        self.gridLayout_33.addWidget(self.psql_roles_checkBox, 0, 1, 1, 1)
        self.psql_users_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_33)
        self.psql_users_checkBox.setObjectName(_fromUtf8("psql_users_checkBox"))
        self.gridLayout_33.addWidget(self.psql_users_checkBox, 0, 2, 1, 1)
        self.psql_is_dba_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_33)
        self.psql_is_dba_checkBox.setObjectName(_fromUtf8("psql_is_dba_checkBox"))
        self.gridLayout_33.addWidget(self.psql_is_dba_checkBox, 1, 2, 1, 1)
        self.tabWidget_20.addTab(self.tab_79, _fromUtf8(""))
        self.tab_80 = QtGui.QWidget()
        self.tab_80.setObjectName(_fromUtf8("tab_80"))
        self.gridLayoutWidget_34 = QtGui.QWidget(self.tab_80)
        self.gridLayoutWidget_34.setGeometry(QtCore.QRect(20, 10, 741, 61))
        self.gridLayoutWidget_34.setObjectName(_fromUtf8("gridLayoutWidget_34"))
        self.gridLayout_34 = QtGui.QGridLayout(self.gridLayoutWidget_34)
        self.gridLayout_34.setMargin(0)
        self.gridLayout_34.setObjectName(_fromUtf8("gridLayout_34"))
        self.psql_schema_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_34)
        self.psql_schema_checkBox.setObjectName(_fromUtf8("psql_schema_checkBox"))
        self.gridLayout_34.addWidget(self.psql_schema_checkBox, 0, 1, 1, 1)
        self.psql_columns_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_34)
        self.psql_columns_checkBox.setObjectName(_fromUtf8("psql_columns_checkBox"))
        self.gridLayout_34.addWidget(self.psql_columns_checkBox, 1, 0, 1, 1)
        self.psql_count_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_34)
        self.psql_count_checkBox.setObjectName(_fromUtf8("psql_count_checkBox"))
        self.gridLayout_34.addWidget(self.psql_count_checkBox, 0, 0, 1, 1)
        self.psql_dbs_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_34)
        self.psql_dbs_checkBox.setObjectName(_fromUtf8("psql_dbs_checkBox"))
        self.gridLayout_34.addWidget(self.psql_dbs_checkBox, 0, 2, 1, 1)
        self.psql_tables_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_34)
        self.psql_tables_checkBox.setObjectName(_fromUtf8("psql_tables_checkBox"))
        self.gridLayout_34.addWidget(self.psql_tables_checkBox, 1, 1, 1, 1)
        self.tabWidget_20.addTab(self.tab_80, _fromUtf8(""))
        self.tab_81 = QtGui.QWidget()
        self.tab_81.setObjectName(_fromUtf8("tab_81"))
        self.formLayoutWidget_21 = QtGui.QWidget(self.tab_81)
        self.formLayoutWidget_21.setGeometry(QtCore.QRect(10, 10, 222, 61))
        self.formLayoutWidget_21.setObjectName(_fromUtf8("formLayoutWidget_21"))
        self.formLayout_21 = QtGui.QFormLayout(self.formLayoutWidget_21)
        self.formLayout_21.setMargin(0)
        self.formLayout_21.setObjectName(_fromUtf8("formLayout_21"))
        self.psql_dump_all_checkBox = QtGui.QCheckBox(self.formLayoutWidget_21)
        self.psql_dump_all_checkBox.setObjectName(_fromUtf8("psql_dump_all_checkBox"))
        self.formLayout_21.setWidget(2, QtGui.QFormLayout.LabelRole, self.psql_dump_all_checkBox)
        self.psql_dump_checkBox = QtGui.QCheckBox(self.formLayoutWidget_21)
        self.psql_dump_checkBox.setObjectName(_fromUtf8("psql_dump_checkBox"))
        self.formLayout_21.setWidget(1, QtGui.QFormLayout.LabelRole, self.psql_dump_checkBox)
        self.tabWidget_20.addTab(self.tab_81, _fromUtf8(""))
        self.tab_82 = QtGui.QWidget()
        self.tab_82.setObjectName(_fromUtf8("tab_82"))
        self.psql_search_checkBox = QtGui.QCheckBox(self.tab_82)
        self.psql_search_checkBox.setGeometry(QtCore.QRect(20, 10, 274, 17))
        self.psql_search_checkBox.setObjectName(_fromUtf8("psql_search_checkBox"))
        self.gridLayoutWidget_35 = QtGui.QWidget(self.tab_82)
        self.gridLayoutWidget_35.setGeometry(QtCore.QRect(20, 30, 741, 51))
        self.gridLayoutWidget_35.setObjectName(_fromUtf8("gridLayoutWidget_35"))
        self.gridLayout_35 = QtGui.QGridLayout(self.gridLayoutWidget_35)
        self.gridLayout_35.setMargin(0)
        self.gridLayout_35.setObjectName(_fromUtf8("gridLayout_35"))
        self.psql_DB_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_35)
        self.psql_DB_lineEdit.setObjectName(_fromUtf8("psql_DB_lineEdit"))
        self.gridLayout_35.addWidget(self.psql_DB_lineEdit, 0, 1, 1, 1)
        self.psql_TBL_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_35)
        self.psql_TBL_checkBox.setObjectName(_fromUtf8("psql_TBL_checkBox"))
        self.gridLayout_35.addWidget(self.psql_TBL_checkBox, 1, 0, 1, 1)
        self.psql_TBL_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_35)
        self.psql_TBL_lineEdit.setObjectName(_fromUtf8("psql_TBL_lineEdit"))
        self.gridLayout_35.addWidget(self.psql_TBL_lineEdit, 1, 1, 1, 1)
        self.psql_DB_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_35)
        self.psql_DB_checkBox.setObjectName(_fromUtf8("psql_DB_checkBox"))
        self.gridLayout_35.addWidget(self.psql_DB_checkBox, 0, 0, 1, 1)
        self.psql_COL_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_35)
        self.psql_COL_checkBox.setObjectName(_fromUtf8("psql_COL_checkBox"))
        self.gridLayout_35.addWidget(self.psql_COL_checkBox, 1, 2, 1, 1)
        self.psql_COL_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_35)
        self.psql_COL_lineEdit.setObjectName(_fromUtf8("psql_COL_lineEdit"))
        self.gridLayout_35.addWidget(self.psql_COL_lineEdit, 1, 3, 1, 1)
        self.tabWidget_20.addTab(self.tab_82, _fromUtf8(""))
        self.tab_83 = QtGui.QWidget()
        self.tab_83.setObjectName(_fromUtf8("tab_83"))
        self.formLayoutWidget_22 = QtGui.QWidget(self.tab_83)
        self.formLayoutWidget_22.setGeometry(QtCore.QRect(10, 10, 191, 51))
        self.formLayoutWidget_22.setObjectName(_fromUtf8("formLayoutWidget_22"))
        self.formLayout_22 = QtGui.QFormLayout(self.formLayoutWidget_22)
        self.formLayout_22.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_22.setMargin(0)
        self.formLayout_22.setObjectName(_fromUtf8("formLayout_22"))
        self.psql_banner_checkBox = QtGui.QCheckBox(self.formLayoutWidget_22)
        self.psql_banner_checkBox.setObjectName(_fromUtf8("psql_banner_checkBox"))
        self.formLayout_22.setWidget(0, QtGui.QFormLayout.LabelRole, self.psql_banner_checkBox)
        self.tabWidget_20.addTab(self.tab_83, _fromUtf8(""))
        self.tab_96 = QtGui.QWidget()
        self.tab_96.setObjectName(_fromUtf8("tab_96"))
        self.groupBox_22 = QtGui.QGroupBox(self.tab_96)
        self.groupBox_22.setGeometry(QtCore.QRect(10, 10, 751, 81))
        self.groupBox_22.setTitle(_fromUtf8(""))
        self.groupBox_22.setObjectName(_fromUtf8("groupBox_22"))
        self.psql_sql_query_checkBox = QtGui.QCheckBox(self.groupBox_22)
        self.psql_sql_query_checkBox.setGeometry(QtCore.QRect(10, 10, 181, 17))
        self.psql_sql_query_checkBox.setObjectName(_fromUtf8("psql_sql_query_checkBox"))
        self.psql_sqlshell_checkBox = QtGui.QCheckBox(self.groupBox_22)
        self.psql_sqlshell_checkBox.setGeometry(QtCore.QRect(10, 30, 201, 17))
        self.psql_sqlshell_checkBox.setObjectName(_fromUtf8("psql_sqlshell_checkBox"))
        self.psql_sqlfile_checkBox = QtGui.QCheckBox(self.groupBox_22)
        self.psql_sqlfile_checkBox.setGeometry(QtCore.QRect(10, 50, 221, 17))
        self.psql_sqlfile_checkBox.setObjectName(_fromUtf8("psql_sqlfile_checkBox"))
        self.psql_sql_query_lineEdit = QtGui.QLineEdit(self.groupBox_22)
        self.psql_sql_query_lineEdit.setGeometry(QtCore.QRect(230, 10, 491, 20))
        self.psql_sql_query_lineEdit.setObjectName(_fromUtf8("psql_sql_query_lineEdit"))
        self.psql_sqlfile_lineEdit = QtGui.QLineEdit(self.groupBox_22)
        self.psql_sqlfile_lineEdit.setGeometry(QtCore.QRect(230, 50, 491, 20))
        self.psql_sqlfile_lineEdit.setObjectName(_fromUtf8("psql_sqlfile_lineEdit"))
        self.tabWidget_20.addTab(self.tab_96, _fromUtf8(""))
        self.tab_84 = QtGui.QWidget()
        self.tab_84.setObjectName(_fromUtf8("tab_84"))
        self.psql_brute_tables_checkBox = QtGui.QCheckBox(self.tab_84)
        self.psql_brute_tables_checkBox.setGeometry(QtCore.QRect(10, 10, 141, 20))
        self.psql_brute_tables_checkBox.setObjectName(_fromUtf8("psql_brute_tables_checkBox"))
        self.psql_brute_columns_checkBox = QtGui.QCheckBox(self.tab_84)
        self.psql_brute_columns_checkBox.setGeometry(QtCore.QRect(10, 40, 151, 17))
        self.psql_brute_columns_checkBox.setObjectName(_fromUtf8("psql_brute_columns_checkBox"))
        self.tabWidget_20.addTab(self.tab_84, _fromUtf8(""))
        self.tabWidget_19.addTab(self.tab_78, _fromUtf8(""))
        self.tab_85 = QtGui.QWidget()
        self.tab_85.setObjectName(_fromUtf8("tab_85"))
        self.groupBox_15 = QtGui.QGroupBox(self.tab_85)
        self.groupBox_15.setGeometry(QtCore.QRect(10, 10, 751, 111))
        self.groupBox_15.setTitle(_fromUtf8(""))
        self.groupBox_15.setObjectName(_fromUtf8("groupBox_15"))
        self.psql_fsa_write_radioButton = QtGui.QRadioButton(self.groupBox_15)
        self.psql_fsa_write_radioButton.setGeometry(QtCore.QRect(10, 20, 261, 17))
        self.psql_fsa_write_radioButton.setObjectName(_fromUtf8("psql_fsa_write_radioButton"))
        self.psql_fsa_write_lineEdit = QtGui.QLineEdit(self.groupBox_15)
        self.psql_fsa_write_lineEdit.setGeometry(QtCore.QRect(280, 20, 431, 20))
        self.psql_fsa_write_lineEdit.setObjectName(_fromUtf8("psql_fsa_write_lineEdit"))
        self.psql_fsa_write_filepath_lineEdit = QtGui.QLineEdit(self.groupBox_15)
        self.psql_fsa_write_filepath_lineEdit.setGeometry(QtCore.QRect(280, 50, 431, 20))
        self.psql_fsa_write_filepath_lineEdit.setObjectName(_fromUtf8("psql_fsa_write_filepath_lineEdit"))
        self.label_11 = QtGui.QLabel(self.groupBox_15)
        self.label_11.setGeometry(QtCore.QRect(20, 50, 221, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.psql_fsa_read_radioButton = QtGui.QRadioButton(self.groupBox_15)
        self.psql_fsa_read_radioButton.setGeometry(QtCore.QRect(10, 80, 251, 17))
        self.psql_fsa_read_radioButton.setObjectName(_fromUtf8("psql_fsa_read_radioButton"))
        self.psql_fsa_read_lineEdit = QtGui.QLineEdit(self.groupBox_15)
        self.psql_fsa_read_lineEdit.setGeometry(QtCore.QRect(280, 80, 431, 20))
        self.psql_fsa_read_lineEdit.setObjectName(_fromUtf8("psql_fsa_read_lineEdit"))
        self.psql_fsa_write_file_toolButton = QtGui.QToolButton(self.groupBox_15)
        self.psql_fsa_write_file_toolButton.setGeometry(QtCore.QRect(720, 20, 25, 19))
        self.psql_fsa_write_file_toolButton.setText(_fromUtf8(""))
        self.psql_fsa_write_file_toolButton.setObjectName(_fromUtf8("psql_fsa_write_file_toolButton"))
        self.psql_fsa_write_path_toolButton = QtGui.QToolButton(self.groupBox_15)
        self.psql_fsa_write_path_toolButton.setGeometry(QtCore.QRect(720, 50, 25, 19))
        self.psql_fsa_write_path_toolButton.setText(_fromUtf8(""))
        self.psql_fsa_write_path_toolButton.setObjectName(_fromUtf8("psql_fsa_write_path_toolButton"))
        self.tabWidget_19.addTab(self.tab_85, _fromUtf8(""))
        self.tab_86 = QtGui.QWidget()
        self.tab_86.setObjectName(_fromUtf8("tab_86"))
        self.groupBox_16 = QtGui.QGroupBox(self.tab_86)
        self.groupBox_16.setGeometry(QtCore.QRect(10, 10, 751, 80))
        self.groupBox_16.setTitle(_fromUtf8(""))
        self.groupBox_16.setObjectName(_fromUtf8("groupBox_16"))
        self.psql_fingerprint_checkBox = QtGui.QCheckBox(self.groupBox_16)
        self.psql_fingerprint_checkBox.setGeometry(QtCore.QRect(10, 30, 281, 17))
        self.psql_fingerprint_checkBox.setObjectName(_fromUtf8("psql_fingerprint_checkBox"))
        self.tabWidget_19.addTab(self.tab_86, _fromUtf8(""))
        self.tab_87 = QtGui.QWidget()
        self.tab_87.setObjectName(_fromUtf8("tab_87"))
        self.tabWidget_21 = QtGui.QTabWidget(self.tab_87)
        self.tabWidget_21.setGeometry(QtCore.QRect(0, 0, 771, 121))
        self.tabWidget_21.setObjectName(_fromUtf8("tabWidget_21"))
        self.tab_88 = QtGui.QWidget()
        self.tab_88.setObjectName(_fromUtf8("tab_88"))
        self.os_cmd_groupBox_3 = QtGui.QGroupBox(self.tab_88)
        self.os_cmd_groupBox_3.setGeometry(QtCore.QRect(10, 10, 711, 71))
        self.os_cmd_groupBox_3.setCheckable(False)
        self.os_cmd_groupBox_3.setChecked(False)
        self.os_cmd_groupBox_3.setObjectName(_fromUtf8("os_cmd_groupBox_3"))
        self.psql_os_cmd_lineEdit = QtGui.QLineEdit(self.os_cmd_groupBox_3)
        self.psql_os_cmd_lineEdit.setGeometry(QtCore.QRect(260, 20, 391, 20))
        self.psql_os_cmd_lineEdit.setObjectName(_fromUtf8("psql_os_cmd_lineEdit"))
        self.psql_os_cmd_checkBox = QtGui.QCheckBox(self.os_cmd_groupBox_3)
        self.psql_os_cmd_checkBox.setGeometry(QtCore.QRect(10, 20, 211, 20))
        self.psql_os_cmd_checkBox.setObjectName(_fromUtf8("psql_os_cmd_checkBox"))
        self.psql_os_shell_checkBox = QtGui.QCheckBox(self.os_cmd_groupBox_3)
        self.psql_os_shell_checkBox.setGeometry(QtCore.QRect(10, 40, 251, 20))
        self.psql_os_shell_checkBox.setObjectName(_fromUtf8("psql_os_shell_checkBox"))
        self.tabWidget_21.addTab(self.tab_88, _fromUtf8(""))
        self.tab_89 = QtGui.QWidget()
        self.tab_89.setObjectName(_fromUtf8("tab_89"))
        self.meterpreter_groupBox_3 = QtGui.QGroupBox(self.tab_89)
        self.meterpreter_groupBox_3.setGeometry(QtCore.QRect(10, 10, 741, 71))
        self.meterpreter_groupBox_3.setCheckable(False)
        self.meterpreter_groupBox_3.setChecked(False)
        self.meterpreter_groupBox_3.setObjectName(_fromUtf8("meterpreter_groupBox_3"))
        self.gridLayoutWidget_36 = QtGui.QWidget(self.meterpreter_groupBox_3)
        self.gridLayoutWidget_36.setGeometry(QtCore.QRect(10, 20, 711, 48))
        self.gridLayoutWidget_36.setObjectName(_fromUtf8("gridLayoutWidget_36"))
        self.gridLayout_36 = QtGui.QGridLayout(self.gridLayoutWidget_36)
        self.gridLayout_36.setMargin(0)
        self.gridLayout_36.setObjectName(_fromUtf8("gridLayout_36"))
        self.psql_msf_path_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_36)
        self.psql_msf_path_checkBox.setObjectName(_fromUtf8("psql_msf_path_checkBox"))
        self.gridLayout_36.addWidget(self.psql_msf_path_checkBox, 1, 0, 1, 1)
        self.psql_msf_path_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_36)
        self.psql_msf_path_lineEdit.setObjectName(_fromUtf8("psql_msf_path_lineEdit"))
        self.gridLayout_36.addWidget(self.psql_msf_path_lineEdit, 1, 1, 1, 1)
        self.psql_os_pwn_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_36)
        self.psql_os_pwn_checkBox.setObjectName(_fromUtf8("psql_os_pwn_checkBox"))
        self.gridLayout_36.addWidget(self.psql_os_pwn_checkBox, 0, 0, 1, 1)
        self.tabWidget_21.addTab(self.tab_89, _fromUtf8(""))
        self.tab_90 = QtGui.QWidget()
        self.tab_90.setObjectName(_fromUtf8("tab_90"))
        self.reg_groupBox_3 = QtGui.QGroupBox(self.tab_90)
        self.reg_groupBox_3.setGeometry(QtCore.QRect(0, 0, 831, 91))
        self.reg_groupBox_3.setCheckable(False)
        self.reg_groupBox_3.setChecked(False)
        self.reg_groupBox_3.setObjectName(_fromUtf8("reg_groupBox_3"))
        self.gridLayoutWidget_37 = QtGui.QWidget(self.reg_groupBox_3)
        self.gridLayoutWidget_37.setGeometry(QtCore.QRect(10, 40, 811, 48))
        self.gridLayoutWidget_37.setObjectName(_fromUtf8("gridLayoutWidget_37"))
        self.gridLayout_37 = QtGui.QGridLayout(self.gridLayoutWidget_37)
        self.gridLayout_37.setMargin(0)
        self.gridLayout_37.setObjectName(_fromUtf8("gridLayout_37"))
        self.psql_reg_value_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_37)
        self.psql_reg_value_checkBox.setObjectName(_fromUtf8("psql_reg_value_checkBox"))
        self.gridLayout_37.addWidget(self.psql_reg_value_checkBox, 0, 2, 1, 1)
        self.psql_reg_type_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_37)
        self.psql_reg_type_lineEdit.setObjectName(_fromUtf8("psql_reg_type_lineEdit"))
        self.gridLayout_37.addWidget(self.psql_reg_type_lineEdit, 1, 3, 1, 1)
        self.psql_reg_value_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_37)
        self.psql_reg_value_lineEdit.setObjectName(_fromUtf8("psql_reg_value_lineEdit"))
        self.gridLayout_37.addWidget(self.psql_reg_value_lineEdit, 0, 3, 1, 1)
        self.psql_reg_key_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_37)
        self.psql_reg_key_checkBox.setObjectName(_fromUtf8("psql_reg_key_checkBox"))
        self.gridLayout_37.addWidget(self.psql_reg_key_checkBox, 0, 0, 1, 1)
        self.psql_reg_data_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_37)
        self.psql_reg_data_checkBox.setObjectName(_fromUtf8("psql_reg_data_checkBox"))
        self.gridLayout_37.addWidget(self.psql_reg_data_checkBox, 1, 0, 1, 1)
        self.psql_reg_key_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_37)
        self.psql_reg_key_lineEdit.setObjectName(_fromUtf8("psql_reg_key_lineEdit"))
        self.gridLayout_37.addWidget(self.psql_reg_key_lineEdit, 0, 1, 1, 1)
        self.psql_reg_data_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_37)
        self.psql_reg_data_lineEdit.setObjectName(_fromUtf8("psql_reg_data_lineEdit"))
        self.gridLayout_37.addWidget(self.psql_reg_data_lineEdit, 1, 1, 1, 1)
        self.psql_reg_type_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_37)
        self.psql_reg_type_checkBox.setObjectName(_fromUtf8("psql_reg_type_checkBox"))
        self.gridLayout_37.addWidget(self.psql_reg_type_checkBox, 1, 2, 1, 1)
        self.psql_reg_add_radioButton = QtGui.QRadioButton(self.reg_groupBox_3)
        self.psql_reg_add_radioButton.setGeometry(QtCore.QRect(10, 20, 180, 17))
        self.psql_reg_add_radioButton.setObjectName(_fromUtf8("psql_reg_add_radioButton"))
        self.psql_reg_read_radioButton = QtGui.QRadioButton(self.reg_groupBox_3)
        self.psql_reg_read_radioButton.setGeometry(QtCore.QRect(250, 20, 216, 17))
        self.psql_reg_read_radioButton.setObjectName(_fromUtf8("psql_reg_read_radioButton"))
        self.psql_reg_del_radioButton = QtGui.QRadioButton(self.reg_groupBox_3)
        self.psql_reg_del_radioButton.setGeometry(QtCore.QRect(550, 20, 180, 17))
        self.psql_reg_del_radioButton.setObjectName(_fromUtf8("psql_reg_del_radioButton"))
        self.tabWidget_21.addTab(self.tab_90, _fromUtf8(""))
        self.tabWidget_19.addTab(self.tab_87, _fromUtf8(""))
        self.tab_91 = QtGui.QWidget()
        self.tab_91.setObjectName(_fromUtf8("tab_91"))
        self.groupBox_17 = QtGui.QGroupBox(self.tab_91)
        self.groupBox_17.setGeometry(QtCore.QRect(10, 0, 731, 121))
        self.groupBox_17.setObjectName(_fromUtf8("groupBox_17"))
        self.gridLayoutWidget_38 = QtGui.QWidget(self.groupBox_17)
        self.gridLayoutWidget_38.setGeometry(QtCore.QRect(10, 20, 711, 80))
        self.gridLayoutWidget_38.setObjectName(_fromUtf8("gridLayoutWidget_38"))
        self.gridLayout_38 = QtGui.QGridLayout(self.gridLayoutWidget_38)
        self.gridLayout_38.setMargin(0)
        self.gridLayout_38.setObjectName(_fromUtf8("gridLayout_38"))
        self.label_13 = QtGui.QLabel(self.gridLayoutWidget_38)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_38.addWidget(self.label_13, 2, 0, 1, 1)
        self.psql_udfi_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_38)
        self.psql_udfi_lineEdit.setObjectName(_fromUtf8("psql_udfi_lineEdit"))
        self.gridLayout_38.addWidget(self.psql_udfi_lineEdit, 2, 1, 1, 1)
        self.psql_udfi_toolButton = QtGui.QToolButton(self.gridLayoutWidget_38)
        self.psql_udfi_toolButton.setObjectName(_fromUtf8("psql_udfi_toolButton"))
        self.gridLayout_38.addWidget(self.psql_udfi_toolButton, 2, 2, 1, 1)
        self.psql_udfi_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_38)
        self.psql_udfi_checkBox.setObjectName(_fromUtf8("psql_udfi_checkBox"))
        self.gridLayout_38.addWidget(self.psql_udfi_checkBox, 0, 0, 1, 1)
        self.tabWidget_19.addTab(self.tab_91, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget_19.setCurrentIndex(0)
        self.tabWidget_20.setCurrentIndex(6)
        self.tabWidget_21.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.psql_current_user_checkBox.setText(_translate("Form", "Retrieve DBMS current user", None))
        self.psql_passwords_checkBox.setText(_translate("Form", "Enumerate DBMS users password hashes", None))
        self.psql_privileges_checkBox.setText(_translate("Form", "Enumerate DBMS users privileges", None))
        self.psql_roles_checkBox.setText(_translate("Form", "Enumerate DBMS users roles", None))
        self.psql_users_checkBox.setText(_translate("Form", "Enumerate DBMS users", None))
        self.psql_is_dba_checkBox.setText(_translate("Form", "Detect if  current user is DBA", None))
        self.tabWidget_20.setTabText(self.tabWidget_20.indexOf(self.tab_79), _translate("Form", "Enumeration users", None))
        self.psql_schema_checkBox.setText(_translate("Form", "Enumerate DBMS schema", None))
        self.psql_columns_checkBox.setText(_translate("Form", "Enumerate DBMS database table columns", None))
        self.psql_count_checkBox.setText(_translate("Form", "Retrieve number of entries for table(s)", None))
        self.psql_dbs_checkBox.setText(_translate("Form", "Enumerate DBMS databases", None))
        self.psql_tables_checkBox.setText(_translate("Form", "Enumerate DBMS database tables", None))
        self.tabWidget_20.setTabText(self.tabWidget_20.indexOf(self.tab_80), _translate("Form", "Enumeration DB", None))
        self.psql_dump_all_checkBox.setText(_translate("Form", "Dump all DBMS databases tables entries", None))
        self.psql_dump_checkBox.setText(_translate("Form", "Dump DBMS database table entries", None))
        self.tabWidget_20.setTabText(self.tabWidget_20.indexOf(self.tab_81), _translate("Form", "Enumeration entries", None))
        self.psql_search_checkBox.setText(_translate("Form", "Search column(s), table(s) and/or database name(s)", None))
        self.psql_TBL_checkBox.setText(_translate("Form", "DBMS db tables to enumerate", None))
        self.psql_DB_checkBox.setText(_translate("Form", "DBMS db to enumerate", None))
        self.psql_COL_checkBox.setText(_translate("Form", "DBMS db columns to enumerate", None))
        self.tabWidget_20.setTabText(self.tabWidget_20.indexOf(self.tab_82), _translate("Form", "Enumeration search", None))
        self.psql_banner_checkBox.setText(_translate("Form", "Retrieve DBMS banner", None))
        self.tabWidget_20.setTabText(self.tabWidget_20.indexOf(self.tab_83), _translate("Form", "Enumeration generic", None))
        self.psql_sql_query_checkBox.setText(_translate("Form", "SQL statement to be executed", None))
        self.psql_sqlshell_checkBox.setText(_translate("Form", "Prompt for an interactive SQL shell", None))
        self.psql_sqlfile_checkBox.setText(_translate("Form", "Execute SQL statements from given file", None))
        self.tabWidget_20.setTabText(self.tabWidget_20.indexOf(self.tab_96), _translate("Form", "Custom", None))
        self.psql_brute_tables_checkBox.setText(_translate("Form", "Check of common tables", None))
        self.psql_brute_columns_checkBox.setText(_translate("Form", "Check  of common columns", None))
        self.tabWidget_20.setTabText(self.tabWidget_20.indexOf(self.tab_84), _translate("Form", "Brute force", None))
        self.tabWidget_19.setTabText(self.tabWidget_19.indexOf(self.tab_78), _translate("Form", "Enumeration", None))
        self.psql_fsa_write_radioButton.setText(_translate("Form", "Write a local file on the back-end DBMS file system", None))
        self.label_11.setText(_translate("Form", "Back-end DBMS absolute filepath to write to", None))
        self.psql_fsa_read_radioButton.setText(_translate("Form", "Read a file from the back-end DBMS file system", None))
        self.tabWidget_19.setTabText(self.tabWidget_19.indexOf(self.tab_85), _translate("Form", "File System Access", None))
        self.psql_fingerprint_checkBox.setText(_translate("Form", "Extensive database management system fingerprint", None))
        self.tabWidget_19.setTabText(self.tabWidget_19.indexOf(self.tab_86), _translate("Form", "Fingerprint", None))
        self.os_cmd_groupBox_3.setTitle(_translate("Form", "run arbitrary commands on the database server\'s underlying operating system", None))
        self.psql_os_cmd_checkBox.setText(_translate("Form", "Execute an operating system command", None))
        self.psql_os_shell_checkBox.setText(_translate("Form", "Prompt  interactive operating system shell", None))
        self.tabWidget_21.setTabText(self.tabWidget_21.indexOf(self.tab_88), _translate("Form", "Run arbitrary operating system command", None))
        self.meterpreter_groupBox_3.setTitle(_translate("Form", "Out-of-band stateful connection: Meterpreter", None))
        self.psql_msf_path_checkBox.setText(_translate("Form", "Local path where Metasploit Framework is installed", None))
        self.psql_os_pwn_checkBox.setText(_translate("Form", "Prompt for an OOB shell, Meterpreter or VNC", None))
        self.tabWidget_21.setTabText(self.tabWidget_21.indexOf(self.tab_89), _translate("Form", "Out-of-band stateful connection", None))
        self.reg_groupBox_3.setTitle(_translate("Form", "Windows registry access", None))
        self.psql_reg_value_checkBox.setText(_translate("Form", "Windows registry key value", None))
        self.psql_reg_key_checkBox.setText(_translate("Form", "Windows registry key path", None))
        self.psql_reg_data_checkBox.setText(_translate("Form", "Windows registry key value data", None))
        self.psql_reg_type_checkBox.setText(_translate("Form", "Windows registry key value type", None))
        self.psql_reg_add_radioButton.setText(_translate("Form", "Write a  key value data", None))
        self.psql_reg_read_radioButton.setText(_translate("Form", "Read a registry key value", None))
        self.psql_reg_del_radioButton.setText(_translate("Form", "Delete a  registry key value", None))
        self.tabWidget_21.setTabText(self.tabWidget_21.indexOf(self.tab_90), _translate("Form", "Windows registry access", None))
        self.tabWidget_19.setTabText(self.tabWidget_19.indexOf(self.tab_87), _translate("Form", "OSTakeover", None))
        self.groupBox_17.setTitle(_translate("Form", "Options  used to create custom user-defined functions", None))
        self.label_13.setText(_translate("Form", "Local path of the shared library", None))
        self.psql_udfi_toolButton.setText(_translate("Form", "Open", None))
        self.psql_udfi_checkBox.setText(_translate("Form", "Inject custom user-defined functions", None))
        self.tabWidget_19.setTabText(self.tabWidget_19.indexOf(self.tab_91), _translate("Form", "UDFI", None))


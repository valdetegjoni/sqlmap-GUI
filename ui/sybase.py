# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sybase.ui'
#
# Created: Mon Oct 10 04:01:58 2016
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

class Ui_FormSybase(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(899, 656)
        self.tabWidget_10 = QtGui.QTabWidget(Form)
        self.tabWidget_10.setGeometry(QtCore.QRect(0, 0, 781, 151))
        self.tabWidget_10.setObjectName(_fromUtf8("tabWidget_10"))
        self.tab_40 = QtGui.QWidget()
        self.tab_40.setObjectName(_fromUtf8("tab_40"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_40)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 10, 751, 80))
        self.groupBox_7.setTitle(_fromUtf8(""))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.sybase_fingerprint_checkBox = QtGui.QCheckBox(self.groupBox_7)
        self.sybase_fingerprint_checkBox.setGeometry(QtCore.QRect(10, 30, 281, 17))
        self.sybase_fingerprint_checkBox.setObjectName(_fromUtf8("sybase_fingerprint_checkBox"))
        self.tabWidget_10.addTab(self.tab_40, _fromUtf8(""))
        self.tab_43 = QtGui.QWidget()
        self.tab_43.setObjectName(_fromUtf8("tab_43"))
        self.tabWidget_8 = QtGui.QTabWidget(self.tab_43)
        self.tabWidget_8.setGeometry(QtCore.QRect(0, 0, 771, 121))
        self.tabWidget_8.setObjectName(_fromUtf8("tabWidget_8"))
        self.tab_37 = QtGui.QWidget()
        self.tab_37.setObjectName(_fromUtf8("tab_37"))
        self.gridLayoutWidget_18 = QtGui.QWidget(self.tab_37)
        self.gridLayoutWidget_18.setGeometry(QtCore.QRect(10, 10, 751, 81))
        self.gridLayoutWidget_18.setObjectName(_fromUtf8("gridLayoutWidget_18"))
        self.gridLayout_18 = QtGui.QGridLayout(self.gridLayoutWidget_18)
        self.gridLayout_18.setMargin(0)
        self.gridLayout_18.setObjectName(_fromUtf8("gridLayout_18"))
        self.sybase_passwords_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_18)
        self.sybase_passwords_checkBox.setObjectName(_fromUtf8("sybase_passwords_checkBox"))
        self.gridLayout_18.addWidget(self.sybase_passwords_checkBox, 1, 0, 1, 1)
        self.sybase_current_user_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_18)
        self.sybase_current_user_checkBox.setObjectName(_fromUtf8("sybase_current_user_checkBox"))
        self.gridLayout_18.addWidget(self.sybase_current_user_checkBox, 0, 0, 1, 1)
        self.sybase_users_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_18)
        self.sybase_users_checkBox.setObjectName(_fromUtf8("sybase_users_checkBox"))
        self.gridLayout_18.addWidget(self.sybase_users_checkBox, 2, 0, 1, 1)
        self.sybase_roles_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_18)
        self.sybase_roles_checkBox.setObjectName(_fromUtf8("sybase_roles_checkBox"))
        self.gridLayout_18.addWidget(self.sybase_roles_checkBox, 0, 1, 1, 1)
        self.sybase_privileges_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_18)
        self.sybase_privileges_checkBox.setObjectName(_fromUtf8("sybase_privileges_checkBox"))
        self.gridLayout_18.addWidget(self.sybase_privileges_checkBox, 1, 1, 1, 1)
        self.sybase_is_dba_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_18)
        self.sybase_is_dba_checkBox.setObjectName(_fromUtf8("sybase_is_dba_checkBox"))
        self.gridLayout_18.addWidget(self.sybase_is_dba_checkBox, 2, 1, 1, 1)
        self.tabWidget_8.addTab(self.tab_37, _fromUtf8(""))
        self.tab_38 = QtGui.QWidget()
        self.tab_38.setObjectName(_fromUtf8("tab_38"))
        self.gridLayoutWidget_19 = QtGui.QWidget(self.tab_38)
        self.gridLayoutWidget_19.setGeometry(QtCore.QRect(20, 10, 741, 81))
        self.gridLayoutWidget_19.setObjectName(_fromUtf8("gridLayoutWidget_19"))
        self.gridLayout_19 = QtGui.QGridLayout(self.gridLayoutWidget_19)
        self.gridLayout_19.setMargin(0)
        self.gridLayout_19.setObjectName(_fromUtf8("gridLayout_19"))
        self.sybase_columns_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_19)
        self.sybase_columns_checkBox.setObjectName(_fromUtf8("sybase_columns_checkBox"))
        self.gridLayout_19.addWidget(self.sybase_columns_checkBox, 1, 0, 1, 1)
        self.sybase_count_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_19)
        self.sybase_count_checkBox.setObjectName(_fromUtf8("sybase_count_checkBox"))
        self.gridLayout_19.addWidget(self.sybase_count_checkBox, 0, 0, 1, 1)
        self.sybase_tables_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_19)
        self.sybase_tables_checkBox.setObjectName(_fromUtf8("sybase_tables_checkBox"))
        self.gridLayout_19.addWidget(self.sybase_tables_checkBox, 2, 0, 1, 1)
        self.sybase_schema_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_19)
        self.sybase_schema_checkBox.setObjectName(_fromUtf8("sybase_schema_checkBox"))
        self.gridLayout_19.addWidget(self.sybase_schema_checkBox, 0, 1, 1, 1)
        self.sybase_dbs_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_19)
        self.sybase_dbs_checkBox.setObjectName(_fromUtf8("sybase_dbs_checkBox"))
        self.gridLayout_19.addWidget(self.sybase_dbs_checkBox, 1, 1, 1, 1)
        self.tabWidget_8.addTab(self.tab_38, _fromUtf8(""))
        self.tab_39 = QtGui.QWidget()
        self.tab_39.setObjectName(_fromUtf8("tab_39"))
        self.formLayoutWidget_13 = QtGui.QWidget(self.tab_39)
        self.formLayoutWidget_13.setGeometry(QtCore.QRect(10, 10, 222, 61))
        self.formLayoutWidget_13.setObjectName(_fromUtf8("formLayoutWidget_13"))
        self.formLayout_13 = QtGui.QFormLayout(self.formLayoutWidget_13)
        self.formLayout_13.setMargin(0)
        self.formLayout_13.setObjectName(_fromUtf8("formLayout_13"))
        self.sybase_dump_all_checkBox = QtGui.QCheckBox(self.formLayoutWidget_13)
        self.sybase_dump_all_checkBox.setObjectName(_fromUtf8("sybase_dump_all_checkBox"))
        self.formLayout_13.setWidget(2, QtGui.QFormLayout.LabelRole, self.sybase_dump_all_checkBox)
        self.sybase_dump_checkBox = QtGui.QCheckBox(self.formLayoutWidget_13)
        self.sybase_dump_checkBox.setObjectName(_fromUtf8("sybase_dump_checkBox"))
        self.formLayout_13.setWidget(1, QtGui.QFormLayout.LabelRole, self.sybase_dump_checkBox)
        self.tabWidget_8.addTab(self.tab_39, _fromUtf8(""))
        self.tab_41 = QtGui.QWidget()
        self.tab_41.setObjectName(_fromUtf8("tab_41"))
        self.formLayoutWidget_14 = QtGui.QWidget(self.tab_41)
        self.formLayoutWidget_14.setGeometry(QtCore.QRect(10, 20, 191, 51))
        self.formLayoutWidget_14.setObjectName(_fromUtf8("formLayoutWidget_14"))
        self.formLayout_14 = QtGui.QFormLayout(self.formLayoutWidget_14)
        self.formLayout_14.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_14.setMargin(0)
        self.formLayout_14.setObjectName(_fromUtf8("formLayout_14"))
        self.sybase_banner_checkBox = QtGui.QCheckBox(self.formLayoutWidget_14)
        self.sybase_banner_checkBox.setObjectName(_fromUtf8("sybase_banner_checkBox"))
        self.formLayout_14.setWidget(0, QtGui.QFormLayout.LabelRole, self.sybase_banner_checkBox)
        self.tabWidget_8.addTab(self.tab_41, _fromUtf8(""))
        self.tab_92 = QtGui.QWidget()
        self.tab_92.setObjectName(_fromUtf8("tab_92"))
        self.groupBox_18 = QtGui.QGroupBox(self.tab_92)
        self.groupBox_18.setGeometry(QtCore.QRect(10, 10, 651, 81))
        self.groupBox_18.setTitle(_fromUtf8(""))
        self.groupBox_18.setObjectName(_fromUtf8("groupBox_18"))
        self.sybase_sql_query_checkBox = QtGui.QCheckBox(self.groupBox_18)
        self.sybase_sql_query_checkBox.setGeometry(QtCore.QRect(10, 10, 181, 17))
        self.sybase_sql_query_checkBox.setObjectName(_fromUtf8("sybase_sql_query_checkBox"))
        self.sybase_sqlshell_checkBox = QtGui.QCheckBox(self.groupBox_18)
        self.sybase_sqlshell_checkBox.setGeometry(QtCore.QRect(10, 30, 201, 17))
        self.sybase_sqlshell_checkBox.setObjectName(_fromUtf8("sybase_sqlshell_checkBox"))
        self.sybase_sqlfile_checkBox = QtGui.QCheckBox(self.groupBox_18)
        self.sybase_sqlfile_checkBox.setGeometry(QtCore.QRect(10, 50, 221, 17))
        self.sybase_sqlfile_checkBox.setObjectName(_fromUtf8("sybase_sqlfile_checkBox"))
        self.sybase_sql_query_lineEdit = QtGui.QLineEdit(self.groupBox_18)
        self.sybase_sql_query_lineEdit.setGeometry(QtCore.QRect(230, 10, 411, 20))
        self.sybase_sql_query_lineEdit.setObjectName(_fromUtf8("sybase_sql_query_lineEdit"))
        self.sybase_sqlfile_lineEdit = QtGui.QLineEdit(self.groupBox_18)
        self.sybase_sqlfile_lineEdit.setGeometry(QtCore.QRect(230, 50, 401, 20))
        self.sybase_sqlfile_lineEdit.setObjectName(_fromUtf8("sybase_sqlfile_lineEdit"))
        self.tabWidget_8.addTab(self.tab_92, _fromUtf8(""))
        self.tab_42 = QtGui.QWidget()
        self.tab_42.setObjectName(_fromUtf8("tab_42"))
        self.sybase_brute_tables_checkBox = QtGui.QCheckBox(self.tab_42)
        self.sybase_brute_tables_checkBox.setGeometry(QtCore.QRect(20, 20, 141, 20))
        self.sybase_brute_tables_checkBox.setObjectName(_fromUtf8("sybase_brute_tables_checkBox"))
        self.sybase_brute_columns_checkBox = QtGui.QCheckBox(self.tab_42)
        self.sybase_brute_columns_checkBox.setGeometry(QtCore.QRect(20, 50, 151, 17))
        self.sybase_brute_columns_checkBox.setObjectName(_fromUtf8("sybase_brute_columns_checkBox"))
        self.tabWidget_8.addTab(self.tab_42, _fromUtf8(""))
        self.tabWidget_10.addTab(self.tab_43, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget_10.setCurrentIndex(0)
        self.tabWidget_8.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.sybase_fingerprint_checkBox.setText(_translate("Form", "Extensive database management system fingerprint", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_40), _translate("Form", "Fingerprint", None))
        self.sybase_passwords_checkBox.setText(_translate("Form", "Enumerate DBMS users password hashes", None))
        self.sybase_current_user_checkBox.setText(_translate("Form", "Retrieve DBMS current user", None))
        self.sybase_users_checkBox.setText(_translate("Form", "Enumerate DBMS users", None))
        self.sybase_roles_checkBox.setText(_translate("Form", "Enumerate DBMS users roles", None))
        self.sybase_privileges_checkBox.setText(_translate("Form", "Enumerate DBMS users privileges", None))
        self.sybase_is_dba_checkBox.setText(_translate("Form", "Detect if  current user is DBA", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_37), _translate("Form", "Enumeration users", None))
        self.sybase_columns_checkBox.setText(_translate("Form", "Enumerate DBMS database table columns", None))
        self.sybase_count_checkBox.setText(_translate("Form", "Retrieve number of entries for table(s)", None))
        self.sybase_tables_checkBox.setText(_translate("Form", "Enumerate DBMS database tables", None))
        self.sybase_schema_checkBox.setText(_translate("Form", "Enumerate DBMS schema", None))
        self.sybase_dbs_checkBox.setText(_translate("Form", "Enumerate DBMS databases", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_38), _translate("Form", "Enumeration DB", None))
        self.sybase_dump_all_checkBox.setText(_translate("Form", "Dump all DBMS databases tables entries", None))
        self.sybase_dump_checkBox.setText(_translate("Form", "Dump DBMS database table entries", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_39), _translate("Form", "Enumeration entries", None))
        self.sybase_banner_checkBox.setText(_translate("Form", "Retrieve DBMS banner", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_41), _translate("Form", "Enumeration generic", None))
        self.sybase_sql_query_checkBox.setText(_translate("Form", "SQL statement to be executed", None))
        self.sybase_sqlshell_checkBox.setText(_translate("Form", "Prompt for an interactive SQL shell", None))
        self.sybase_sqlfile_checkBox.setText(_translate("Form", "Execute SQL statements from given file", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_92), _translate("Form", "Custom Enumeration", None))
        self.sybase_brute_tables_checkBox.setText(_translate("Form", "Check of common tables", None))
        self.sybase_brute_columns_checkBox.setText(_translate("Form", "Check  of common columns", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_42), _translate("Form", "Brute force", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_43), _translate("Form", "Enumeration", None))


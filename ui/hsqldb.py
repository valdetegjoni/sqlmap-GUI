# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hsqldb.ui'
#
# Created: Mon Oct 10 04:18:03 2016
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

class Ui_FormHsqldb(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(899, 656)
        self.tabWidget_6 = QtGui.QTabWidget(Form)
        self.tabWidget_6.setGeometry(QtCore.QRect(0, 0, 781, 161))
        self.tabWidget_6.setObjectName(_fromUtf8("tabWidget_6"))
        self.db2_enum_tab_3 = QtGui.QWidget()
        self.db2_enum_tab_3.setObjectName(_fromUtf8("db2_enum_tab_3"))
        self.tabWidget_7 = QtGui.QTabWidget(self.db2_enum_tab_3)
        self.tabWidget_7.setGeometry(QtCore.QRect(0, 0, 771, 131))
        self.tabWidget_7.setObjectName(_fromUtf8("tabWidget_7"))
        self.tab_14 = QtGui.QWidget()
        self.tab_14.setObjectName(_fromUtf8("tab_14"))
        self.gridLayoutWidget_11 = QtGui.QWidget(self.tab_14)
        self.gridLayoutWidget_11.setGeometry(QtCore.QRect(10, 10, 711, 51))
        self.gridLayoutWidget_11.setObjectName(_fromUtf8("gridLayoutWidget_11"))
        self.gridLayout_11 = QtGui.QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_11.setMargin(0)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.hsql_roles_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_11)
        self.hsql_roles_checkBox.setObjectName(_fromUtf8("hsql_roles_checkBox"))
        self.gridLayout_11.addWidget(self.hsql_roles_checkBox, 0, 1, 1, 1)
        self.hsql_is_dba_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_11)
        self.hsql_is_dba_checkBox.setObjectName(_fromUtf8("hsql_is_dba_checkBox"))
        self.gridLayout_11.addWidget(self.hsql_is_dba_checkBox, 1, 1, 1, 1)
        self.hsql_current_user_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_11)
        self.hsql_current_user_checkBox.setObjectName(_fromUtf8("hsql_current_user_checkBox"))
        self.gridLayout_11.addWidget(self.hsql_current_user_checkBox, 0, 0, 1, 1)
        self.hsql_users_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_11)
        self.hsql_users_checkBox.setObjectName(_fromUtf8("hsql_users_checkBox"))
        self.gridLayout_11.addWidget(self.hsql_users_checkBox, 1, 0, 1, 1)
        self.tabWidget_7.addTab(self.tab_14, _fromUtf8(""))
        self.tab_18 = QtGui.QWidget()
        self.tab_18.setObjectName(_fromUtf8("tab_18"))
        self.gridLayoutWidget_12 = QtGui.QWidget(self.tab_18)
        self.gridLayoutWidget_12.setGeometry(QtCore.QRect(20, 10, 701, 81))
        self.gridLayoutWidget_12.setObjectName(_fromUtf8("gridLayoutWidget_12"))
        self.gridLayout_12 = QtGui.QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_12.setMargin(0)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.hsql_columns_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_12)
        self.hsql_columns_checkBox.setObjectName(_fromUtf8("hsql_columns_checkBox"))
        self.gridLayout_12.addWidget(self.hsql_columns_checkBox, 1, 0, 1, 1)
        self.hsql_count_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_12)
        self.hsql_count_checkBox.setObjectName(_fromUtf8("hsql_count_checkBox"))
        self.gridLayout_12.addWidget(self.hsql_count_checkBox, 0, 0, 1, 1)
        self.hsql_tables_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_12)
        self.hsql_tables_checkBox.setObjectName(_fromUtf8("hsql_tables_checkBox"))
        self.gridLayout_12.addWidget(self.hsql_tables_checkBox, 2, 0, 1, 1)
        self.hsql_schema_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_12)
        self.hsql_schema_checkBox.setObjectName(_fromUtf8("hsql_schema_checkBox"))
        self.gridLayout_12.addWidget(self.hsql_schema_checkBox, 0, 1, 1, 1)
        self.hsql_dbs_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_12)
        self.hsql_dbs_checkBox.setObjectName(_fromUtf8("hsql_dbs_checkBox"))
        self.gridLayout_12.addWidget(self.hsql_dbs_checkBox, 1, 1, 1, 1)
        self.tabWidget_7.addTab(self.tab_18, _fromUtf8(""))
        self.tab_19 = QtGui.QWidget()
        self.tab_19.setObjectName(_fromUtf8("tab_19"))
        self.formLayoutWidget_6 = QtGui.QWidget(self.tab_19)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(10, 10, 222, 61))
        self.formLayoutWidget_6.setObjectName(_fromUtf8("formLayoutWidget_6"))
        self.formLayout_6 = QtGui.QFormLayout(self.formLayoutWidget_6)
        self.formLayout_6.setMargin(0)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.hsql_dump_all_checkBox = QtGui.QCheckBox(self.formLayoutWidget_6)
        self.hsql_dump_all_checkBox.setAutoExclusive(True)
        self.hsql_dump_all_checkBox.setObjectName(_fromUtf8("hsql_dump_all_checkBox"))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.LabelRole, self.hsql_dump_all_checkBox)
        self.hsql_dump_checkBox = QtGui.QCheckBox(self.formLayoutWidget_6)
        self.hsql_dump_checkBox.setAutoExclusive(True)
        self.hsql_dump_checkBox.setObjectName(_fromUtf8("hsql_dump_checkBox"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.LabelRole, self.hsql_dump_checkBox)
        self.tabWidget_7.addTab(self.tab_19, _fromUtf8(""))
        self.tab_20 = QtGui.QWidget()
        self.tab_20.setObjectName(_fromUtf8("tab_20"))
        self.hsql_search_checkBox = QtGui.QCheckBox(self.tab_20)
        self.hsql_search_checkBox.setGeometry(QtCore.QRect(20, 10, 274, 17))
        self.hsql_search_checkBox.setObjectName(_fromUtf8("hsql_search_checkBox"))
        self.gridLayoutWidget_14 = QtGui.QWidget(self.tab_20)
        self.gridLayoutWidget_14.setGeometry(QtCore.QRect(20, 30, 711, 61))
        self.gridLayoutWidget_14.setObjectName(_fromUtf8("gridLayoutWidget_14"))
        self.gridLayout_14 = QtGui.QGridLayout(self.gridLayoutWidget_14)
        self.gridLayout_14.setMargin(0)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.hsql_TBL_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_14)
        self.hsql_TBL_checkBox.setObjectName(_fromUtf8("hsql_TBL_checkBox"))
        self.gridLayout_14.addWidget(self.hsql_TBL_checkBox, 1, 0, 1, 1)
        self.hsql_DB_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_14)
        self.hsql_DB_lineEdit.setObjectName(_fromUtf8("hsql_DB_lineEdit"))
        self.gridLayout_14.addWidget(self.hsql_DB_lineEdit, 0, 1, 1, 1)
        self.hsql_DB_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_14)
        self.hsql_DB_checkBox.setObjectName(_fromUtf8("hsql_DB_checkBox"))
        self.gridLayout_14.addWidget(self.hsql_DB_checkBox, 0, 0, 1, 1)
        self.hsql_TBL_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_14)
        self.hsql_TBL_lineEdit.setObjectName(_fromUtf8("hsql_TBL_lineEdit"))
        self.gridLayout_14.addWidget(self.hsql_TBL_lineEdit, 1, 1, 1, 1)
        self.hsql_COL_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_14)
        self.hsql_COL_checkBox.setObjectName(_fromUtf8("hsql_COL_checkBox"))
        self.gridLayout_14.addWidget(self.hsql_COL_checkBox, 1, 2, 1, 1)
        self.hsql_COL_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_14)
        self.hsql_COL_lineEdit.setObjectName(_fromUtf8("hsql_COL_lineEdit"))
        self.gridLayout_14.addWidget(self.hsql_COL_lineEdit, 1, 3, 1, 1)
        self.tabWidget_7.addTab(self.tab_20, _fromUtf8(""))
        self.tab_21 = QtGui.QWidget()
        self.tab_21.setObjectName(_fromUtf8("tab_21"))
        self.formLayoutWidget_7 = QtGui.QWidget(self.tab_21)
        self.formLayoutWidget_7.setGeometry(QtCore.QRect(10, 20, 191, 51))
        self.formLayoutWidget_7.setObjectName(_fromUtf8("formLayoutWidget_7"))
        self.formLayout_7 = QtGui.QFormLayout(self.formLayoutWidget_7)
        self.formLayout_7.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_7.setMargin(0)
        self.formLayout_7.setObjectName(_fromUtf8("formLayout_7"))
        self.hsql_banner_checkBox = QtGui.QCheckBox(self.formLayoutWidget_7)
        self.hsql_banner_checkBox.setObjectName(_fromUtf8("hsql_banner_checkBox"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.LabelRole, self.hsql_banner_checkBox)
        self.tabWidget_7.addTab(self.tab_21, _fromUtf8(""))
        self.tab_22 = QtGui.QWidget()
        self.tab_22.setObjectName(_fromUtf8("tab_22"))
        self.hsql_sql_query_checkBox = QtGui.QCheckBox(self.tab_22)
        self.hsql_sql_query_checkBox.setGeometry(QtCore.QRect(10, 10, 181, 17))
        self.hsql_sql_query_checkBox.setObjectName(_fromUtf8("hsql_sql_query_checkBox"))
        self.hsql_sql_query_lineEdit = QtGui.QLineEdit(self.tab_22)
        self.hsql_sql_query_lineEdit.setGeometry(QtCore.QRect(230, 10, 491, 20))
        self.hsql_sql_query_lineEdit.setObjectName(_fromUtf8("hsql_sql_query_lineEdit"))
        self.hsql_sqlshell_checkBox = QtGui.QCheckBox(self.tab_22)
        self.hsql_sqlshell_checkBox.setGeometry(QtCore.QRect(10, 40, 201, 17))
        self.hsql_sqlshell_checkBox.setObjectName(_fromUtf8("hsql_sqlshell_checkBox"))
        self.hsql_sqlfile_checkBox = QtGui.QCheckBox(self.tab_22)
        self.hsql_sqlfile_checkBox.setGeometry(QtCore.QRect(10, 70, 221, 17))
        self.hsql_sqlfile_checkBox.setObjectName(_fromUtf8("hsql_sqlfile_checkBox"))
        self.hsql_sqlfile_lineEdit = QtGui.QLineEdit(self.tab_22)
        self.hsql_sqlfile_lineEdit.setGeometry(QtCore.QRect(232, 70, 491, 20))
        self.hsql_sqlfile_lineEdit.setObjectName(_fromUtf8("hsql_sqlfile_lineEdit"))
        self.tabWidget_7.addTab(self.tab_22, _fromUtf8(""))
        self.tab_23 = QtGui.QWidget()
        self.tab_23.setObjectName(_fromUtf8("tab_23"))
        self.hsql_brute_tables_checkBox = QtGui.QCheckBox(self.tab_23)
        self.hsql_brute_tables_checkBox.setGeometry(QtCore.QRect(10, 10, 141, 20))
        self.hsql_brute_tables_checkBox.setObjectName(_fromUtf8("hsql_brute_tables_checkBox"))
        self.hsql_brute_columns_checkBox = QtGui.QCheckBox(self.tab_23)
        self.hsql_brute_columns_checkBox.setGeometry(QtCore.QRect(10, 40, 151, 17))
        self.hsql_brute_columns_checkBox.setObjectName(_fromUtf8("hsql_brute_columns_checkBox"))
        self.tabWidget_7.addTab(self.tab_23, _fromUtf8(""))
        self.tabWidget_6.addTab(self.db2_enum_tab_3, _fromUtf8(""))
        self.db2_fingerprint_tab_3 = QtGui.QWidget()
        self.db2_fingerprint_tab_3.setObjectName(_fromUtf8("db2_fingerprint_tab_3"))
        self.groupBox_6 = QtGui.QGroupBox(self.db2_fingerprint_tab_3)
        self.groupBox_6.setGeometry(QtCore.QRect(9, 10, 293, 37))
        self.groupBox_6.setTitle(_fromUtf8(""))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_40 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_40.setObjectName(_fromUtf8("gridLayout_40"))
        self.hsql_fingerprint_checkBox = QtGui.QCheckBox(self.groupBox_6)
        self.hsql_fingerprint_checkBox.setObjectName(_fromUtf8("hsql_fingerprint_checkBox"))
        self.gridLayout_40.addWidget(self.hsql_fingerprint_checkBox, 0, 0, 1, 1)
        self.tabWidget_6.addTab(self.db2_fingerprint_tab_3, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget_6.setCurrentIndex(0)
        self.tabWidget_7.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.hsql_roles_checkBox.setText(_translate("Form", "Enumerate DBMS users roles", None))
        self.hsql_is_dba_checkBox.setText(_translate("Form", "Detect if  current user is DBA", None))
        self.hsql_current_user_checkBox.setText(_translate("Form", "Retrieve DBMS current user", None))
        self.hsql_users_checkBox.setText(_translate("Form", "Enumerate DBMS users", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_14), _translate("Form", "Users", None))
        self.hsql_columns_checkBox.setText(_translate("Form", "Enumerate DBMS database table columns", None))
        self.hsql_count_checkBox.setText(_translate("Form", "Retrieve number of entries for table(s)", None))
        self.hsql_tables_checkBox.setText(_translate("Form", "Enumerate DBMS database tables", None))
        self.hsql_schema_checkBox.setText(_translate("Form", "Enumerate DBMS schema", None))
        self.hsql_dbs_checkBox.setText(_translate("Form", "Enumerate DBMS databases", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_18), _translate("Form", "Databases", None))
        self.hsql_dump_all_checkBox.setText(_translate("Form", "Dump all DBMS databases tables entries", None))
        self.hsql_dump_checkBox.setText(_translate("Form", "Dump DBMS database table entries", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_19), _translate("Form", "Entries", None))
        self.hsql_search_checkBox.setText(_translate("Form", "Search column(s), table(s) and/or database name(s)", None))
        self.hsql_TBL_checkBox.setText(_translate("Form", "DBMS db tables to enumerate", None))
        self.hsql_DB_checkBox.setText(_translate("Form", "DBMS db to enumerate", None))
        self.hsql_COL_checkBox.setText(_translate("Form", "DBMS db columns to enumerate", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_20), _translate("Form", "Search", None))
        self.hsql_banner_checkBox.setText(_translate("Form", "Retrieve DBMS banner", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_21), _translate("Form", "Generic", None))
        self.hsql_sql_query_checkBox.setText(_translate("Form", "SQL statement to be executed", None))
        self.hsql_sqlshell_checkBox.setText(_translate("Form", "Prompt for an interactive SQL shell", None))
        self.hsql_sqlfile_checkBox.setText(_translate("Form", "Execute SQL statements from given file", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_22), _translate("Form", "Custom", None))
        self.hsql_brute_tables_checkBox.setText(_translate("Form", "Check of common tables", None))
        self.hsql_brute_columns_checkBox.setText(_translate("Form", "Check  of common columns", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_23), _translate("Form", "Brute force", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.db2_enum_tab_3), _translate("Form", "Enumeration", None))
        self.hsql_fingerprint_checkBox.setText(_translate("Form", "Extensive database management system fingerprint", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.db2_fingerprint_tab_3), _translate("Form", "Fingerprint", None))


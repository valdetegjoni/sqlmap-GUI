# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enumeration.ui'
#
# Created: Tue Oct 11 18:45:11 2016
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

class Ui_FormEnumeration(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(899, 656)
        self.tabWidget_20 = QtGui.QTabWidget(Form)
        self.tabWidget_20.setGeometry(QtCore.QRect(0, 0, 760, 105)) #10, 0, 791, 170
        self.tabWidget_20.setObjectName(_fromUtf8("tabWidget_20"))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.groupBox_18 = QtGui.QGroupBox(self.tab_5)
        self.groupBox_18.setGeometry(QtCore.QRect(10, 10, 321, 51))
        self.groupBox_18.setTitle(_fromUtf8(""))
        self.groupBox_18.setObjectName(_fromUtf8("groupBox_18"))
        self.fingerprint_checkBox = QtGui.QCheckBox(self.groupBox_18)
        self.fingerprint_checkBox.setGeometry(QtCore.QRect(10, 20, 281, 17))
        self.fingerprint_checkBox.setObjectName(_fromUtf8("fingerprint_checkBox"))
        self.tabWidget_20.addTab(self.tab_5, _fromUtf8(""))
        self.tab_79 = QtGui.QWidget()
        self.tab_79.setObjectName(_fromUtf8("tab_79"))
        self.gridLayoutWidget_33 = QtGui.QWidget(self.tab_79)
        self.gridLayoutWidget_33.setGeometry(QtCore.QRect(10, 10, 578, 42))
        self.gridLayoutWidget_33.setObjectName(_fromUtf8("gridLayoutWidget_33"))
        self.gridLayout_33 = QtGui.QGridLayout(self.gridLayoutWidget_33)
        self.gridLayout_33.setMargin(0)
        self.gridLayout_33.setObjectName(_fromUtf8("gridLayout_33"))
        self.is_dba_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_33)
        self.is_dba_checkBox.setObjectName(_fromUtf8("is_dba_checkBox"))
        self.gridLayout_33.addWidget(self.is_dba_checkBox, 1, 2, 1, 1)
        self.current_user_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_33)
        self.current_user_checkBox.setObjectName(_fromUtf8("current_user_checkBox"))
        self.gridLayout_33.addWidget(self.current_user_checkBox, 0, 0, 1, 1)
        self.users_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_33)
        self.users_checkBox.setObjectName(_fromUtf8("users_checkBox"))
        self.gridLayout_33.addWidget(self.users_checkBox, 0, 2, 1, 1)
        self.roles_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_33)
        self.roles_checkBox.setObjectName(_fromUtf8("roles_checkBox"))
        self.gridLayout_33.addWidget(self.roles_checkBox, 0, 1, 1, 1)
        self.privileges_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_33)
        self.privileges_checkBox.setObjectName(_fromUtf8("privileges_checkBox"))
        self.gridLayout_33.addWidget(self.privileges_checkBox, 1, 1, 1, 1)
        self.passwords_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_33)
        self.passwords_checkBox.setObjectName(_fromUtf8("passwords_checkBox"))
        self.gridLayout_33.addWidget(self.passwords_checkBox, 1, 0, 1, 1)
        self.tabWidget_20.addTab(self.tab_79, _fromUtf8(""))
        self.tab_80 = QtGui.QWidget()
        self.tab_80.setObjectName(_fromUtf8("tab_80"))
        self.gridLayoutWidget_34 = QtGui.QWidget(self.tab_80)
        self.gridLayoutWidget_34.setGeometry(QtCore.QRect(20, 10, 741, 61))
        self.gridLayoutWidget_34.setObjectName(_fromUtf8("gridLayoutWidget_34"))
        self.gridLayout_34 = QtGui.QGridLayout(self.gridLayoutWidget_34)
        self.gridLayout_34.setMargin(0)
        self.gridLayout_34.setObjectName(_fromUtf8("gridLayout_34"))
        self.schema_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_34)
        self.schema_checkBox.setObjectName(_fromUtf8("schema_checkBox"))
        self.gridLayout_34.addWidget(self.schema_checkBox, 0, 1, 1, 1)
        self.columns_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_34)
        self.columns_checkBox.setObjectName(_fromUtf8("columns_checkBox"))
        self.gridLayout_34.addWidget(self.columns_checkBox, 1, 0, 1, 1)
        self.count_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_34)
        self.count_checkBox.setObjectName(_fromUtf8("count_checkBox"))
        self.gridLayout_34.addWidget(self.count_checkBox, 0, 0, 1, 1)
        self.dbs_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_34)
        self.dbs_checkBox.setObjectName(_fromUtf8("dbs_checkBox"))
        self.gridLayout_34.addWidget(self.dbs_checkBox, 0, 2, 1, 1)
        self.tables_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_34)
        self.tables_checkBox.setObjectName(_fromUtf8("tables_checkBox"))
        self.gridLayout_34.addWidget(self.tables_checkBox, 1, 1, 1, 1)
        self.current_db_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_34)
        self.current_db_checkBox.setObjectName(_fromUtf8("current_db_checkBox"))
        self.gridLayout_34.addWidget(self.current_db_checkBox, 1, 2, 1, 1)
        self.tabWidget_20.addTab(self.tab_80, _fromUtf8(""))
        self.tab_81 = QtGui.QWidget()
        self.tab_81.setObjectName(_fromUtf8("tab_81"))
        self.formLayoutWidget_21 = QtGui.QWidget(self.tab_81)
        self.formLayoutWidget_21.setGeometry(QtCore.QRect(10, 10, 222, 61))
        self.formLayoutWidget_21.setObjectName(_fromUtf8("formLayoutWidget_21"))
        self.formLayout_21 = QtGui.QFormLayout(self.formLayoutWidget_21)
        self.formLayout_21.setMargin(0)
        self.formLayout_21.setObjectName(_fromUtf8("formLayout_21"))
        self.dump_all_checkBox = QtGui.QCheckBox(self.formLayoutWidget_21)
        self.dump_all_checkBox.setObjectName(_fromUtf8("dump_all_checkBox"))
        self.formLayout_21.setWidget(2, QtGui.QFormLayout.LabelRole, self.dump_all_checkBox)
        self.dump_checkBox = QtGui.QCheckBox(self.formLayoutWidget_21)
        self.dump_checkBox.setObjectName(_fromUtf8("dump_checkBox"))
        self.formLayout_21.setWidget(1, QtGui.QFormLayout.LabelRole, self.dump_checkBox)
        self.tabWidget_20.addTab(self.tab_81, _fromUtf8(""))
        self.tab_82 = QtGui.QWidget()
        self.tab_82.setObjectName(_fromUtf8("tab_82"))
        self.search_checkBox = QtGui.QCheckBox(self.tab_82)
        self.search_checkBox.setGeometry(QtCore.QRect(20, 10, 274, 17))
        self.search_checkBox.setObjectName(_fromUtf8("search_checkBox"))
        self.gridLayoutWidget_35 = QtGui.QWidget(self.tab_82)
        self.gridLayoutWidget_35.setGeometry(QtCore.QRect(20, 30, 741, 51))
        self.gridLayoutWidget_35.setObjectName(_fromUtf8("gridLayoutWidget_35"))
        self.gridLayout_35 = QtGui.QGridLayout(self.gridLayoutWidget_35)
        self.gridLayout_35.setMargin(0)
        self.gridLayout_35.setObjectName(_fromUtf8("gridLayout_35"))
        self.DB_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_35)
        self.DB_lineEdit.setObjectName(_fromUtf8("DB_lineEdit"))
        self.gridLayout_35.addWidget(self.DB_lineEdit, 0, 1, 1, 1)
        self.TBL_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_35)
        self.TBL_checkBox.setObjectName(_fromUtf8("TBL_checkBox"))
        self.gridLayout_35.addWidget(self.TBL_checkBox, 1, 0, 1, 1)
        self.TBL_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_35)
        self.TBL_lineEdit.setObjectName(_fromUtf8("TBL_lineEdit"))
        self.gridLayout_35.addWidget(self.TBL_lineEdit, 1, 1, 1, 1)
        self.DB_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_35)
        self.DB_checkBox.setObjectName(_fromUtf8("DB_checkBox"))
        self.gridLayout_35.addWidget(self.DB_checkBox, 0, 0, 1, 1)
        self.COL_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_35)
        self.COL_checkBox.setObjectName(_fromUtf8("COL_checkBox"))
        self.gridLayout_35.addWidget(self.COL_checkBox, 1, 2, 1, 1)
        self.COL_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_35)
        self.COL_lineEdit.setObjectName(_fromUtf8("COL_lineEdit"))
        self.gridLayout_35.addWidget(self.COL_lineEdit, 1, 3, 1, 1)
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
        self.banner_checkBox = QtGui.QCheckBox(self.formLayoutWidget_22)
        self.banner_checkBox.setObjectName(_fromUtf8("banner_checkBox"))
        self.formLayout_22.setWidget(0, QtGui.QFormLayout.LabelRole, self.banner_checkBox)
        self.hostname_checkBox = QtGui.QCheckBox(self.formLayoutWidget_22)
        self.hostname_checkBox.setObjectName(_fromUtf8("hostname_checkBox"))
        self.formLayout_22.setWidget(1, QtGui.QFormLayout.LabelRole, self.hostname_checkBox)
        self.tabWidget_20.addTab(self.tab_83, _fromUtf8(""))
        self.tab_96 = QtGui.QWidget()
        self.tab_96.setObjectName(_fromUtf8("tab_96"))
        self.gridLayoutWidget = QtGui.QWidget(self.tab_96)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 641, 73))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.sqlshell_checkBox = QtGui.QCheckBox(self.gridLayoutWidget)
        self.sqlshell_checkBox.setObjectName(_fromUtf8("sqlshell_checkBox"))
        self.gridLayout.addWidget(self.sqlshell_checkBox, 1, 0, 1, 1)
        self.sqlfile_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.sqlfile_lineEdit.setObjectName(_fromUtf8("sqlfile_lineEdit"))
        self.gridLayout.addWidget(self.sqlfile_lineEdit, 2, 1, 1, 1)
        self.sql_query_checkBox = QtGui.QCheckBox(self.gridLayoutWidget)
        self.sql_query_checkBox.setObjectName(_fromUtf8("sql_query_checkBox"))
        self.gridLayout.addWidget(self.sql_query_checkBox, 0, 0, 1, 1)
        self.sqlfile_checkBox = QtGui.QCheckBox(self.gridLayoutWidget)
        self.sqlfile_checkBox.setAutoExclusive(True)
        self.sqlfile_checkBox.setObjectName(_fromUtf8("sqlfile_checkBox"))
        self.gridLayout.addWidget(self.sqlfile_checkBox, 2, 0, 1, 1)
        self.sql_query_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.sql_query_lineEdit.setObjectName(_fromUtf8("sql_query_lineEdit"))
        self.gridLayout.addWidget(self.sql_query_lineEdit, 0, 1, 1, 1)
        self.sqlfile_toolButton = QtGui.QToolButton(self.gridLayoutWidget)
        self.sqlfile_toolButton.setText(_fromUtf8(""))
        self.sqlfile_toolButton.setObjectName(_fromUtf8("sqlfile_toolButton"))
        self.gridLayout.addWidget(self.sqlfile_toolButton, 2, 2, 1, 1)
        self.tabWidget_20.addTab(self.tab_96, _fromUtf8(""))
        self.tab_84 = QtGui.QWidget()
        self.tab_84.setObjectName(_fromUtf8("tab_84"))
        self.brute_tables_checkBox = QtGui.QCheckBox(self.tab_84)
        self.brute_tables_checkBox.setGeometry(QtCore.QRect(10, 10, 141, 20))
        self.brute_tables_checkBox.setObjectName(_fromUtf8("brute_tables_checkBox"))
        self.brute_columns_checkBox = QtGui.QCheckBox(self.tab_84)
        self.brute_columns_checkBox.setGeometry(QtCore.QRect(10, 40, 151, 17))
        self.brute_columns_checkBox.setObjectName(_fromUtf8("brute_columns_checkBox"))
        self.tabWidget_20.addTab(self.tab_84, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget_20.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.fingerprint_checkBox.setText(_translate("Form", "Extensive database management system fingerprint", None))
        self.tabWidget_20.setTabText(self.tabWidget_20.indexOf(self.tab_5), _translate("Form", "Fingerprint", None))
        self.is_dba_checkBox.setText(_translate("Form", "Detect if  current user is DBA", None))
        self.current_user_checkBox.setText(_translate("Form", "Retrieve DBMS current user", None))
        self.users_checkBox.setText(_translate("Form", "Enumerate DBMS users", None))
        self.roles_checkBox.setText(_translate("Form", "Enumerate DBMS users roles", None))
        self.privileges_checkBox.setText(_translate("Form", "Enumerate DBMS users privileges", None))
        self.passwords_checkBox.setText(_translate("Form", "Enumerate DBMS users password hashes", None))
        self.tabWidget_20.setTabText(self.tabWidget_20.indexOf(self.tab_79), _translate("Form", "Users", None))
        self.schema_checkBox.setText(_translate("Form", "Enumerate DBMS schema", None))
        self.columns_checkBox.setText(_translate("Form", "Enumerate DBMS database table columns", None))
        self.count_checkBox.setText(_translate("Form", "Retrieve number of entries for table(s)", None))
        self.dbs_checkBox.setText(_translate("Form", "Enumerate DBMS databases", None))
        self.tables_checkBox.setText(_translate("Form", "Enumerate DBMS database tables", None))
        self.current_db_checkBox.setText(_translate("Form", "Retrieve DBMS current database", None))
        self.tabWidget_20.setTabText(self.tabWidget_20.indexOf(self.tab_80), _translate("Form", "Databases", None))
        self.dump_all_checkBox.setText(_translate("Form", "Dump all DBMS databases tables entries", None))
        self.dump_checkBox.setText(_translate("Form", "Dump DBMS database table entries", None))
        self.tabWidget_20.setTabText(self.tabWidget_20.indexOf(self.tab_81), _translate("Form", "Entries", None))
        self.search_checkBox.setText(_translate("Form", "Search column(s), table(s) and/or database name(s)", None))
        self.TBL_checkBox.setText(_translate("Form", "DBMS db tables to enumerate", None))
        self.DB_checkBox.setText(_translate("Form", "DBMS db to enumerate", None))
        self.COL_checkBox.setText(_translate("Form", "DBMS db columns to enumerate", None))
        self.tabWidget_20.setTabText(self.tabWidget_20.indexOf(self.tab_82), _translate("Form", "Search", None))
        self.banner_checkBox.setText(_translate("Form", "Retrieve DBMS banner", None))
        self.hostname_checkBox.setText(_translate("Form", "Retrieve DBMS server hostname", None))
        self.tabWidget_20.setTabText(self.tabWidget_20.indexOf(self.tab_83), _translate("Form", " Generic", None))
        self.sqlshell_checkBox.setText(_translate("Form", "Prompt for an interactive SQL shell", None))
        self.sql_query_checkBox.setText(_translate("Form", "SQL statement to be executed", None))
        self.sqlfile_checkBox.setText(_translate("Form", "Execute SQL statements from given file", None))
        self.tabWidget_20.setTabText(self.tabWidget_20.indexOf(self.tab_96), _translate("Form", "Custom", None))
        self.brute_tables_checkBox.setText(_translate("Form", "Check of common tables", None))
        self.brute_columns_checkBox.setText(_translate("Form", "Check  of common columns", None))
        self.tabWidget_20.setTabText(self.tabWidget_20.indexOf(self.tab_84), _translate("Form", "Brute force", None))

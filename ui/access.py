# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'access.ui'
#
# Created: Mon Oct 10 02:07:28 2016
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

class Ui_FormAccess(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(899, 656)
        self.tabWidget_23 = QtGui.QTabWidget(Form)
        self.tabWidget_23.setGeometry(QtCore.QRect(0, 0, 791, 141)) #0, 0, 771, 111
        self.tabWidget_23.setObjectName(_fromUtf8("tabWidget_23"))
        self.tab_100 = QtGui.QWidget()
        self.tab_100.setObjectName(_fromUtf8("tab_100"))
        self.tabWidget_9 = QtGui.QTabWidget(self.tab_100)
        self.tabWidget_9.setGeometry(QtCore.QRect(0, 0, 761, 114))
        self.tabWidget_9.setObjectName(_fromUtf8("tabWidget_9"))
        self.tab_25 = QtGui.QWidget()
        self.tab_25.setObjectName(_fromUtf8("tab_25"))
        self.gridLayoutWidget_17 = QtGui.QWidget(self.tab_25)
        self.gridLayoutWidget_17.setGeometry(QtCore.QRect(20, 10, 701, 51))
        self.gridLayoutWidget_17.setObjectName(_fromUtf8("gridLayoutWidget_17"))
        self.gridLayout_17 = QtGui.QGridLayout(self.gridLayoutWidget_17)
        self.gridLayout_17.setMargin(0)
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
        self.access_columns_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_17)
        self.access_columns_checkBox.setObjectName(_fromUtf8("access_columns_checkBox"))
        self.gridLayout_17.addWidget(self.access_columns_checkBox, 1, 0, 1, 1)
        self.access_count_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_17)
        self.access_count_checkBox.setObjectName(_fromUtf8("access_count_checkBox"))
        self.gridLayout_17.addWidget(self.access_count_checkBox, 0, 0, 1, 1)
        self.access_schema_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_17)
        self.access_schema_checkBox.setObjectName(_fromUtf8("access_schema_checkBox"))
        self.gridLayout_17.addWidget(self.access_schema_checkBox, 0, 1, 1, 1)
        self.access_tables_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_17)
        self.access_tables_checkBox.setObjectName(_fromUtf8("access_tables_checkBox"))
        self.gridLayout_17.addWidget(self.access_tables_checkBox, 1, 1, 1, 1)
        self.tabWidget_9.addTab(self.tab_25, _fromUtf8(""))
        self.tab_27 = QtGui.QWidget()
        self.tab_27.setObjectName(_fromUtf8("tab_27"))
        self.formLayoutWidget_8 = QtGui.QWidget(self.tab_27)
        self.formLayoutWidget_8.setGeometry(QtCore.QRect(10, 10, 222, 61))
        self.formLayoutWidget_8.setObjectName(_fromUtf8("formLayoutWidget_8"))
        self.formLayout_8 = QtGui.QFormLayout(self.formLayoutWidget_8)
        self.formLayout_8.setMargin(0)
        self.formLayout_8.setObjectName(_fromUtf8("formLayout_8"))
        self.access_dump_all_checkBox = QtGui.QCheckBox(self.formLayoutWidget_8)
        self.access_dump_all_checkBox.setAutoExclusive(True)
        self.access_dump_all_checkBox.setObjectName(_fromUtf8("access_dump_all_checkBox"))
        self.formLayout_8.setWidget(2, QtGui.QFormLayout.LabelRole, self.access_dump_all_checkBox)
        self.access_dump_checkBox = QtGui.QCheckBox(self.formLayoutWidget_8)
        self.access_dump_checkBox.setAutoExclusive(True)
        self.access_dump_checkBox.setObjectName(_fromUtf8("access_dump_checkBox"))
        self.formLayout_8.setWidget(1, QtGui.QFormLayout.LabelRole, self.access_dump_checkBox)
        self.tabWidget_9.addTab(self.tab_27, _fromUtf8(""))
        self.tab_30 = QtGui.QWidget()
        self.tab_30.setObjectName(_fromUtf8("tab_30"))
        self.gridLayout_39 = QtGui.QGridLayout(self.tab_30)
        self.gridLayout_39.setObjectName(_fromUtf8("gridLayout_39"))
        self.access_sql_query_checkBox = QtGui.QCheckBox(self.tab_30)
        self.access_sql_query_checkBox.setObjectName(_fromUtf8("access_sql_query_checkBox"))
        self.gridLayout_39.addWidget(self.access_sql_query_checkBox, 0, 0, 1, 1)
        self.access_sql_query_lineEdit = QtGui.QLineEdit(self.tab_30)
        self.access_sql_query_lineEdit.setObjectName(_fromUtf8("access_sql_query_lineEdit"))
        self.gridLayout_39.addWidget(self.access_sql_query_lineEdit, 0, 1, 1, 1)
        self.access_sqlshell_checkBox = QtGui.QCheckBox(self.tab_30)
        self.access_sqlshell_checkBox.setObjectName(_fromUtf8("access_sqlshell_checkBox"))
        self.gridLayout_39.addWidget(self.access_sqlshell_checkBox, 1, 0, 1, 1)
        self.access_sqlfile_checkBox = QtGui.QCheckBox(self.tab_30)
        self.access_sqlfile_checkBox.setObjectName(_fromUtf8("access_sqlfile_checkBox"))
        self.gridLayout_39.addWidget(self.access_sqlfile_checkBox, 2, 0, 1, 1)
        self.access_sqlfile_lineEdit = QtGui.QLineEdit(self.tab_30)
        self.access_sqlfile_lineEdit.setObjectName(_fromUtf8("access_sqlfile_lineEdit"))
        self.gridLayout_39.addWidget(self.access_sqlfile_lineEdit, 2, 1, 1, 1)
        self.tabWidget_9.addTab(self.tab_30, _fromUtf8(""))
        self.tab_31 = QtGui.QWidget()
        self.tab_31.setObjectName(_fromUtf8("tab_31"))
        self.access_brute_tables_checkBox = QtGui.QCheckBox(self.tab_31)
        self.access_brute_tables_checkBox.setGeometry(QtCore.QRect(10, 10, 141, 20))
        self.access_brute_tables_checkBox.setObjectName(_fromUtf8("access_brute_tables_checkBox"))
        self.brute_columns_checkBox_4 = QtGui.QCheckBox(self.tab_31)
        self.brute_columns_checkBox_4.setGeometry(QtCore.QRect(20, 100, 151, 17))
        self.brute_columns_checkBox_4.setObjectName(_fromUtf8("brute_columns_checkBox_4"))
        self.access_brute_columns_checkBox = QtGui.QCheckBox(self.tab_31)
        self.access_brute_columns_checkBox.setGeometry(QtCore.QRect(10, 40, 151, 17))
        self.access_brute_columns_checkBox.setObjectName(_fromUtf8("access_brute_columns_checkBox"))
        self.tabWidget_9.addTab(self.tab_31, _fromUtf8(""))
        self.tabWidget_23.addTab(self.tab_100, _fromUtf8(""))
        self.tab_101 = QtGui.QWidget()
        self.tab_101.setObjectName(_fromUtf8("tab_101"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_101)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 741, 31))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.access_fingerprint_checkBox = QtGui.QCheckBox(self.groupBox_3)
        self.access_fingerprint_checkBox.setGeometry(QtCore.QRect(10, 10, 281, 17))
        self.access_fingerprint_checkBox.setObjectName(_fromUtf8("access_fingerprint_checkBox"))
        self.tabWidget_23.addTab(self.tab_101, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget_23.setCurrentIndex(0)
        self.tabWidget_9.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.access_columns_checkBox.setText(_translate("Form", "Enumerate DBMS database table columns", None))
        self.access_count_checkBox.setText(_translate("Form", "Retrieve number of entries for table(s)", None))
        self.access_schema_checkBox.setText(_translate("Form", "Enumerate DBMS schema", None))
        self.access_tables_checkBox.setText(_translate("Form", "Enumerate DBMS database tables", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_25), _translate("Form", "Enumeration DB", None))
        self.access_dump_all_checkBox.setText(_translate("Form", "Dump all DBMS databases tables entries", None))
        self.access_dump_checkBox.setText(_translate("Form", "Dump DBMS database table entries", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_27), _translate("Form", "Enumeration entries", None))
        self.access_sql_query_checkBox.setText(_translate("Form", "SQL statement to be executed", None))
        self.access_sqlshell_checkBox.setText(_translate("Form", "Prompt for an interactive SQL shell", None))
        self.access_sqlfile_checkBox.setText(_translate("Form", "Execute SQL statements from given file", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_30), _translate("Form", "Custom", None))
        self.access_brute_tables_checkBox.setText(_translate("Form", "Check of common tables", None))
        self.brute_columns_checkBox_4.setText(_translate("Form", "Check  of common columns", None))
        self.access_brute_columns_checkBox.setText(_translate("Form", "Check  of common columns", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_31), _translate("Form", "Brute force", None))
        self.tabWidget_23.setTabText(self.tabWidget_23.indexOf(self.tab_100), _translate("Form", "Enumeration", None))
        self.access_fingerprint_checkBox.setText(_translate("Form", "Extensive database management system fingerprint", None))
        self.tabWidget_23.setTabText(self.tabWidget_23.indexOf(self.tab_101), _translate("Form", "Fingerprint", None))


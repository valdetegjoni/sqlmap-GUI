# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created: Sun Oct 09 23:27:20 2016
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

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName(_fromUtf8("Preferences"))
        Preferences.setWindowModality(QtCore.Qt.WindowModal)
        Preferences.resize(790, 354)
        self.tabWidget = QtGui.QTabWidget(Preferences)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 771, 281))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab_8)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 10, 581, 171))
        self.groupBox_6.setTitle(_fromUtf8(""))
        self.groupBox_6.setCheckable(False)
        self.groupBox_6.setChecked(False)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.pref_cookie_checkBox = QtGui.QCheckBox(self.groupBox_6)
        self.pref_cookie_checkBox.setGeometry(QtCore.QRect(10, 20, 151, 17))
        self.pref_cookie_checkBox.setAutoExclusive(True)
        self.pref_cookie_checkBox.setObjectName(_fromUtf8("pref_cookie_checkBox"))
        self.pref_cookie_textEdit = QtGui.QTextEdit(self.groupBox_6)
        self.pref_cookie_textEdit.setGeometry(QtCore.QRect(163, 10, 401, 41))
        self.pref_cookie_textEdit.setObjectName(_fromUtf8("pref_cookie_textEdit"))
        self.pref_auth_type_checkBox = QtGui.QCheckBox(self.groupBox_6)
        self.pref_auth_type_checkBox.setGeometry(QtCore.QRect(10, 60, 171, 17))
        self.pref_auth_type_checkBox.setAutoExclusive(True)
        self.pref_auth_type_checkBox.setObjectName(_fromUtf8("pref_auth_type_checkBox"))
        self.pref_auth_type_comboBox = QtGui.QComboBox(self.groupBox_6)
        self.pref_auth_type_comboBox.setGeometry(QtCore.QRect(160, 60, 101, 22))
        self.pref_auth_type_comboBox.setObjectName(_fromUtf8("pref_auth_type_comboBox"))
        self.pref_auth_type_comboBox.addItem(_fromUtf8(""))
        self.pref_auth_type_comboBox.addItem(_fromUtf8(""))
        self.pref_auth_type_comboBox.addItem(_fromUtf8(""))
        self.pref_auth_type_comboBox.addItem(_fromUtf8(""))
        self.pref_auth_cred_lineEdit = QtGui.QLineEdit(self.groupBox_6)
        self.pref_auth_cred_lineEdit.setGeometry(QtCore.QRect(370, 60, 191, 20))
        self.pref_auth_cred_lineEdit.setText(_fromUtf8(""))
        self.pref_auth_cred_lineEdit.setObjectName(_fromUtf8("pref_auth_cred_lineEdit"))
        self.pref_auth_file_checkBox = QtGui.QCheckBox(self.groupBox_6)
        self.pref_auth_file_checkBox.setGeometry(QtCore.QRect(10, 90, 251, 17))
        self.pref_auth_file_checkBox.setAutoExclusive(True)
        self.pref_auth_file_checkBox.setObjectName(_fromUtf8("pref_auth_file_checkBox"))
        self.pref_auth_file_toolButton = QtGui.QToolButton(self.groupBox_6)
        self.pref_auth_file_toolButton.setGeometry(QtCore.QRect(540, 90, 25, 19))
        self.pref_auth_file_toolButton.setText(_fromUtf8(""))
        self.pref_auth_file_toolButton.setObjectName(_fromUtf8("pref_auth_file_toolButton"))
        self.pref_auth_file_lineEdit = QtGui.QLineEdit(self.groupBox_6)
        self.pref_auth_file_lineEdit.setGeometry(QtCore.QRect(282, 90, 251, 20))
        self.pref_auth_file_lineEdit.setObjectName(_fromUtf8("pref_auth_file_lineEdit"))
        self.label = QtGui.QLabel(self.groupBox_6)
        self.label.setGeometry(QtCore.QRect(290, 60, 61, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget.addTab(self.tab_8, _fromUtf8(""))
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_9"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_9)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 10, 721, 171))
        self.groupBox_7.setTitle(_fromUtf8(""))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.pref_proxy_lineEdit = QtGui.QLineEdit(self.groupBox_7)
        self.pref_proxy_lineEdit.setGeometry(QtCore.QRect(280, 20, 421, 20))
        self.pref_proxy_lineEdit.setObjectName(_fromUtf8("pref_proxy_lineEdit"))
        self.pref_proxy_radioButton = QtGui.QRadioButton(self.groupBox_7)
        self.pref_proxy_radioButton.setGeometry(QtCore.QRect(10, 20, 221, 17))
        self.pref_proxy_radioButton.setObjectName(_fromUtf8("pref_proxy_radioButton"))
        self.pref_proxy_cred_checkBox = QtGui.QCheckBox(self.groupBox_7)
        self.pref_proxy_cred_checkBox.setGeometry(QtCore.QRect(10, 50, 261, 17))
        self.pref_proxy_cred_checkBox.setObjectName(_fromUtf8("pref_proxy_cred_checkBox"))
        self.pref_proxy_credentials_lineEdit = QtGui.QLineEdit(self.groupBox_7)
        self.pref_proxy_credentials_lineEdit.setGeometry(QtCore.QRect(280, 50, 421, 20))
        self.pref_proxy_credentials_lineEdit.setObjectName(_fromUtf8("pref_proxy_credentials_lineEdit"))
        self.pref_tor_radioButton = QtGui.QRadioButton(self.groupBox_7)
        self.pref_tor_radioButton.setGeometry(QtCore.QRect(10, 90, 161, 17))
        self.pref_tor_radioButton.setObjectName(_fromUtf8("pref_tor_radioButton"))
        self.pref_tor_port_checkBox = QtGui.QCheckBox(self.groupBox_7)
        self.pref_tor_port_checkBox.setGeometry(QtCore.QRect(260, 90, 131, 17))
        self.pref_tor_port_checkBox.setAutoExclusive(False)
        self.pref_tor_port_checkBox.setObjectName(_fromUtf8("pref_tor_port_checkBox"))
        self.pref_tor_aut_checkBox = QtGui.QCheckBox(self.groupBox_7)
        self.pref_tor_aut_checkBox.setGeometry(QtCore.QRect(140, 90, 121, 17))
        self.pref_tor_aut_checkBox.setCheckable(True)
        self.pref_tor_aut_checkBox.setAutoExclusive(False)
        self.pref_tor_aut_checkBox.setObjectName(_fromUtf8("pref_tor_aut_checkBox"))
        self.pref_tor_type_comboBox = QtGui.QComboBox(self.groupBox_7)
        self.pref_tor_type_comboBox.setGeometry(QtCore.QRect(600, 90, 91, 22))
        self.pref_tor_type_comboBox.setObjectName(_fromUtf8("pref_tor_type_comboBox"))
        self.pref_tor_type_comboBox.addItem(_fromUtf8(""))
        self.pref_tor_type_comboBox.addItem(_fromUtf8(""))
        self.pref_tor_type_comboBox.addItem(_fromUtf8(""))
        self.pref_check_tor_checkBox = QtGui.QCheckBox(self.groupBox_7)
        self.pref_check_tor_checkBox.setGeometry(QtCore.QRect(10, 120, 201, 17))
        self.pref_check_tor_checkBox.setObjectName(_fromUtf8("pref_check_tor_checkBox"))
        self.tor_port_lineEdit = QtGui.QLineEdit(self.groupBox_7)
        self.tor_port_lineEdit.setGeometry(QtCore.QRect(380, 90, 121, 20))
        self.tor_port_lineEdit.setObjectName(_fromUtf8("tor_port_lineEdit"))
        self.label_2 = QtGui.QLabel(self.groupBox_7)
        self.label_2.setGeometry(QtCore.QRect(510, 90, 71, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.tab_9, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 321, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 298, 91))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.timeout_doubleSpinBox = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.timeout_doubleSpinBox.setProperty("value", 30.0)
        self.timeout_doubleSpinBox.setObjectName(_fromUtf8("timeout_doubleSpinBox"))
        self.gridLayout.addWidget(self.timeout_doubleSpinBox, 0, 1, 1, 1)
        self.timeout_checkBox = QtGui.QCheckBox(self.gridLayoutWidget)
        self.timeout_checkBox.setObjectName(_fromUtf8("timeout_checkBox"))
        self.gridLayout.addWidget(self.timeout_checkBox, 0, 0, 1, 1)
        self.retries_spinBox = QtGui.QSpinBox(self.gridLayoutWidget)
        self.retries_spinBox.setProperty("value", 3)
        self.retries_spinBox.setObjectName(_fromUtf8("retries_spinBox"))
        self.gridLayout.addWidget(self.retries_spinBox, 1, 1, 1, 1)
        self.retries_checkBox = QtGui.QCheckBox(self.gridLayoutWidget)
        self.retries_checkBox.setObjectName(_fromUtf8("retries_checkBox"))
        self.gridLayout.addWidget(self.retries_checkBox, 1, 0, 1, 1)
        self.delay_checkBox = QtGui.QCheckBox(self.gridLayoutWidget)
        self.delay_checkBox.setObjectName(_fromUtf8("delay_checkBox"))
        self.gridLayout.addWidget(self.delay_checkBox, 2, 0, 1, 1)
        self.delay_doubleSpinBox = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.delay_doubleSpinBox.setObjectName(_fromUtf8("delay_doubleSpinBox"))
        self.gridLayout.addWidget(self.delay_doubleSpinBox, 2, 1, 1, 1)
        self.groupBox_8 = QtGui.QGroupBox(self.tab)
        self.groupBox_8.setGeometry(QtCore.QRect(350, 10, 381, 121))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.skip_urlencode_checkBox = QtGui.QCheckBox(self.groupBox_8)
        self.skip_urlencode_checkBox.setGeometry(QtCore.QRect(10, 20, 201, 17))
        self.skip_urlencode_checkBox.setObjectName(_fromUtf8("skip_urlencode_checkBox"))
        self.force_ssl_checkBox = QtGui.QCheckBox(self.groupBox_8)
        self.force_ssl_checkBox.setGeometry(QtCore.QRect(10, 50, 161, 17))
        self.force_ssl_checkBox.setObjectName(_fromUtf8("force_ssl_checkBox"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.o_groupBox = QtGui.QGroupBox(self.tab_2)
        self.o_groupBox.setGeometry(QtCore.QRect(10, 10, 341, 121))
        self.o_groupBox.setCheckable(True)
        self.o_groupBox.setChecked(False)
        self.o_groupBox.setObjectName(_fromUtf8("o_groupBox"))
        self.keep_alive_checkBox = QtGui.QCheckBox(self.o_groupBox)
        self.keep_alive_checkBox.setGeometry(QtCore.QRect(10, 30, 201, 17))
        self.keep_alive_checkBox.setTristate(False)
        self.keep_alive_checkBox.setObjectName(_fromUtf8("keep_alive_checkBox"))
        self.null_connection_checkBox = QtGui.QCheckBox(self.o_groupBox)
        self.null_connection_checkBox.setGeometry(QtCore.QRect(10, 60, 301, 17))
        self.null_connection_checkBox.setTristate(False)
        self.null_connection_checkBox.setObjectName(_fromUtf8("null_connection_checkBox"))
        self.threads_checkBox = QtGui.QCheckBox(self.o_groupBox)
        self.threads_checkBox.setGeometry(QtCore.QRect(10, 90, 251, 17))
        self.threads_checkBox.setTristate(False)
        self.threads_checkBox.setObjectName(_fromUtf8("threads_checkBox"))
        self.threads_spinBox = QtGui.QSpinBox(self.o_groupBox)
        self.threads_spinBox.setGeometry(QtCore.QRect(290, 90, 42, 22))
        self.threads_spinBox.setProperty("value", 1)
        self.threads_spinBox.setObjectName(_fromUtf8("threads_spinBox"))
        self.predict_output_checkBox = QtGui.QCheckBox(self.tab_2)
        self.predict_output_checkBox.setGeometry(QtCore.QRect(20, 160, 181, 17))
        self.predict_output_checkBox.setObjectName(_fromUtf8("predict_output_checkBox"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_10 = QtGui.QWidget()
        self.tab_10.setObjectName(_fromUtf8("tab_10"))
        self.groupBox_9 = QtGui.QGroupBox(self.tab_10)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 9, 371, 191))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_9)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.invalid_string_checkBox = QtGui.QCheckBox(self.groupBox_9)
        self.invalid_string_checkBox.setObjectName(_fromUtf8("invalid_string_checkBox"))
        self.gridLayout_2.addWidget(self.invalid_string_checkBox, 2, 0, 1, 1)
        self.invalid_logical_checkBox = QtGui.QCheckBox(self.groupBox_9)
        self.invalid_logical_checkBox.setObjectName(_fromUtf8("invalid_logical_checkBox"))
        self.gridLayout_2.addWidget(self.invalid_logical_checkBox, 1, 0, 1, 1)
        self.invalid_bignum_checkBox = QtGui.QCheckBox(self.groupBox_9)
        self.invalid_bignum_checkBox.setObjectName(_fromUtf8("invalid_bignum_checkBox"))
        self.gridLayout_2.addWidget(self.invalid_bignum_checkBox, 0, 0, 1, 1)
        self.no_escape_checkBox = QtGui.QCheckBox(self.groupBox_9)
        self.no_escape_checkBox.setObjectName(_fromUtf8("no_escape_checkBox"))
        self.gridLayout_2.addWidget(self.no_escape_checkBox, 3, 0, 1, 1)
        self.no_cast_checkBox = QtGui.QCheckBox(self.groupBox_9)
        self.no_cast_checkBox.setObjectName(_fromUtf8("no_cast_checkBox"))
        self.gridLayout_2.addWidget(self.no_cast_checkBox, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab_10, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 291, 131))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.level_checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.level_checkBox.setGeometry(QtCore.QRect(20, 20, 151, 17))
        self.level_checkBox.setChecked(False)
        self.level_checkBox.setObjectName(_fromUtf8("level_checkBox"))
        self.level_spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.level_spinBox.setGeometry(QtCore.QRect(190, 20, 42, 22))
        self.level_spinBox.setMinimum(1)
        self.level_spinBox.setMaximum(5)
        self.level_spinBox.setProperty("value", 3)
        self.level_spinBox.setObjectName(_fromUtf8("level_spinBox"))
        self.risk_checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.risk_checkBox.setGeometry(QtCore.QRect(20, 50, 141, 17))
        self.risk_checkBox.setChecked(False)
        self.risk_checkBox.setObjectName(_fromUtf8("risk_checkBox"))
        self.risk_spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.risk_spinBox.setGeometry(QtCore.QRect(190, 50, 42, 22))
        self.risk_spinBox.setMaximum(3)
        self.risk_spinBox.setProperty("value", 3)
        self.risk_spinBox.setObjectName(_fromUtf8("risk_spinBox"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.groupBox_11 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_11.setGeometry(QtCore.QRect(10, 30, 292, 101))
        self.groupBox_11.setTitle(_fromUtf8(""))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_11)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.technique_checkBox = QtGui.QCheckBox(self.groupBox_11)
        self.technique_checkBox.setChecked(False)
        self.technique_checkBox.setObjectName(_fromUtf8("technique_checkBox"))
        self.gridLayout_3.addWidget(self.technique_checkBox, 0, 0, 1, 1)
        self.technique_comboBox = QtGui.QComboBox(self.groupBox_11)
        self.technique_comboBox.setEditable(True)
        self.technique_comboBox.setObjectName(_fromUtf8("technique_comboBox"))
        self.technique_comboBox.addItem(_fromUtf8(""))
        self.technique_comboBox.addItem(_fromUtf8(""))
        self.technique_comboBox.addItem(_fromUtf8(""))
        self.technique_comboBox.addItem(_fromUtf8(""))
        self.technique_comboBox.addItem(_fromUtf8(""))
        self.technique_comboBox.addItem(_fromUtf8(""))
        self.technique_comboBox.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.technique_comboBox, 0, 1, 1, 1)
        self.time_sec_checkBox = QtGui.QCheckBox(self.groupBox_11)
        self.time_sec_checkBox.setObjectName(_fromUtf8("time_sec_checkBox"))
        self.gridLayout_3.addWidget(self.time_sec_checkBox, 1, 0, 1, 1)
        self.time_sec_doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_11)
        self.time_sec_doubleSpinBox.setDecimals(1)
        self.time_sec_doubleSpinBox.setProperty("value", 5.0)
        self.time_sec_doubleSpinBox.setObjectName(_fromUtf8("time_sec_doubleSpinBox"))
        self.gridLayout_3.addWidget(self.time_sec_doubleSpinBox, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_5)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 611, 241))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.dump_format_comboBox = QtGui.QComboBox(self.groupBox_3)
        self.dump_format_comboBox.setObjectName(_fromUtf8("dump_format_comboBox"))
        self.dump_format_comboBox.addItem(_fromUtf8(""))
        self.dump_format_comboBox.addItem(_fromUtf8(""))
        self.dump_format_comboBox.addItem(_fromUtf8(""))
        self.gridLayout_4.addWidget(self.dump_format_comboBox, 2, 1, 1, 1)
        self.output_dir_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.output_dir_lineEdit.setText(_fromUtf8(""))
        self.output_dir_lineEdit.setObjectName(_fromUtf8("output_dir_lineEdit"))
        self.gridLayout_4.addWidget(self.output_dir_lineEdit, 3, 1, 1, 1)
        self.save_ini_checkBox = QtGui.QCheckBox(self.groupBox_3)
        self.save_ini_checkBox.setChecked(False)
        self.save_ini_checkBox.setObjectName(_fromUtf8("save_ini_checkBox"))
        self.gridLayout_4.addWidget(self.save_ini_checkBox, 5, 0, 1, 1)
        self.output_dir_checkBox = QtGui.QCheckBox(self.groupBox_3)
        self.output_dir_checkBox.setChecked(False)
        self.output_dir_checkBox.setObjectName(_fromUtf8("output_dir_checkBox"))
        self.gridLayout_4.addWidget(self.output_dir_checkBox, 3, 0, 1, 1)
        self.parse_errors_checkBox = QtGui.QCheckBox(self.groupBox_3)
        self.parse_errors_checkBox.setChecked(False)
        self.parse_errors_checkBox.setObjectName(_fromUtf8("parse_errors_checkBox"))
        self.gridLayout_4.addWidget(self.parse_errors_checkBox, 4, 0, 1, 2)
        self.save_ini_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.save_ini_lineEdit.setObjectName(_fromUtf8("save_ini_lineEdit"))
        self.gridLayout_4.addWidget(self.save_ini_lineEdit, 5, 1, 1, 1)
        self.trafficfile_checkBox = QtGui.QCheckBox(self.groupBox_3)
        self.trafficfile_checkBox.setObjectName(_fromUtf8("trafficfile_checkBox"))
        self.gridLayout_4.addWidget(self.trafficfile_checkBox, 0, 0, 1, 1)
        self.traffic_file_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.traffic_file_lineEdit.setObjectName(_fromUtf8("traffic_file_lineEdit"))
        self.gridLayout_4.addWidget(self.traffic_file_lineEdit, 0, 1, 1, 1)
        self.batch_checkBox = QtGui.QCheckBox(self.groupBox_3)
        self.batch_checkBox.setChecked(False)
        self.batch_checkBox.setObjectName(_fromUtf8("batch_checkBox"))
        self.gridLayout_4.addWidget(self.batch_checkBox, 1, 0, 1, 2)
        self.dump_format_checkBox = QtGui.QCheckBox(self.groupBox_3)
        self.dump_format_checkBox.setObjectName(_fromUtf8("dump_format_checkBox"))
        self.gridLayout_4.addWidget(self.dump_format_checkBox, 2, 0, 1, 1)
        self.eta_checkBox = QtGui.QCheckBox(self.groupBox_3)
        self.eta_checkBox.setObjectName(_fromUtf8("eta_checkBox"))
        self.gridLayout_4.addWidget(self.eta_checkBox, 6, 0, 1, 2)
        self.trafficfile_toolButton = QtGui.QToolButton(self.groupBox_3)
        self.trafficfile_toolButton.setText(_fromUtf8(""))
        self.trafficfile_toolButton.setObjectName(_fromUtf8("trafficfile_toolButton"))
        self.gridLayout_4.addWidget(self.trafficfile_toolButton, 0, 2, 1, 1)
        self.output_dir_toolButton = QtGui.QToolButton(self.groupBox_3)
        self.output_dir_toolButton.setText(_fromUtf8(""))
        self.output_dir_toolButton.setObjectName(_fromUtf8("output_dir_toolButton"))
        self.gridLayout_4.addWidget(self.output_dir_toolButton, 3, 2, 1, 1)
        self.save_ini_toolButton = QtGui.QToolButton(self.groupBox_3)
        self.save_ini_toolButton.setText(_fromUtf8(""))
        self.save_ini_toolButton.setObjectName(_fromUtf8("save_ini_toolButton"))
        self.gridLayout_4.addWidget(self.save_ini_toolButton, 5, 2, 1, 1)
        self.hex_checkBox = QtGui.QCheckBox(self.groupBox_3)
        self.hex_checkBox.setObjectName(_fromUtf8("hex_checkBox"))
        self.gridLayout_4.addWidget(self.hex_checkBox, 8, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_6)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 341, 201))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.beep_checkBox = QtGui.QCheckBox(self.groupBox_4)
        self.beep_checkBox.setObjectName(_fromUtf8("beep_checkBox"))
        self.gridLayout_6.addWidget(self.beep_checkBox, 0, 0, 1, 1)
        self.cleanup_checkBox = QtGui.QCheckBox(self.groupBox_4)
        self.cleanup_checkBox.setObjectName(_fromUtf8("cleanup_checkBox"))
        self.gridLayout_6.addWidget(self.cleanup_checkBox, 1, 0, 1, 1)
        self.purge_output_checkBox = QtGui.QCheckBox(self.groupBox_4)
        self.purge_output_checkBox.setObjectName(_fromUtf8("purge_output_checkBox"))
        self.gridLayout_6.addWidget(self.purge_output_checkBox, 3, 0, 1, 1)
        self.dependencies_checkBox = QtGui.QCheckBox(self.groupBox_4)
        self.dependencies_checkBox.setObjectName(_fromUtf8("dependencies_checkBox"))
        self.gridLayout_6.addWidget(self.dependencies_checkBox, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_7)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 281, 141))
        self.groupBox_5.setTitle(_fromUtf8(""))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verbosity_checkBox = QtGui.QCheckBox(self.groupBox_5)
        self.verbosity_checkBox.setGeometry(QtCore.QRect(10, 30, 111, 17))
        self.verbosity_checkBox.setChecked(False)
        self.verbosity_checkBox.setObjectName(_fromUtf8("verbosity_checkBox"))
        self.verbosity_spinBox = QtGui.QSpinBox(self.groupBox_5)
        self.verbosity_spinBox.setGeometry(QtCore.QRect(160, 30, 42, 22))
        self.verbosity_spinBox.setMaximum(6)
        self.verbosity_spinBox.setProperty("value", 3)
        self.verbosity_spinBox.setObjectName(_fromUtf8("verbosity_spinBox"))
        self.tabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.preferences_discard_pushButton = QtGui.QPushButton(Preferences)
        self.preferences_discard_pushButton.setGeometry(QtCore.QRect(610, 310, 75, 23))
        self.preferences_discard_pushButton.setObjectName(_fromUtf8("preferences_discard_pushButton"))
        self.preferences_save_pushButton = QtGui.QPushButton(Preferences)
        self.preferences_save_pushButton.setGeometry(QtCore.QRect(510, 310, 75, 23))
        self.preferences_save_pushButton.setObjectName(_fromUtf8("preferences_save_pushButton"))
        self.actionShowDialogBox = QtGui.QAction(Preferences)
        self.actionShowDialogBox.setObjectName(_fromUtf8("actionShowDialogBox"))

        self.retranslateUi(Preferences)
        self.tabWidget.setCurrentIndex(7)
        self.pref_tor_type_comboBox.setCurrentIndex(0)
        QtCore.QObject.connect(self.keep_alive_checkBox, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionShowDialogBox.trigger)
        QtCore.QObject.connect(self.predict_output_checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.threads_checkBox.setDisabled)
        QtCore.QObject.connect(self.null_connection_checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.actionShowDialogBox.setDisabled)
        QtCore.QObject.connect(self.pref_tor_aut_checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pref_tor_port_checkBox.setDisabled)
        QtCore.QObject.connect(self.threads_checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.predict_output_checkBox.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(Preferences)

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(_translate("Preferences", "Preferences", None))
        self.pref_cookie_checkBox.setText(_translate("Preferences", "Setting an HTTP cookie", None))
        self.pref_auth_type_checkBox.setText(_translate("Preferences", "HTTP authentication type", None))
        self.pref_auth_type_comboBox.setItemText(0, _translate("Preferences", "Basic", None))
        self.pref_auth_type_comboBox.setItemText(1, _translate("Preferences", "Digest", None))
        self.pref_auth_type_comboBox.setItemText(2, _translate("Preferences", "NTML", None))
        self.pref_auth_type_comboBox.setItemText(3, _translate("Preferences", "PKI", None))
        self.pref_auth_cred_lineEdit.setPlaceholderText(_translate("Preferences", "username:password", None))
        self.pref_auth_file_checkBox.setText(_translate("Preferences", "HTTP authentication PEM cert/private key file", None))
        self.label.setText(_translate("Preferences", "Credentials", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("Preferences", "Authentication", None))
        self.pref_proxy_radioButton.setText(_translate("Preferences", "Use a proxy to connect to the target URL", None))
        self.pref_proxy_cred_checkBox.setText(_translate("Preferences", "Proxy authentication credentials ", None))
        self.pref_proxy_credentials_lineEdit.setPlaceholderText(_translate("Preferences", "name:password", None))
        self.pref_tor_radioButton.setText(_translate("Preferences", "Tor anonymity network", None))
        self.pref_tor_port_checkBox.setText(_translate("Preferences", "Manually set Tor port", None))
        self.pref_tor_aut_checkBox.setText(_translate("Preferences", "Automatically set Tor ", None))
        self.pref_tor_type_comboBox.setItemText(0, _translate("Preferences", "HTTP ", None))
        self.pref_tor_type_comboBox.setItemText(1, _translate("Preferences", "SOCKS4", None))
        self.pref_tor_type_comboBox.setItemText(2, _translate("Preferences", "SOCKS5", None))
        self.pref_check_tor_checkBox.setText(_translate("Preferences", "Check to see if Tor is used properly", None))
        self.label_2.setText(_translate("Preferences", "Tor proxy type", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("Preferences", "Proxy/Tor", None))
        self.groupBox.setTitle(_translate("Preferences", "Deafult values", None))
        self.timeout_checkBox.setText(_translate("Preferences", "Seconds to wait before timeout connection", None))
        self.retries_checkBox.setText(_translate("Preferences", "Retries when the connection timeouts", None))
        self.delay_checkBox.setText(_translate("Preferences", "Delay in seconds between each HTTP request", None))
        self.groupBox_8.setTitle(_translate("Preferences", "Further options", None))
        self.skip_urlencode_checkBox.setText(_translate("Preferences", "Skip URL encoding of payload data", None))
        self.force_ssl_checkBox.setText(_translate("Preferences", "Force usage of SSL/HTTPS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Preferences", "Request", None))
        self.o_groupBox.setTitle(_translate("Preferences", "Bundle optimization", None))
        self.keep_alive_checkBox.setText(_translate("Preferences", "Use persistent HTTP(s) connections", None))
        self.null_connection_checkBox.setText(_translate("Preferences", "Retrieve page length without actual HTTP response body", None))
        self.threads_checkBox.setText(_translate("Preferences", "Max number of concurrent HTTP(s) requests", None))
        self.predict_output_checkBox.setText(_translate("Preferences", "Predict common queries output", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Preferences", "Optimization", None))
        self.groupBox_9.setTitle(_translate("Preferences", "These options can be used to specify which parameters to test for", None))
        self.invalid_string_checkBox.setText(_translate("Preferences", "Use random strings for invalidating values", None))
        self.invalid_logical_checkBox.setText(_translate("Preferences", "Use logical operations for invalidating values", None))
        self.invalid_bignum_checkBox.setText(_translate("Preferences", "Use big numbers for invalidating values", None))
        self.no_escape_checkBox.setText(_translate("Preferences", "Turn off string escaping mechanism", None))
        self.no_cast_checkBox.setText(_translate("Preferences", "Turn off payload casting mechanism", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("Preferences", "Injection", None))
        self.level_checkBox.setText(_translate("Preferences", "Level of tests to perform", None))
        self.risk_checkBox.setText(_translate("Preferences", "Risk of tests to perform", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Preferences", "Detection", None))
        self.technique_checkBox.setText(_translate("Preferences", "SQL injection techniques to use", None))
        self.technique_comboBox.setItemText(0, _translate("Preferences", "BEUSTQ", None))
        self.technique_comboBox.setItemText(1, _translate("Preferences", "B", None))
        self.technique_comboBox.setItemText(2, _translate("Preferences", "E", None))
        self.technique_comboBox.setItemText(3, _translate("Preferences", "U", None))
        self.technique_comboBox.setItemText(4, _translate("Preferences", "S", None))
        self.technique_comboBox.setItemText(5, _translate("Preferences", "T", None))
        self.technique_comboBox.setItemText(6, _translate("Preferences", "Q", None))
        self.time_sec_checkBox.setText(_translate("Preferences", "Seconds to delay the DBMS response", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Preferences", "Techniques", None))
        self.dump_format_comboBox.setItemText(0, _translate("Preferences", "CSV", None))
        self.dump_format_comboBox.setItemText(1, _translate("Preferences", "HTML", None))
        self.dump_format_comboBox.setItemText(2, _translate("Preferences", "SQLITE", None))
        self.output_dir_lineEdit.setPlaceholderText(_translate("Preferences", "sqlmap/output", None))
        self.save_ini_checkBox.setText(_translate("Preferences", "Save options to a configuration INI file", None))
        self.output_dir_checkBox.setText(_translate("Preferences", "Custom output directory path", None))
        self.parse_errors_checkBox.setText(_translate("Preferences", "Parse and display DBMS error messages from responses", None))
        self.save_ini_lineEdit.setText(_translate("Preferences", "sqlmap/INI-file/options.ini", None))
        self.trafficfile_checkBox.setText(_translate("Preferences", "Log all HTTP traffic into a textual file", None))
        self.batch_checkBox.setText(_translate("Preferences", "Never ask for user input, use the default behaviour", None))
        self.dump_format_checkBox.setText(_translate("Preferences", "Format of dumped data ", None))
        self.eta_checkBox.setText(_translate("Preferences", "Display for each output the estimated time of arrival", None))
        self.hex_checkBox.setText(_translate("Preferences", "Use DBMS hex function(s) for data retrieval", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Preferences", "General", None))
        self.beep_checkBox.setText(_translate("Preferences", "Beep on question and/or when SQL injection is found", None))
        self.cleanup_checkBox.setText(_translate("Preferences", "Clean up the DBMS from sqlmap specific UDF and tables", None))
        self.purge_output_checkBox.setText(_translate("Preferences", "Safely remove all content from output directory", None))
        self.dependencies_checkBox.setText(_translate("Preferences", "Check for missing (non-core) sqlmap dependencies", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Preferences", "Miscellaneous", None))
        self.verbosity_checkBox.setText(_translate("Preferences", "Verbosity level", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Preferences", "Verbosity", None))
        self.preferences_discard_pushButton.setText(_translate("Preferences", "Discard", None))
        self.preferences_save_pushButton.setText(_translate("Preferences", "Save", None))
        self.actionShowDialogBox.setText(_translate("Preferences", "showDialogBox", None))


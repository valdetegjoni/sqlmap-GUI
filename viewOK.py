#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
import sys
import os
import subprocess
import signal
import psutil
from ui.access import Ui_FormAccess
from ui.advancedhelp import Ui_advancedhelp
from ui.custominj import Ui_FormCustom
from ui.db2 import Ui_FormDB2
from ui.detection import Ui_Detection
from ui.direct import Ui_FormDirect
from ui.enumeration import Ui_FormEnumeration
from ui.firebird import Ui_FormFirebird
from ui.fsaccess import Ui_FormFSA
from ui.hsqldb import Ui_FormHsqldb
from ui.main import Ui_MainWindow
from ui.mssqlenum import Ui_FormMssEnum
from ui.mssqlfing import Ui_FormMssFing
from ui.mssqlfsa import Ui_FormMssFsa
from ui.mssqlostake import Ui_FormMssOSTake
from ui.mssqlserver import Ui_FormMssqlserver
from ui.mysql import Ui_FormMysql
from ui.openlog import Ui_OpenLog
from ui.oracle import Ui_FormOracle
from ui.ostakeover import Ui_FormOSTakeover
from ui.popup import Ui_popup
from ui.postgresql import Ui_FormPostgreSql
from ui.preferences import Ui_Preferences
from ui.sqlite import Ui_FormSqlite
from ui.sybase import Ui_FormSybase
from ui.postgresql import Ui_FormPostgreSql
from ui.udfi import Ui_FormUDFI

class MyApp(QtGui.QMainWindow):
	def __init__(self, parent=None):
		super(MyApp, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.startOnce() 
		self.command = ""
		self.od=""
		self.pushB=""
		self.directOpt=""
		self.dbms=""
		self.detectionOpt=""
		self.prefOpt = ""
		self.enumOpt=""
		self.fsaOpt=""
		self.udfiOpt=""
		self.takeoverOpt=""
		self.customOpt=""
		self.accessOpt = ""
		self.db2Opt = ""
		self.firebirdOpt= ""
		self.hsqldbOpt = ""
		self.mssqlserverOpt = ""
		self.dmp_format = "CSV"
		
	#	self.process = QtCore.QProcess(self)
		self.intero = ""

	def startOnce(self):
		print "startOnce"
		# Detection - Exploitation 
		widgetDetection = QtGui.QWidget(self.ui.detection_tab)
		self.subDetection = Ui_Detection()
		self.subDetection.setupUi(widgetDetection)
		# Direct connection
		self.widgetDirect = QtGui.QWidget(self.ui.direct_tab)
		self.subDirect = Ui_FormDirect()
		self.subDirect.setupUi(self.widgetDirect)
		
		#Menu/settings/preferences
		self.widget = QtGui.QDialog()
		self.pref = Ui_Preferences()
		self.pref.setupUi(self.widget)
		#Menu/File/Open Log
		self.widgetLog = QtGui.QDialog()
		self.openlog = Ui_OpenLog()
		self.openlog.setupUi(self.widgetLog)

		#Menu/Help
		self.widgethelp = QtGui.QDialog()
		self.help = Ui_advancedhelp()
		self.help.setupUi(self.widgethelp)
		
		self.widgetpopup = QtGui.QDialog()
		self.popup = Ui_popup()
		self.popup.setupUi(self.widgetpopup)
		#self.setDefaultIndexes()
		self.connectButtons()

	
	def connectButtons(self):
		self.ui.menuSettings.triggered[QtGui.QAction].connect(self.add_preferences)
		self.ui.run_pushButton.clicked.connect(self.startSqlmap)
		self.ui.stop_pushButton.clicked.connect( self.stopSqlmap)
		self.pref.output_dir_toolButton.clicked.connect(lambda : self.openDir(self.pref.output_dir_lineEdit))
		QtCore.QObject.connect(self.openlog.pushButton_open,QtCore.SIGNAL("clicked()"), self.file_dialog)
		QtCore.QObject.connect(self.openlog.pushButton_save,QtCore.SIGNAL("clicked()"), self.file_save)
		self.ui.menuFile.connect(self.ui.actionOpen_log_2, QtCore.SIGNAL("triggered()"), self.openLog)
		self.ui.menuFile.connect(self.ui.actionSave_options, QtCore.SIGNAL("triggered()"), self.saveOptions)
		self.ui.menuFile.connect(self.ui.actionLoad_options,QtCore.SIGNAL("triggered()"),self.loadOptions) 
		self.ui.menuFile.connect(self.ui.actionExit,QtCore.SIGNAL("triggered()"),self.close) 
		self.ui.menuHelp.connect(self.ui.actionShow_advanced_help_message,QtCore.SIGNAL("triggered()"),self.showhelp) 
		self.ui.toolBar.connect(self.ui.actionOpen_log, QtCore.SIGNAL("triggered()"), self.openLog)
		self.subDirect.direct_save_pushButton.clicked.connect(self.savedirectOptions)
		self.subDirect.direct_discard_pushButton.clicked.connect(self.discarddirectOptions)
		self.subDirect.access_toolButton.clicked.connect(lambda : self.accessOptions(self.subDirect.scrollArea)) 
		self.subDirect.db2_toolButton.clicked.connect(lambda : self.db2Options(self.subDirect.scrollArea))
		self.subDirect.firebird_toolButton.clicked.connect(lambda :self.firebirdOptions(self.subDirect.scrollArea))
		self.subDirect.hsqldb_toolButton.clicked.connect(lambda :self.hsqldbOptions(self.subDirect.scrollArea))
		self.subDirect.mssqlserver_toolButton.clicked.connect(lambda :self.mssqlserverOptions(self.subDirect.scrollArea))
		self.subDirect.mysql_toolButton.clicked.connect(lambda :self.mysqlOptions(self.subDirect.scrollArea))
		self.subDirect.oracle_toolButton.clicked.connect(lambda :self.oracleOptions(self.subDirect.scrollArea))
		self.subDirect.postgresql_toolButton.clicked.connect(lambda :self.postgresqlOptions(self.subDirect.scrollArea))
		self.subDirect.sqlite_toolButton.clicked.connect(lambda :self.sqliteOptions(self.subDirect.scrollArea))
		self.subDirect.sybase_toolButton.clicked.connect(lambda :self.sybaseOptions(self.subDirect.scrollArea))
		self.subDetection.detection_save_pushButton.clicked.connect(self.savedetectionOptions)
		self.subDetection.detection_discard_pushButton.clicked.connect(self.discarddetectionOptions)
		self.subDetection.enumeration_checkBox.clicked.connect(lambda : self.enumerationOptions(self.subDetection.scrollArea))
		self.subDetection.file_system_access_checkBox.clicked.connect(lambda : self.fsaOptions(self.subDetection.scrollArea))
		self.subDetection.takeover_checkBox.clicked.connect(lambda : self.takeoverOptions(self.subDetection.scrollArea))
		self.subDetection.UDFI_checkBox.clicked.connect(lambda : self.UDFIOptions(self.subDetection.scrollArea))
		self.subDetection.custom_injection_checkBox.clicked.connect(lambda : self.customInjectionOptions(self.subDetection.scrollArea))
		self.subDetection.requestfile_toolButton.clicked.connect(lambda : self.openDir(self.subDetection.requestfile_lineEdit))
		self.subDetection.tamper_toolButton.clicked.connect(lambda : self.openDir(self.subDetection.tamper_lineEdit))
		self.subDetection.output_dir_toolButton.clicked.connect(lambda : self.openDir(self.subDetection.output_dir_lineEdit))
		

	def o(self):
		print "close the window"
		self.widget.close()
	
#	def startSqlmap(self):
	# prende la riga di options/switches e la passa ad sqlmap.py 
	def stopSqlmap(self):
		print "stop "
		self.process.kill()
		
	def onstart (self):
		self.ui.stop_pushButton.setEnabled(True)     
		self.ui.run_pushButton.setEnabled(False)
		print "Started\n"

	def onfinish (self):
		self.ui.stop_pushButton.setEnabled(False)     
		self.ui.run_pushButton.setEnabled(True)
		self.process.deleteLater()
		self.hidepopup()
		print "Finish running\n"		
	
	def startSqlmap(self):
		if self.ui.command_lineEdit.text().isEmpty():
			self.showdialog("Enter the desired options please !")
		else :
			self.ui.csv_plainTextEdit.clear()
			self.ui.html_plainTextEdit.clear()
			self.ui.sqlite_plainTextEdit.clear()

			self.process = QtCore.QProcess(self)
			self.ui.run_pushButton.setEnabled(False) # call it first because 
                                     # processes are not started instantly
			self.process.setProcessChannelMode(self.process.MergedChannels)
			self.process.started.connect(self.onstart) # connect "start" signal
			self.process.finished.connect(self.onfinish)
			self.process.readyReadStandardOutput.connect(self.stdoutReady)
			self.process.readyReadStandardError.connect(self.stderrReady)

			commandSqlMap = self.ui.command_lineEdit.text()

			command = str(commandSqlMap)
			argv ="python sqlmap.py" + " " + command
			print	argv
			self.process.start(argv,  QtCore.QProcess.ReadWrite);
			chioce = "Y"
			self.popup.lineEdit.setText(chioce)

			while self.process.pid() > 0  :
					self.showpopup()
					stri = str(self.popup.lineEdit.text())
					if stri.isdigit()== True:
						dig= int(stri)
						self.process.write('%d\n'%dig )
					else :
						self.process.write('% s \n' % stri) 
					self.process.closeWriteChannel()
					
			print "process end"
	
	
	def append(self, text):
		cursor = self.ui.plainTextEdit.textCursor()
		cursor.movePosition(cursor.End)
		cursor.insertText(text)
	
	def appendformat(self,text):
		if self.dmp_format == 'CSV':
			cursor = self.ui.csv_plainTextEdit.textCursor()
		elif self.dmp_format == 'HTML':
			cursor = self.ui.html_plainTextEdit.textCursor()
		elif self.dmp_format == 'SQLITE':
			cursor = self.ui.sqlite_plainTextEdit.textCursor()
		cursor.movePosition(cursor.End)
		cursor.insertText(text)
	
	def appendError(self, text):
		cursor = self.ui.error_plainTextEdit.textCursor()
		cursor.movePosition(cursor.End)
		cursor.insertText(text)

	def stdoutReady(self):
		text = str(self.process.readAllStandardOutput())
		print "RIGA : " +text.strip()
		self.append(text)
		if self.dmp_format !='':
			self.appendformat(text)

	def stderrReady(self):
		text = str(self.process.readAllStandardError())
		print text.strip()
		self.appendError(text)

		
	def showhelp(self):
		self.widgethelp.exec_()		

	def showpopup(self):
		self.widgetpopup.exec_()		
	
	def hidepopup(self):
		self.widgetpopup.done(1)
		
	def saveOptions(self):
		if self.ui.command_lineEdit.text().isEmpty():
			self.showdialog("No options to save!")
		else :
			commandSqlMap = self.ui.command_lineEdit.text()
			sopt = QtGui.QFileDialog(self)
			self.filenameopt = sopt.getOpenFileName()
			from os.path import isfile
			if isfile(self.filenameopt):
				import codecs
				s = codecs.open(self.filenameopt,'w','utf-8')
				s.write(unicode(commandSqlMap))
				s.close()

	def loadOptions(self):
		sopt = QtGui.QFileDialog(self)
		self.filenameopt = sopt.getOpenFileName()
		from os.path import isfile
		if isfile(self.filenameopt):
			import codecs
			s = codecs.open(self.filenameopt,'r','utf-8').read()
			self.ui.command_lineEdit.setText(s)
	
	def discardprefOptions(self):
		self.prefOpt = ""
		self.widget.close()
		self.pref.setupUi(self.widget)
		return self.prefOpt
	
	def saveprefOptions(self):
		#Menu/settings/preferences
		self.prefOpt = ""
		if self.pref.pref_cookie_checkBox.isChecked():	
			if self.pref.pref_cookie_textEdit.toPlainText().isEmpty() == False:
				self.prefOpt = " " + "--cookie="+self.pref.pref_cookie_textEdit.toPlainText()
			else :
				self.showdialog("Enter cookie value on authentication via cookie please!")
		elif self.pref.pref_auth_type_checkBox.isChecked():
			if self.pref.pref_auth_cred_lineEdit.text().isEmpty() == False:
					http_authentication_type = str(self.pref.pref_auth_type_comboBox.currentText())
					http_authentication_cred = self.pref.pref_auth_cred_lineEdit.text()
					self.prefOpt = self.prefOpt +" "+ " --auth-type="+http_authentication_type+ "  "+ " --auth-cred=" + http_authentication_cred 
			else :
				self.showdialog("Enter HTTP authentication credentials (name:password) please!")
		elif self.pref.pref_auth_file_checkBox.isChecked(): 
			if self.pref.pref_auth_file_lineEdit.text().isEmpty() == False:
					self.prefOpt = self.prefOpt +" "+ "--auth-file="+ self.pref.pref_auth_file_lineEdit.text()
			else :
				self.showdialog("Enter HTTP authentication PEM cert/private key file please!")
		if self.pref.pref_proxy_radioButton.isChecked():	
			if self.pref.pref_proxy_lineEdit.text().isEmpty() == False:
				self.prefOpt = self.prefOpt +" "+ "--proxy="+self.pref.pref_proxy_lineEdit.text()
			if self.pref.pref_proxy_cred_checkBox.isChecked():
				if self.pref.pref_proxy_credentials_lineEdit.text().isEmpty() == False:
					self.prefOpt = self.prefOpt +" "+"--proxy-cred="+ self.pref.pref_proxy_credentials_lineEdit.text()
		elif self.pref.pref_tor_radioButton.isChecked():	
			if self.pref.pref_tor_aut_checkBox.isChecked():
				self.prefOpt = self.prefOpt +" "+ "--tor "
			if self.pref.pref_tor_port_checkBox.isChecked():
				if self.pref.tor_port_lineEdit.text().isEmpty() == False:
					tor_port = self.pref.tor_port_lineEdit.text()
					self.prefOpt = self.prefOpt + " "+ "--tor-port="+ tor_port +" "+ "--tor-type="+ str(self.pref.pref_tor_type_comboBox.currentText())
				else :
					self.showdialog("Set Tor proxy port other than default please!")#this is not necessary
			if self.pref.pref_check_tor_checkBox.isChecked():
				self.prefOpt = self.prefOpt + " "+ "--check-tor "			 
		if self.pref.timeout_checkBox.isChecked():
			timeout = str(self.pref.timeout_doubleSpinBox.value())
			self.prefOpt = self.prefOpt + " "+"--timeout="+timeout
#			optDict["Request"][timeout] = self.pref.timeout_doubleSpinBox.value()
			#optDict[timeout].append(self.pref.timeout_doubleSpinBox.value())
		if self.pref.retries_checkBox.isChecked():
			retries = str(self.pref.retries_spinBox.value())
			self.prefOpt = self.prefOpt + " "+"--retries="+retries
		if self.pref.delay_checkBox.isChecked():
			delay = str(self.pref.delay_doubleSpinBox.value())
			self.prefOpt = self.prefOpt + " "+"--delay="+delay
		if self.pref.skip_urlencode_checkBox.isChecked():
			self.prefOpt = self.prefOpt + " "+"--skip-urlencode "
		if self.pref.force_ssl_checkBox.isChecked():
			self.prefOpt = self.prefOpt + " "+"--force-ssl "
		if self.pref.keep_alive_checkBox.isChecked():
			self.prefOpt = self.prefOpt + " "+"--keep-alive "
		if self.pref.null_connection_checkBox.isChecked():
			self.prefOpt = self.prefOpt + " "+"--null-connection "
		if self.pref.threads_checkBox.isChecked():
			threads = str(self.pref.threads_spinBox.value())
			self.prefOpt = self.prefOpt + " "+"--threads="+threads
		elif self.pref.predict_output_checkBox.isChecked():
			self.prefOpt = self.prefOpt + " "+"--predict-output"
		if self.pref.invalid_bignum_checkBox.isChecked():
			self.prefOpt = self.prefOpt + " "+"--invalid-bignum"
		if self.pref.invalid_logical_checkBox.isChecked():
			self.prefOpt = self.prefOpt + " "+"--invalid-logical"
		if self.pref.invalid_string_checkBox.isChecked():
			self.prefOpt = self.prefOpt + " "+"--invalid-string"
		if self.pref.no_escape_checkBox.isChecked():
			self.prefOpt = self.prefOpt + " "+"--no-escape"
		if self.pref.no_cast_checkBox.isChecked():
			self.prefOpt = self.prefOpt + " "+"--no-cast"
		if self.pref.level_checkBox.isChecked():
			level = str(self.pref.level_spinBox.value())
			self.prefOpt = self.prefOpt + " "+"--level="+level
		if self.pref.risk_checkBox.isChecked():
			risk = str(self.pref.risk_spinBox.value())
			self.prefOpt = self.prefOpt + " "+"--risk="+risk
		if self.pref.technique_checkBox.isChecked():
			technique = str(self.pref.technique_comboBox.currentText())
			self.prefOpt = self.prefOpt + " "+"--technique="+technique
		if self.pref.time_sec_checkBox.isChecked():
			time_sec = str(self.pref.time_sec_doubleSpinBox.value())
			self.prefOpt = self.prefOpt + " "+"--time-sec="+time_sec
		if self.pref.trafficfile_checkBox.isChecked():
			if self.pref.traffic_file_lineEdit.text().isEmpty() == False:
				trafficfile = self.pref.traffic_file_lineEdit.text()
				self.prefOpt = self.prefOpt + " "+ "-t "+ " "+ trafficfile
			else :
				self.showdialog("Set textual filename to log all HTTP traffic please!")#this is not necessary
		if self.pref.batch_checkBox.isChecked():
			self.prefOpt = self.prefOpt + " "+"--batch "
		if self.pref.dump_format_checkBox.isChecked():
			dump_format = str(self.pref.dump_format_comboBox.currentText())
			self.dmp_format= dump_format
			self.prefOpt = self.prefOpt + " "+"--dump-format="+dump_format
		if self.pref.output_dir_checkBox.isChecked():
			if self.pref.output_dir_lineEdit.text().isEmpty() == False:
				output_dir = self.pref.output_dir_lineEdit.text()
				self.prefOpt = self.prefOpt + " "+ "--output-dir="+ " "+ output_dir
		if self.pref.parse_errors_checkBox.isChecked():
			self.prefOpt = self.prefOpt + " "+"--parse-errors"
		if self.pref.save_ini_checkBox.isChecked():
			if self.pref.save_ini_lineEdit.text().isEmpty() == False:
				self.prefOpt = self.prefOpt + " "+ "--save="+ " "+ self.pref.save_ini_lineEdit.text()
		if self.pref.eta_checkBox.isChecked():
			self.prefOpt = self.prefOpt + " "+"--eta"
		if self.pref.hex_checkBox.isChecked():
			self.prefOpt = self.prefOpt + " "+"--hex"
		if self.pref.beep_checkBox.isChecked():
			self.prefOpt = self.prefOpt + " "+"--beep"
		if self.pref.cleanup_checkBox.isChecked():
			self.prefOpt = self.prefOpt + " "+"--cleanup"
		if self.pref.dependencies_checkBox.isChecked():
			self.prefOpt = self.prefOpt + " "+"--dependencies"
		if self.pref.purge_output_checkBox.isChecked():
			self.prefOpt = self.prefOpt + " "+"--purge-output"
		if self.pref.verbosity_checkBox.isChecked():
			verbosity = str(self.pref.verbosity_spinBox.value())
			self.prefOpt = self.prefOpt + " "+"-v "+" "+verbosity
		print self.prefOpt
		return self.prefOpt
	
	# Direct connection options/switches  
	def savedirectOptions(self):
		directO = "-d"+ self.dbms+self.directOptions() +self.userOptionsDBMS()+ " "+self.saveprefOptions()
		self.ui.command_lineEdit.setText(directO)
		
	def userOptionsDBMS(self):
		if self.dbms == "access":
			self.command = self.getAccessOptions()
		elif self.dbms == "db2":
			self.command = self.getdb2Options()
		elif self.dbms == "firebird":
			self.command = self.getfirebirdOptions()
		elif self.dbms == "hsqldb":
			self.command = self.gethsqldbOptions()
		elif self.dbms == "mssqlserver":
			self.command = self.pluginsUser()
		elif self.dbms == "mysql":
			self.command = self.pluginsUser()
		elif self.dbms == "oracle":
			self.command = self.getOracleOptions()
		elif self.dbms == "postgresql":
			self.command = self.pluginsUser()
		elif self.dbms == "sqlite":
			self.command = self.getSqliteOptions()
		elif self.dbms == "sybase":
			self.command = self.getSybaseOptions()
		else :
			if self.command == "":
				self.showdialog("choose an option from enum udfi... please!")
		return self.command

	def pluginsUser(self):
		if self.pushB=="UDFI":
			self.command = self.getUDFI()
		if self.pushB=="Enumeration":
			self.command =self.getEnumeration()
		if self.pushB=="Takeover":
			self.command =self.getOSTakeover()
		if self.pushB== "FSA":
			self.command =self.getFSAccess()
		if self.pushB=="Custom":
			self.command =self.getcustomInjection()
		return self.command
		
	def savedetectionOptions(self):
		if self.subDetection.url_lineEdit.text().isEmpty():
			self.showdialog("Please enter url!")
		else:
			url = "-u" + " " + self.subDetection.url_lineEdit.text() 
			detectionO =str(url)+ self.detectionOptions() +"  "+self.pluginsUser() + " "+self.saveprefOptions()
			self.ui.command_lineEdit.setText(detectionO)
	
	def discarddetectionOptions(self):
		print "discarddetectionOptions"
		
	def detectionOptions(self):
		self.detectionOpt=""
		if self.subDetection.eval_checkBox.isChecked():
			if self.subDetection.eval_lineEdit.text().isEmpty()==False:
				self.detectionOpt = self.detectionOpt + " "+"--eval="+self.subDetection.eval_lineEdit.text()
		if self.subDetection.data_radioButton.isChecked():
			if self.subDetection.data_plainTextEdit.toPlainText().isEmpty()==False:
				self.detectionOpt = self.detectionOpt +" "+"--data="+ self.subDetection.data_plainTextEdit.toPlainText()
		if self.subDetection.testparameter_checkBox.isChecked():
			if self.subDetection.testparameter_lineEdit.text().isEmpty()==False:
				self.detectionOpt = self.detectionOpt +" "+"-p "+" "+ self.subDetection.testparameter_lineEdit.text()
		elif self.subDetection.requestfile_checkBox.isChecked():
			if self.subDetection.requestfile_lineEdit.text().isEmpty()==False:
				self.detectionOpt = self.detectionOpt +" "+"-r"+" "+self.subDetection.requestfile_lineEdit.text()
			if self.subDetection.requestfile_checkBox.isChecked():
				if self.subDetection.testparam_lineEdit.text().isEmpty()==False:
					self.detectionOpt = self.detectionOpt +" "+"-p"+" "+self.subDetection.testparam_lineEdit.text()
		elif self.subDetection.host_header_checkBox.isChecked():
			if self.subDetection.host_header_lineEdit.text().isEmpty()==False:
				self.detectionOpt = self.detectionOpt +" "+"--host="+" "+self.subDetection.host_header_lineEdit.text()
			if self.subDetection.headers_checkBox.isChecked():
				if self.subDetection.headers_lineEdit.text().isEmpty()==False:
					self.detectionOpt = self.detectionOpt +" "+"--headers="+" "+self.subDetection.headers_lineEdit.text()
		elif self.subDetection.user_agent_checkBox.isChecked():
			if self.subDetection.user_agent_lineEdit.text().isEmpty()==False:
				self.detectionOpt = self.detectionOpt +" "+"--user-agent="+" "+self.subDetection.user_agent_lineEdit.text()
		if self.subDetection.referer_checkBox.isChecked():
			if self.subDetection.referer_lineEdit.text().isEmpty()==False:
				self.detectionOpt = self.detectionOpt +" "+"--referer="+" "+self.subDetection.referer_lineEdit.text()
		if self.subDetection.cookie_checkBox.isChecked():
			if self.subDetection.cookie_lineEdit.text().isEmpty()==False:
				self.detectionOpt = self.detectionOpt +" "+"--cookie="+" "+self.subDetection.cookie_lineEdit.text()
			if self.subDetection.cookie_del_checkBox.isChecked():
				if self.subDetection.cookie_del_lineEdit.text().isEmpty()==False:
					self.detectionOpt = self.detectionOpt +" "+"--cookie-del="+" "+self.subDetection.cookie_del_lineEdit.text()
		if self.subDetection.tamper_checkBox.isChecked():
			if self.subDetection.tamper_lineEdit.text().isEmpty()==False:
				self.detectionOpt = self.detectionOpt +" "+"--tamper="+" "+self.subDetection.tamper_lineEdit.text()
		if self.subDetection.crawl_checkBox.isChecked():
			crawl = str(self.subDetection.crawl_spinBox.value())
			self.detectionOpt = self.detectionOpt +" "+"--crawl="+" "+crawl
		if self.subDetection.crawl_exclude_checkBox.isChecked():
			if self.subDetection.crawl_exclude_lineEdit.text().isEmpty()==False:
				self.detectionOpt = self.detectionOpt +" "+"--crawl-exclude="+" "+self.subDetection.crawl_exclude_lineEdit.text()
		if self.subDetection.forms_checkBox.isChecked()	:
			self.detectionOpt = self.detectionOpt +" "+"--forms"
#			optDict["General"]["forms"] = True
		if self.subDetection.string_radioButton.isChecked():
			if self.subDetection.string_lineEdit.text().isEmpty()==False:
				self.detectionOpt = self.detectionOpt +" "+"--string="+" "+self.subDetection.string_lineEdit.text()
		if self.subDetection.code_radioButton.isChecked():
			if self.subDetection.code_lineEdit.text().isEmpty()==False:
				self.detectionOpt = self.detectionOpt +" "+"--code="+" "+self.subDetection.code_lineEdit.text()
		if self.subDetection.regexp_radioButton.isChecked():
			if self.subDetection.regexp_lineEdit.text().isEmpty()==False:
				self.detectionOpt = self.detectionOpt +" "+"--regexp="+" "+self.subDetection.regexp_lineEdit.text()
		if self.subDetection.not_string_radioButton.isChecked():
			if self.subDetection.not_string_lineEdit.text().isEmpty()==False:
				self.detectionOpt = self.detectionOpt +" "+"--not-string="+" "+self.subDetection.not_string_lineEdit.text()
		if self.subDetection.titles_checkBox.isChecked():	
			self.detectionOpt = self.detectionOpt +" "+"--titles"
		if self.subDetection.text_only_checkBox.isChecked():	
			self.detectionOpt = self.detectionOpt +" "+"--text-only" #output_groupBox
		if self.subDetection.output_groupBox.isChecked():
			if self.subDetection.output_dir_checkBox.isChecked():
				if self.subDetection.output_dir_lineEdit.text().isEmpty() == False:
					output_dir = self.subDetection.output_dir_lineEdit.text()
					self.detectionOpt = self.detectionOpt + " "+ "--output-dir="+ " "+ output_dir

		return self.detectionOpt
		
	def directOptions(self):
		regexp = QtCore.QRegExp("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
		validator = QtGui.QRegExpValidator(regexp,self.subDirect.IP_lineEdit) 
		state,pos = validator.validate(self.subDirect.IP_lineEdit.text(), 0)
		if self.subDirect.username_radioButton.isChecked():
			if self.subDirect.username_lineEdit.text().isEmpty():
				self.showdialog("Enter username please!")
			elif self.subDirect.password_lineEdit.text().isEmpty():
				self.showdialog("Enter password please!")
			elif (state== QtGui.QValidator.Acceptable) == False:
				self.showdialog("Check IP format please!") 
			elif str(self.subDirect.port_spinBox.value()) == "0":
				self.showdialog("Enter port please!") 			
			elif self.subDirect.db_name_lineEdit.text().isEmpty():
				self.showdialog("Enter DB name please!")
			else :
				username = self.subDirect.username_lineEdit.text()
				password = self.subDirect.password_lineEdit.text()
				IP = self.subDirect.IP_lineEdit.text()
				db_name = self.subDirect.db_name_lineEdit.text()
				port = str(self.subDirect.port_spinBox.value()) 
				self.directOpt =  "://"+username+":"+password+"@"+IP+":"+port+"/"+db_name
#				print self.directOpt # "firebird://sysdba:testpass@127.0.0.1:3050//opt/firebird/testdb.fdb"
#				print state== QtGui.QValidator.Acceptable
		elif self.subDirect.db_filepath_radioButton.isChecked():
			if self.subDirect.db_filepath_lineEdit.text().isEmpty():
				self.showdialog("Enter DB filepath please!")
			else :
				db_filepath = self.subDirect.db_filepath_lineEdit.text()
				#dbms = str(self.subDirect.dbms_comboBox.currentText())
				self.directOpt = "://"+db_filepath
		return self.directOpt
		
	def accessOptions(self,scrollArea):
		#Access dbms
		self.widgetAcc = QtGui.QWidget()
		self.subAccess = Ui_FormAccess()
		self.subAccess.setupUi(self)
		self.subAccess.setupUi(self.widgetAcc)  
		scrollAreaE =  QtGui.QScrollArea(scrollArea) 
		self.widgetAcc.setParent(scrollArea)
		scrollAreaE.setWidget(self.widgetAcc) 
		scrollArea.setWidget(scrollAreaE)
		self.widgetAcc.setGeometry(QtCore.QRect(10, 0, 791, 141))
		self.widgetAcc.show()

	def discarddirectOptions(self):
		self.accessOptions(self.subDirect.scrollArea)
		return self.ui.command_lineEdit.setText("")
		
	def getAccessOptions(self):
		self.accessOpt = ""
		if self.subAccess.access_count_checkBox.isChecked():
			self.accessOpt = " "+ "--count"
		if self.subAccess.access_schema_checkBox.isChecked():
			self.accessOpt = self.accessOpt+ " "+ "--schema"
		if self.subAccess.access_columns_checkBox.isChecked():
			self.accessOpt = self.accessOpt+ " "+ "--columns"
		if self.subAccess.access_tables_checkBox.isChecked():
			self.accessOpt = self.accessOpt+ " "+ "--tables"
		if self.subAccess.access_dump_checkBox.isChecked():
			self.accessOpt = self.accessOpt+ " "+ "--dump"
		elif self.subAccess.access_dump_all_checkBox.isChecked():
			self.accessOpt = self.accessOpt+ " "+ "--dump-all"
		if self.subAccess.access_sql_query_checkBox.isChecked():
			if self.subAccess.access_sql_query_lineEdit.text().isEmpty()== False:
				self.accessOpt = self.accessOpt+ " "+ "--sql-query=" + self.subAccess.access_sql_query_lineEdit.text()
		if self.subAccess.access_sqlshell_checkBox.isChecked():
			self.accessOpt = self.accessOpt+ " "+ "--sql-shell"
		if self.subAccess.access_brute_tables_checkBox.isChecked():
			self.accessOpt = self.accessOpt+ " "+ "--common-tables"
		if self.subAccess.access_brute_columns_checkBox.isChecked():
			self.accessOpt = self.accessOpt+ " "+ "--common-columns"
		if self.subAccess.access_fingerprint_checkBox.isChecked():
			self.accessOpt = self.accessOpt+ " "+ "--fingerprint"
		return self.accessOpt
		
	
	def db2Options(self,scrollArea):
		self.dbms = "db2"
		# Ui_FormDB2 
		self.widgetDB2 = QtGui.QWidget()
		self.subDB2 = Ui_FormDB2()
		self.subDB2.setupUi(self)
		self.subDB2.setupUi(self.widgetDB2)  
		scrollAreaE =  QtGui.QScrollArea(scrollArea) 
		self.widgetDB2.setParent(scrollArea)
		scrollAreaE.setWidget(self.widgetDB2) 
		scrollArea.setWidget(scrollAreaE)
		#scrollArea.setGeometry(QtCore.QRect(120, 20, 680, 210))
		self.widgetDB2.setGeometry(QtCore.QRect(10, 0, 791, 150)) #0, 0, 791, 145
		self.widgetDB2.show()

	def getdb2Options(self):
		self.db2Opt = ""
		if self.subDB2.db2_current_user_checkBox.isChecked():
			self.db2Opt = " "+ "--current-user"
		if self.subDB2.db2_privileges_checkBox.isChecked():
			self.db2Opt = self.db2Opt+ " "+ "--privileges"
		if self.subDB2.db2_users_checkBox.isChecked():
			self.db2Opt = self.db2Opt+ " "+ "--users"
		if self.subDB2.db2_roles_checkBox.isChecked():
			self.db2Opt = self.db2Opt+ " "+ "--roles"
		if self.subDB2.db2_is_dba_checkBox.isChecked():
			self.db2Opt = self.db2Opt+ " "+ "--is-dba"
		if self.subDB2.db2_count_checkBox.isChecked():
			self.db2Opt = self.db2Opt+ " "+ "--count"
		if self.subDB2.db2_schema_checkBox.isChecked():
			self.db2Opt = self.db2Opt+ " "+ "--schema"
		if self.subDB2.db2_columns_checkBox.isChecked():
			self.db2Opt = self.db2Opt+ " "+ "--columns"
		if self.subDB2.db2_tables_checkBox.isChecked():
			self.db2Opt = self.db2Opt+ " "+ "--tables"
		if self.subDB2.db2_dbs_checkBox.isChecked():
			self.db2Opt = self.db2Opt+ " "+ "--dbs"
		if self.subDB2.db2_dump_checkBox.isChecked():
			self.db2Opt = self.db2Opt+ " "+ "--dump"
		elif self.subDB2.db2_dump_all_checkBox.isChecked():
			self.db2Opt = self.db2Opt+ " "+ "--dump-all"
		if self.subDB2.db2_search_checkBox.isChecked():
			if self.subDB2.db2_DB_checkBox.isChecked():
				if self.subDB2.db2_DB_lineEdit.text().isEmpty()== False:
					self.searchD =""
					self.searchD = "-D" + " "+ self.subDB2.db2_DB_lineEdit.text()
			if self.subDB2.db2_TBL_checkBox.isChecked():
				if self.subDB2.db2_TBL_lineEdit.text().isEmpty()== False:
					self.searchTBL = ""
					self.searchTBL = " "+"-T" + " "+ self.subDB2.db2_TBL_lineEdit.text()
			if self.subDB2.db2_COL_checkBox.isChecked():
				if self.subDB2.db2_COL_lineEdit.text().isEmpty()== False:
					self.searchC = ""
					self.searchC = " "+"-C" + " "+ self.subDB2.db2_COL_lineEdit.text()
			else :
				self.showdialog("Enter column(s), table(s) and/or database name(s) to search please!")
			self.db2Opt = self.db2Opt+ " "+ "--search"+ " "+ self.searchD + self.searchTBL + self.searchC
		if self.subDB2.db2_banner_checkBox.isChecked():
			self.db2Opt = self.db2Opt+ " "+ "--banner"
		if self.subDB2.db2_hostname_checkBox.isChecked():
			self.db2Opt = self.db2Opt+ " "+ "--hostname"
		if self.subDB2.db2_sql_query_checkBox.isChecked():
			if self.subDB2.adb2_sql_query_lineEdit.text().isEmpty()== False:
				self.db2Opt = self.db2Opt+ " "+ "--sql-query=" + self.subDB2.db2_sql_query_lineEdit.text()
		if self.subDB2.db2_sqlshell_checkBox.isChecked():
			self.db2Opt = self.db2Opt+ " "+ "--sql-shell"
		if self.subDB2.db2_brute_tables_checkBox.isChecked():
			self.db2Opt = self.db2Opt+ " "+ "--common-tables"
		if self.subDB2.db2_brute_columns_checkBox_2.isChecked():
			self.db2Opt = self.db2Opt+ " "+ "--common-columns"
		if self.subDB2.db2_fingerprint_checkBox.isChecked():
			self.db2Opt = self.db2Opt+ " "+ "--fingerprint"
		return self.db2Opt
	
	def firebirdOptions(self,scrollArea):
		self.dbms = "firebird"
		self.widgetFirebird = QtGui.QWidget()
		self.subFirebird = Ui_FormFirebird()
		self.subFirebird.setupUi(self)
		self.subFirebird.setupUi(self.widgetFirebird)  
		scrollAreaE =  QtGui.QScrollArea(scrollArea) 
		self.widgetFirebird.setParent(scrollArea)
		scrollAreaE.setWidget(self.widgetFirebird) 
		scrollArea.setWidget(scrollAreaE)
		#scrollArea.setGeometry(QtCore.QRect(120, 20, 680, 210))
		self.widgetFirebird.setGeometry(QtCore.QRect(10, 0, 791, 150)) #10, 0, 791, 150
		self.widgetFirebird.show()

	def getfirebirdOptions(self):
		self.firebirdOpt = ""
		if self.subFirebird.firebird_current_user_checkBox.isChecked():
			self.firebirdOpt = " "+ "--current-user"
		if self.subFirebird.firebird_privileges_checkBox.isChecked():
			self.firebirdOpt = self.firebirdOpt+ " "+ "--privileges"
		if self.subFirebird.firebird_users_checkBox.isChecked():
			self.firebirdOpt = self.firebirdOpt+ " "+ "--users"
		if self.subFirebird.firebird_roles_checkBox.isChecked():
			self.firebirdOpt = self.firebirdOpt+ " "+ "--roles"
		if self.subFirebird.firebird_is_dba_checkBox.isChecked():
			self.firebirdOpt = self.firebirdOpt+ " "+ "--is-dba"
		if self.subFirebird.firebird_count_checkBox.isChecked():
			self.firebirdOpt = self.firebirdOpt+ " "+ "--count"
		if self.subFirebird.firebird_schema_checkBox.isChecked():
			self.firebirdOpt = self.firebirdOpt+ " "+ "--schema"
		if self.subFirebird.firebird_columns_checkBox.isChecked():
			self.firebirdOpt = self.firebirdOpt+ " "+ "--columns"
		if self.subFirebird.firebird_tables_checkBox.isChecked():
			self.firebirdOpt = self.firebirdOpt+ " "+ "--tables"
		if self.subFirebird.firebird_dump_checkBox.isChecked():
			self.firebirdOpt = self.firebirdOpt+ " "+ "--dump"
		elif self.subFirebird.firebird_dump_all_checkBox.isChecked():
			self.firebirdOpt = self.firebirdOpt+ " "+ "--dump-all"
		if self.subFirebird.firebird_banner_checkBox.isChecked():
			self.firebirdOpt = self.firebirdOpt+ " "+ "--banner"
		if self.subFirebird.firebird_sql_query_checkBox.isChecked():
			if self.subFirebird.firebird_sql_query_lineEdit.text().isEmpty()== False:
				self.firebirdOpt = self.firebirdOpt+ " "+ "--sql-query=" + self.subFirebird.firebird_sql_query_lineEdit.text()
		if self.subFirebird.firebird_sqlshell_checkBox.isChecked():
			self.firebirdOpt = self.firebirdOpt+ " "+ "--sql-shell"
		if self.subFirebird.firebird_brute_tables_checkBox.isChecked():
			self.firebirdOpt = self.firebirdOpt+ " "+ "--common-tables"
		if self.subFirebird.firebird_brute_columns_checkBox.isChecked():
			self.firebirdOpt = self.firebirdOpt+ " "+ "--common-columns"
		if self.subFirebird.firebird__fingerprint_checkBox.isChecked():
			self.firebirdOpt = self.firebirdOpt+ " "+ "--fingerprint"
		return self.firebirdOpt
		
	def hsqldbOptions(self,scrollArea):
		self.dbms = "hsqldb"
		self.widgetHsqldb = QtGui.QWidget()
		self.subHsqldb = Ui_FormHsqldb()
		self.subHsqldb.setupUi(self)
		self.subHsqldb.setupUi(self.widgetHsqldb)  
		scrollAreaE =  QtGui.QScrollArea(scrollArea) 
		self.widgetHsqldb.setParent(scrollArea)
		scrollAreaE.setWidget(self.widgetHsqldb) 
		scrollArea.setWidget(scrollAreaE)
		#scrollArea.setGeometry(QtCore.QRect(120, 20, 680, 210))
		self.widgetHsqldb.setGeometry(QtCore.QRect(10, 0, 791, 160))#10, 0, 791, 150
		self.widgetHsqldb.show()
	
	def gethsqldbOptions(self):
		self.hsqldbOpt = ""
		if self.subHsqldb.hsql_current_user_checkBox.isChecked():
			self.hsqldbOpt = " "+ "--current-user"
		if self.subHsqldb.hsql_users_checkBox.isChecked():
			self.hsqldbOpt = self.hsqldbOpt+ " "+ "--users"
		if self.subHsqldb.hsql_roles_checkBox.isChecked():
			self.hsqldbOpt = self.hsqldbOpt+ " "+ "--roles"
		if self.subHsqldb.hsql_is_dba_checkBox.isChecked():
			self.hsqldbOpt = self.hsqldbOpt+ " "+ "--is-dba"
		if self.subHsqldb.hsql_count_checkBox.isChecked():
			self.hsqldbOpt = self.hsqldbOpt+ " "+ "--count"
		if self.subHsqldb.hsql_schema_checkBox.isChecked():
			self.hsqldbOpt = self.hsqldbOpt+ " "+ "--schema"
		if self.subHsqldb.hsql_columns_checkBox.isChecked():
			self.hsqldbOpt = self.hsqldbOpt+ " "+ "--columns"
		if self.subHsqldb.hsql_tables_checkBox.isChecked():
			self.hsqldbOpt = self.hsqldbOpt+ " "+ "--tables"
		if self.subHsqldb.hsql_dbs_checkBox.isChecked():
			self.hsqldbOpt = self.hsqldbOpt+ " "+ "--dbs"
		if self.subHsqldb.hsql_dump_checkBox.isChecked():
			self.hsqldbOpt = self.hsqldbOpt+ " "+ "--dump"
		elif self.subHsqldb.hsql_dump_all_checkBox.isChecked():
			self.hsqldbOpt = self.hsqldbOpt+ " "+ "--dump-all"
		if self.subHsqldb.hsql_search_checkBox.isChecked():
			if self.subHsqldb.hsql_DB_checkBox.isChecked():
				if self.subHsqldb.hsql_DB_lineEdit.text().isEmpty()== False:
					self.searchD =""
					self.searchD = "-D" + " "+ self.subHsqldb.hsql_DB_lineEdit.text()
			if self.subHsqldb.hsql_TBL_checkBox.isChecked():
				if self.subHsqldb.hsql_TBL_lineEdit.text().isEmpty()== False:
					self.searchTBL = ""
					self.searchTBL = " "+"-T" + " "+ self.subHsqldb.hsql_TBL_lineEdit.text()
			if self.subHsqldb.hsql_COL_checkBox.isChecked():
				if self.subHsqldb.hsql_COL_lineEdit.text().isEmpty()== False:
					self.searchC = ""
					self.searchC = " "+"-C" + " "+ self.subHsqldb.hsql_COL_lineEdit.text()
			else :
				self.showdialog("Enter column(s), table(s) and/or database name(s) to search please!")
			self.hsqldbOpt = self.hsqldbOpt+ " "+ "--search"+ " "+ self.searchD + self.searchTBL + self.searchC
		if self.subHsqldb.hsql_banner_checkBox.isChecked():
			self.hsqldbOpt = self.hsqldbOpt+ " "+ "--banner"
		if self.subHsqldb.hsql_sql_query_checkBox.isChecked():
			if self.subHsqldb.hsql_sql_query_lineEdit.text().isEmpty()== False:
				self.hsqldbOpt = self.hsqldbOpt+ " "+ "--sql-query=" + self.subHsqldb.hsql_sql_query_lineEdit.text()
		if self.subHsqldb.hsql_sqlshell_checkBox.isChecked():
			self.hsqldbOpt = self.hsqldbOpt+ " "+ "--sql-shell"
		if self.subHsqldb.hsql_brute_tables_checkBox.isChecked():
			self.hsqldbOpt = self.hsqldbOpt+ " "+ "--common-tables"
		if self.subHsqldb.hsql_brute_columns_checkBox.isChecked():
			self.hsqldbOpt = self.hsqldbOpt+ " "+ "--common-columns"
		if self.subHsqldb.hsql_fingerprint_checkBox.isChecked():
			self.hsqldbOpt = self.hsqldbOpt+ " "+ "--fingerprint"
		return self.hsqldbOpt
		
	def mssqlserverOptions(self,scrollArea):
		self.dbms = "mssqlserver"
		self.widgetMssqlserver = QtGui.QWidget()
		self.subMssql = Ui_FormMssqlserver()
		self.subMssql.setupUi(self)
		self.subMssql.setupUi(self.widgetMssqlserver)  
		scrollAreaE =  QtGui.QScrollArea(scrollArea) 
		self.widgetMssqlserver.setParent(scrollArea)
		scrollAreaE.setWidget(self.widgetMssqlserver) 
		scrollArea.setWidget(scrollAreaE)
		#scrollArea.setGeometry(QtCore.QRect(120, 20, 680, 210))
		self.widgetMssqlserver.setGeometry(QtCore.QRect(10, 0, 785, 185)) 
		self.widgetMssqlserver.show()
		self.subMssql.mssql_enum_checkBox.clicked.connect(lambda : self.enumerationOptions(self.subMssql.scrollArea))
		self.subMssql.mssql_fsa_checkBox.clicked.connect(lambda : self.fsaOptions(self.subMssql.scrollArea))
		self.subMssql.mssql_ostake_checkBox.clicked.connect(lambda : self.takeoverOptions(self.subMssql.scrollArea))
		
	def mysqlOptions(self,scrollArea):
		self.dbms = "mysql"
		self.widgetMysql = QtGui.QWidget()
		self.subMysql = Ui_FormMysql()
		self.subMysql.setupUi(self)
		self.subMysql.setupUi(self.widgetMysql)  
		scrollAreaE =  QtGui.QScrollArea(scrollArea) 
		self.widgetMysql.setParent(scrollArea)
		scrollAreaE.setWidget(self.widgetMysql) 
		scrollArea.setWidget(scrollAreaE)
		#scrollArea.setGeometry(QtCore.QRect(120, 20, 680, 210))
		self.widgetMysql.setGeometry(QtCore.QRect(10, 0, 791, 185))#10, 0, 785, 185
		self.widgetMysql.show()
		self.subMysql.enum_checkBox.clicked.connect(lambda : self.enumerationOptions(self.subMysql.scrollArea))
		self.subMysql.fsa_checkBox.clicked.connect(lambda : self.fsaOptions(self.subMysql.scrollArea))
		self.subMysql.udfi_checkBox.clicked.connect(lambda : self.UDFIOptions(self.subMysql.scrollArea))
		self.subMysql.ostake_checkBox.clicked.connect(lambda : self.takeoverOptions(self.subMysql.scrollArea))

	def oracleOptions(self,scrollArea):
		self.dbms = "oracle"
		self.widgetOracle = QtGui.QWidget()
		self.subOracle = Ui_FormOracle()
		self.subOracle.setupUi(self)
		self.subOracle.setupUi(self.widgetOracle)  
		scrollAreaE =  QtGui.QScrollArea(scrollArea) 
		self.widgetOracle.setParent(scrollArea)
		scrollAreaE.setWidget(self.widgetOracle) 
		scrollArea.setWidget(scrollAreaE)
		#scrollArea.setGeometry(QtCore.QRect(120, 20, 680, 210))
		self.widgetOracle.setGeometry(QtCore.QRect(10, 0, 791, 150))
		self.widgetOracle.show()

	def getOracleOptions(self):
		self.oracleOpt = ""
		if self.subOracle.oracle_current_user_checkBox.isChecked():
			self.oracleOpt = " "+ "--current-user"
		if self.subOracle.oracle_users_checkBox.isChecked():
			self.oracleOpt = self.oracleOpt+ " "+ "--users"
		if self.subOracle.oracle_roles_checkBox.isChecked():
			self.oracleOpt = self.oracleOpt+ " "+ "--roles"
		if self.subOracle.oracle_passwords_checkBox.isChecked():
			self.oracleOpt = self.oracleOpt+ " "+ "--passwords"
		if self.subOracle.oracle_privileges_checkBox.isChecked():
			self.oracleOpt = self.oracleOpt+ " "+ "--privileges"
		if self.subOracle.oracle_is_dba_checkBox.isChecked():
			self.oracleOpt = self.oracleOpt+ " "+ "--is-dba"
		if self.subOracle.oracle_count_checkBox.isChecked():
			self.oracleOpt = self.oracleOpt+ " "+ "--count"
		if self.subOracle.oracle_schema_checkBox.isChecked():
			self.oracleOpt = self.oracleOpt+ " "+ "--schema"
		if self.subOracle.oracle_columns_checkBox.isChecked():
			self.oracleOpt = self.oracleOpt+ " "+ "--columns"
		if self.subOracle.oracle_tables_checkBox.isChecked():
			self.oracleOpt = self.oracleOpt+ " "+ "--tables"
		if self.subOracle.oracle_dbs_checkBox.isChecked():
			self.oracleOpt = self.oracleOpt+ " "+ "--dbs"
		if self.subOracle.oracle_dump_checkBox.isChecked():
			self.oracleOpt = self.oracleOpt+ " "+ "--dump"
		elif self.subOracle.oracle_dump_all_checkBox.isChecked():
			self.oracleOpt = self.oracleOpt+ " "+ "--dump-all"
		if self.subOracle.oracle_search_checkBox.isChecked():
			self.searchD =""
			self.searchTBL = ""
			self.searchC = ""
			if self.subOracle.oracle_DB_checkBox.isChecked():
				if self.subOracle.oracle_DB_lineEdit.text().isEmpty()==False:
					self.searchD = "-D" + " "+ self.subOracle.oracle_DB_lineEdit.text()
					self.oracleOpt = self.oracleOpt+ " "+ "--search"+ " "+ self.searchD
					#self.showdialog("Enter  database name(s) to search please!")
			if self.subOracle.oracle_TBL_checkBox.isChecked():
				if self.subOracle.oracle_TBL_lineEdit.text().isEmpty()==False:
					self.searchTBL = " "+"-T" + " "+ self.subOracle.oracle_TBL_lineEdit.text()
					self.oracleOpt = self.oracleOpt+ " "+ "--search"+ " "+ self.searchTBL
			if self.subOracle.oracle_COL_checkBox.isChecked():
				if self.subOracle.oracle_COL_lineEdit.text().isEmpty()==False:
					self.searchC = " "+"-C" + " "+ self.subOracle.oracle_COL_lineEdit.text()
					self.oracleOpt = self.oracleOpt+ " "+ "--search"+ " "+ self.searchC
		if self.subOracle.oracle_banner_checkBox.isChecked():
			self.oracleOpt = self.oracleOpt+ " "+ "--banner"
		if self.subOracle.oracle_hostname_checkBox.isChecked():
			self.oracleOpt = self.oracleOpt+ " "+ "--hostname"
		if self.subOracle.oracle_sql_query_checkBox.isChecked():
			if self.subOracle.oracle_sql_query_lineEdit.text().isEmpty()== False:
				self.oracleOpt = self.oracleOpt+ " "+ "--sql-query=" + self.subOracle.oracle_sql_query_lineEdit.text()
		if self.subOracle.oracle_sqlshell_checkBox.isChecked():
			self.oracleOpt = self.oracleOpt+ " "+ "--sql-shell"
		if self.subOracle.oracle_brute_tables_checkBox.isChecked():
			self.oracleOpt = self.oracleOpt+ " "+ "--common-tables"
		if self.subOracle.oracle_brute_columns_checkBox.isChecked():
			self.oracleOpt = self.oracleOpt+ " "+ "--common-columns"
		if self.subOracle.oracle_fingerprint_checkBox.isChecked():
			self.oracleOpt = self.oracleOpt+ " "+ "--fingerprint"
		return self.oracleOpt
	
	def postgresqlOptions(self,scrollArea):
		self.dbms = "postgresql"
		self.widgetMysql = QtGui.QWidget()
		self.subMysql = Ui_FormMysql()
		self.subMysql.setupUi(self)
		self.subMysql.setupUi(self.widgetMysql)  
		scrollAreaE =  QtGui.QScrollArea(scrollArea) 
		self.widgetMysql.setParent(scrollArea)
		scrollAreaE.setWidget(self.widgetMysql) 
		scrollArea.setWidget(scrollAreaE)
		#scrollArea.setGeometry(QtCore.QRect(120, 20, 680, 210))
		self.widgetMysql.setGeometry(QtCore.QRect(10, 0, 791, 185)) #10, 0, 785, 185
		self.widgetMysql.show()
		self.subMysql.enum_checkBox.clicked.connect(lambda : self.enumerationOptions(self.subMysql.scrollArea))
		self.subMysql.fsa_checkBox.clicked.connect(lambda : self.fsaOptions(self.subMysql.scrollArea))
		self.subMysql.udfi_checkBox.clicked.connect(lambda : self.UDFIOptions(self.subMysql.scrollArea))
		self.subMysql.ostake_checkBox.clicked.connect(lambda : self.takeoverOptions(self.subMysql.scrollArea))
		
	def sqliteOptions(self,scrollArea):
		self.dbms = "sqlite"
		self.widgetSqlite = QtGui.QWidget()
		self.subSqlite = Ui_FormSqlite()
		self.subSqlite.setupUi(self)
		self.subSqlite.setupUi(self.widgetSqlite)  
		scrollAreaE =  QtGui.QScrollArea(scrollArea) 
		self.widgetSqlite.setParent(scrollArea)
		scrollAreaE.setWidget(self.widgetSqlite) 
		scrollArea.setWidget(scrollAreaE)
		#scrollArea.setGeometry(QtCore.QRect(120, 20, 680, 210))
		self.widgetSqlite.setGeometry(QtCore.QRect(10, 0, 791, 150))
		self.widgetSqlite.show()

	def getSqliteOptions(self):
		self.sqliteOpt = ""
		if self.subSqlite.sqlite_roles_checkBox.isChecked():
			self.sqliteOpt = " "+ "--roles"
		if self.subSqlite.sqlite_count_checkBox.isChecked():
			self.sqliteOpt = self.sqliteOpt+ " "+ "--count"
		if self.subSqlite.sqlite_schema_checkBox.isChecked():
			self.sqliteOpt = self.sqliteOpt+ " "+ "--schema"
		if self.subSqlite.sqlite_columns_checkBox.isChecked():
			self.sqliteOpt = self.sqliteOpt+ " "+ "--columns"
		if self.subSqlite.sqlite_tables_checkBox.isChecked():
			self.sqliteOpt = self.sqliteOpt+ " "+ "--tables"
		if self.subSqlite.sqlite_dump_checkBox.isChecked():
			self.sqliteOpt = self.sqliteOpt+ " "+ "--dump"
		elif self.subSqlite.sqlite_dump_all_checkBox.isChecked():
			self.sqliteOpt = self.sqliteOpt+ " "+ "--dump-all"
		if self.subSqlite.sqlite_banner_checkBox.isChecked():
			self.sqliteOpt = self.sqliteOpt+ " "+ "--banner"
		if self.subSqlite.sqlite_sql_query_checkBox.isChecked():
			if self.subSqlite.sqlite_sql_query_lineEdit.text().isEmpty()== False:
				self.sqliteOpt = self.sqliteOpt+ " "+ "--sql-query=" + self.subSqlite.sqlite_sql_query_lineEdit.text()
		if self.subSqlite.sqlite_sqlshell_checkBox.isChecked():
			self.sqliteOpt = self.sqliteOpt+ " "+ "--sql-shell"
		if self.subSqlite.sqlite_brute_tables_checkBox.isChecked():
			self.sqliteOpt = self.sqliteOpt+ " "+ "--common-tables"
		if self.subSqlite.sqlite_brute_columns_checkBox.isChecked():
			self.sqliteOpt = self.sqliteOpt+ " "+ "--common-columns"
		if self.subSqlite.sqlite_fingerprint_checkBox.isChecked():
			self.sqliteOpt = self.sqliteOpt+ " "+ "--fingerprint"
		return self.sqliteOpt

	def sybaseOptions(self,scrollArea):
		self.dbms = "sybase"
		self.widgetSybase = QtGui.QWidget()
		self.subSybase = Ui_FormSybase()
		self.subSybase.setupUi(self)
		self.subSybase.setupUi(self.widgetSybase)  
		scrollAreaE =  QtGui.QScrollArea(scrollArea) 
		self.widgetSybase.setParent(scrollArea)
		scrollAreaE.setWidget(self.widgetSybase) 
		scrollArea.setWidget(scrollAreaE)
		#scrollArea.setGeometry(QtCore.QRect(120, 20, 680, 210))
		self.widgetSybase.setGeometry(QtCore.QRect(10, 0, 791, 150))
		self.widgetSybase.show()
		
	def getSybaseOptions(self):
		self.sybaseOpt = ""
		if self.subSybase.sybase_current_user_checkBox.isChecked():
			self.sybaseOpt = " "+ "--current-user"
		if self.subSybase.sybase_users_checkBox.isChecked():
			self.sybaseOpt = self.sybaseOpt+ " "+ "--users"
		if self.subSybase.sybase_roles_checkBox.isChecked():
			self.sybaseOpt = self.sybaseOpt+ " "+ "--roles"
		if self.subSybase.sybase_passwords_checkBox.isChecked():
			self.sybaseOpt = self.sybaseOpt+ " "+ "--passwords"
		if self.subSybase.sybase_privileges_checkBox.isChecked():
			self.sybaseOpt = self.sybaseOpt+ " "+ "--privileges"
		if self.subSybase.sybase_is_dba_checkBox.isChecked():
			self.sybaseOpt = self.sybaseOpt+ " "+ "--is-dba"
		if self.subSybase.sybase_count_checkBox.isChecked():
			self.sybaseOpt = self.sybaseOpt+ " "+ "--count"
		if self.subSybase.sybase_schema_checkBox.isChecked():
			self.sybaseOpt = self.sybaseOpt+ " "+ "--schema"
		if self.subSybase.sybase_columns_checkBox.isChecked():
			self.sybaseOpt = self.sybaseOpt+ " "+ "--columns"
		if self.subSybase.sybase_tables_checkBox.isChecked():
			self.sybaseOpt = self.sybaseOpt+ " "+ "--tables"
		if self.subSybase.sybase_dbs_checkBox.isChecked():
			self.sybaseOpt = self.sybaseOpt+ " "+ "--dbs"
		if self.subSybase.sybase_dump_checkBox.isChecked():
			self.sybaseOpt = self.sybaseOpt+ " "+ "--dump"
		elif self.subSybase.sybase_dump_all_checkBox.isChecked():
			self.sybaseOpt = self.sybaseOpt+ " "+ "--dump-all"
		if self.subSybase.sybase_banner_checkBox.isChecked():
			self.sybaseOpt = self.sybaseOpt+ " "+ "--banner"
		if self.subSybase.sybase_sql_query_checkBox.isChecked():
			if self.subSybase.sybase_sql_query_lineEdit.text().isEmpty()== False:
				self.sybaseOpt = self.sybaseOpt+ " "+ "--sql-query=" + self.subSybase.sybase_sql_query_lineEdit.text()
		if self.subSybase.sybase_sqlshell_checkBox.isChecked():
			self.sybaseOpt = self.sybaseOpt+ " "+ "--sql-shell"
		if self.subSybase.sybase_brute_tables_checkBox.isChecked():
			self.sybaseOpt = self.sybaseOpt+ " "+ "--common-tables"
		if self.subSybase.sybase_brute_columns_checkBox.isChecked():
			self.sybaseOpt = self.sybaseOpt+ " "+ "--common-columns"
		if self.subSybase.sybase_fingerprint_checkBox.isChecked():
			self.sybaseOpt = self.sybaseOpt+ " "+ "--fingerprint"
		return self.sybaseOpt
	
	def enumerationOptions(self,scrollArea):
		self.pushB="Enumeration"
		self.widgetEnum = QtGui.QWidget()
		self.subEnumeration = Ui_FormEnumeration()
		self.subEnumeration.setupUi(self)
		self.subEnumeration.setupUi(self.widgetEnum)  
		scrollAreaE =  QtGui.QScrollArea(scrollArea) 
		self.widgetEnum.setParent(scrollArea)
		scrollAreaE.setWidget(self.widgetEnum) 
		scrollArea.setWidget(scrollAreaE)
		#scrollArea.setGeometry(QtCore.QRect(120, 20, 680, 210))
		self.widgetEnum.setGeometry(QtCore.QRect(10, 0, 775, 135)) # 10, 0, 791, 170
		self.widgetEnum.show()
		self.subEnumeration.sqlfile_toolButton.clicked.connect(lambda : self.openDir(self.subEnumeration.sqlfile_lineEdit))

	def getEnumeration(self):
		self.enumOpt=""
		if self.subEnumeration.fingerprint_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--fingerprint"
		if self.subEnumeration.current_user_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--current-user"
		if self.subEnumeration.passwords_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--passwords"
		if self.subEnumeration.users_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--users"
		if self.subEnumeration.is_dba_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--is-dba"
		if self.subEnumeration.privileges_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--privileges"
		if self.subEnumeration.roles_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--roles"
		if self.subEnumeration.count_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--count"
		if self.subEnumeration.columns_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--columns"
		if self.subEnumeration.schema_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--schema"
		if self.subEnumeration.current_db_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--current-db"
		if self.subEnumeration.tables_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--tables"
		if self.subEnumeration.dbs_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--dbs"
		if self.subEnumeration.dump_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--dump"
		elif self.subEnumeration.dump_all_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--dump-all"
		if self.subEnumeration.search_checkBox.isChecked():
			self.search=""
			self.DB =""
			self.TBL =""
			self.COL =""
			if self.subEnumeration.DB_checkBox.isChecked():
				if self.subEnumeration.DB_lineEdit.text().isEmpty():
					pass
				else :
					self.DB = "-D "+ self.subEnumeration.DB_lineEdit.text()
			if self.subEnumeration.TBL_checkBox.isChecked():
				if self.subEnumeration.TBL_lineEdit.text().isEmpty():
					pass
				else :
					self.TBL = "-T "+ self.subEnumeration.TBL_lineEdit.text()
			if self.subEnumeration.COL_checkBox.isChecked():
				if self.subEnumeration.COL_lineEdit.text().isEmpty():
					pass
				else :
					self.COL = "-C "+ self.subEnumeration.COL_lineEdit.text()
			else :
				self.showdialog("Insert one of the search options please !")
			self.search=""+" --search"+" "+self.DB+" "+ self.TBL+" "+self.COL
			self.enumOpt = self.enumOpt + self.search
		if self.subEnumeration.banner_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--banner"
		if self.subEnumeration.hostname_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--hostname"
		if self.subEnumeration.brute_tables_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--common-tables"
		if self.subEnumeration.brute_columns_checkBox.isChecked():
			self.enumOpt = self.enumOpt + "--common-columns"
		if self.subEnumeration.sql_query_checkBox.isChecked():
			if self.subEnumeration.sql_query_lineEdit.text().isEmpty()== False:
				self.enumOpt = self.enumOpt+ " "+ "--sql-query=" + self.subEnumeration.sql_query_lineEdit.text()
		if self.subEnumeration.sqlshell_checkBox.isChecked():
			self.enumOpt = self.enumOpt+ " "+ "--sql-shell"
		elif self.subEnumeration.sqlfile_checkBox.isChecked():
			if self.subEnumeration.sqlfile_lineEdit.text().isEmpty()== False:
				self.enumOpt = self.enumOpt+ " "+"--sql-file="+self.subEnumeration.sqlfile_lineEdit.text()
		return self.enumOpt

	def fsaOptions(self,scrollArea):
		self.pushB="FSA"
		self.widgetFSA = QtGui.QWidget()
		self.subFSAccess = Ui_FormFSA()
		self.subFSAccess.setupUi(self)
		self.subFSAccess.setupUi(self.widgetFSA)  
		scrollAreaE =  QtGui.QScrollArea(scrollArea) 
		self.widgetFSA.setParent(scrollArea)
		scrollAreaE.setWidget(self.widgetFSA) 
		scrollArea.setWidget(scrollAreaE)
		#scrollArea.setGeometry(QtCore.QRect(120, 20, 680, 210))
		self.widgetFSA.setGeometry(QtCore.QRect(10, 0, 791, 141))
		self.widgetFSA.show()
		print "fsaOptions"
		self.subFSAccess.fsa_write_file_toolButton.clicked.connect(lambda : self.openDir(self.subFSAccess.fsa_write_lineEdit))
		self.subFSAccess.fsa_write_path_toolButton.clicked.connect(lambda : self.openDir(self.subFSAccess.fsa_write_filepath_lineEdit))
	
	#Get FSAccess user's options
	def getFSAccess(self):
		self.fsaOpt=""		
		if self.subFSAccess.fsa_write_radioButton.isChecked():
			if self.subFSAccess.fsa_write_lineEdit.text().isEmpty():
				pass
			if self.subFSAccess.fsa_write_filepath_lineEdit.text().isEmpty(): 
				self.showdialog("Enter correct input data please!")
			else :
				self.fsaOpt = self.fsaOpt + "  --file-write="+self.subFSAccess.fsa_write_lineEdit.text()+ " --file-dest="+self.subFSAccess.fsa_write_filepath_lineEdit.text()
		elif self.subFSAccess.fsa_read_radioButton.isChecked():
			if self.subFSAccess.fsa_read_lineEdit.text().isEmpty():
				self.showdialog("Enter correct input data please!")
			else :
				self.fsaOpt = self.fsaOpt + "  --file-read="+self.subFSAccess.fsa_read_lineEdit.text()
		return self.fsaOpt
	
	def takeoverOptions(self,scrollArea):
		self.pushB="Takeover"
		self.widgetTakeover = QtGui.QWidget()
		self.subOSTakeover = Ui_FormOSTakeover()
		self.subOSTakeover.setupUi(self)
		self.subOSTakeover.setupUi(self.widgetTakeover)  
		scrollAreaE =  QtGui.QScrollArea(scrollArea) 
		self.widgetTakeover.setParent(scrollArea)
		scrollAreaE.setWidget(self.widgetTakeover) 
		scrollArea.setWidget(scrollAreaE)
		#scrollArea.setGeometry(QtCore.QRect(120, 20, 680, 210))
		self.widgetTakeover.setGeometry(QtCore.QRect(10, 0, 791, 141))
		self.widgetTakeover.show()
		self.subOSTakeover.msf_path_checkBox.clicked.connect(lambda : self.openDir(self.subOSTakeover.msf_path_lineEdit))
	
	#Get OSTakeover user's options
	def getOSTakeover(self):
		self.takeoverOpt=""
		#if self.subOSTakeover.os_cmd_groupBox.isChecked():
		if self.subOSTakeover.os_cmd_checkBox.isChecked():
			if self.subOSTakeover.os_cmd_lineEdit.text().isEmpty():
				pass
			else :
				self.takeoverOpt = self.takeoverOpt + "--os-cmd="+self.subOSTakeover.os_cmd_lineEdit.text()
		if self.subOSTakeover.os_shell_checkBox.isChecked():
			self.takeoverOpt = self.takeoverOpt + "  --os-shell "
		#elif self.subOSTakeover.meterpreter_groupBox.isChecked():
		elif self.subOSTakeover.os_pwn_checkBox.isChecked():
			self.takeoverOpt = self.takeoverOpt + "  --os-pwn  "
			if self.subOSTakeover.msf_path_checkBox.isChecked():
				if self.subOSTakeover.msf_path_lineEdit.text().isEmpty():
					pass
				else :
					self.takeoverOpt = self.takeoverOpt + " --msf-path="+ self.subOSTakeover.msf_path_lineEdit.text()
		#elif self.subOSTakeover.reg_groupBox.isChecked():
		if self.subOSTakeover.reg_add_radioButton.isChecked():
			self.takeoverOpt = self.takeoverOpt + " --reg-add "
		if self.subOSTakeover.reg_read_radioButton.isChecked():
			self.takeoverOpt = self.takeoverOpt + " --reg-read "
		if self.subOSTakeover.reg_del_radioButton.isChecked():
			self.takeoverOpt = self.takeoverOpt + " --reg-del "
		if self.subOSTakeover.reg_key_checkBox.isChecked():
			if self.subOSTakeover.reg_key_lineEdit.text().isEmpty():
				self.showdialog("Enter registry access correct data please!")
			else :
				self.takeoverOpt = self.takeoverOpt + "  --reg-key="+self.subOSTakeover.reg_key_lineEdit.text()
		if self.subOSTakeover.reg_value_checkBox.isChecked():
			if self.subOSTakeover.reg_value_lineEdit.text().isEmpty():
				self.showdialog("Enter registry access correct data please!")
			else :
				self.takeoverOpt = self.takeoverOpt + "  --reg-value="+self.subOSTakeover.reg_value_lineEdit.text()
		if self.subOSTakeover.reg_data_checkBox.isChecked():
			if self.subOSTakeover.reg_data_lineEdit.text().isEmpty():
				self.showdialog("Enter registry access correct data please!")
			else :
				self.takeoverOpt = self.takeoverOpt + "  --reg-data="+self.subOSTakeover.reg_data_lineEdit.text()
		if self.subOSTakeover.reg_type_checkBox.isChecked():
			if self.subOSTakeover.reg_type_lineEdit.text().isEmpty():
				self.showdialog("Enter registry access correct data please!")
			else :
				self.takeoverOpt = self.takeoverOpt + "  --reg-type="+self.subOSTakeover.reg_type_lineEdit.text()
		return self.takeoverOpt

	def UDFIOptions(self,scrollArea):
		self.pushB="UDFI"
		self.widgetUdfi = QtGui.QWidget()
		self.subUDFI = Ui_FormUDFI()
		self.subUDFI.setupUi(self)
		self.subUDFI.setupUi(self.widgetUdfi)  
		scrollAreaE =  QtGui.QScrollArea(scrollArea) 
		self.widgetUdfi.setParent(scrollArea)
		scrollAreaE.setWidget(self.widgetUdfi) 
		scrollArea.setWidget(scrollAreaE)
		#scrollArea.setGeometry(QtCore.QRect(120, 20, 680, 210))
		self.widgetUdfi.setGeometry(QtCore.QRect(10, 0, 791, 141))
		self.widgetUdfi.show()
		self.subUDFI.udfi_toolButton.clicked.connect(lambda : self.openDir(self.subUDFI.udfi_lineEdit))

	# Get UDFI user's options
	def getUDFI(self):
		self.udfiOpt=""			
		if self.subUDFI.udfi_checkBox.isChecked():
			self.udfi_L = self.subUDFI.udfi_lineEdit.text()
			self.udfiOpt = self.udfiOpt + " "+ "--udf-inject" + " "+ "--shared-lib="+ self.udfi_L
		return self.udfiOpt
		
	def customInjectionOptions(self,scrollArea):
		self.pushB="Custom"
		self.widgetCustom = QtGui.QWidget()
		self.subCustom = Ui_FormCustom()
		self.subCustom.setupUi(self)
		self.subCustom.setupUi(self.widgetCustom)  
		scrollAreaE =  QtGui.QScrollArea(scrollArea) 
		self.widgetCustom.setParent(scrollArea)
		scrollAreaE.setWidget(self.widgetCustom) 
		scrollArea.setWidget(scrollAreaE)
		#scrollArea.setGeometry(QtCore.QRect(120, 20, 680, 210))
		self.widgetCustom.setGeometry(QtCore.QRect(10, 0, 791, 141))
		self.widgetCustom.show()
		
	def getcustomInjection(self):
		self.customOpt=""			
		if self.subCustom.prefix_checkBox.isChecked():
			if self.subCustom.prefix_lineEdit.text().isEmpty():
				pass
			else :
				if self.subCustom.suffix_checkBox.isChecked():
					if self.subCustom.suffix_lineEdit.text().isEmpty():
						self.showdialog("Enter preffix suffix data please!")
					else :
						suffix = self.subCustom.suffix_lineEdit.text()
						self.customOpt = " "+"--prefix=" +self.subCustom.prefix_lineEdit.text()+" "+"--suffix="+suffix
		return self.customOpt
		
	def openDir(self,lineEdit):
		filenames = QtGui.QFileDialog.getOpenFileName()
		if (filenames.isNull()):
			lineEdit.setText(_translate("ROIGUI", filenames, None))
		else:
			lineEdit.setText(filenames)
	
	def showdialog(self,testo):
		msg = QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Information)
		msg.setText(testo)
#		msg.setInformativeText("This is additional information")
		msg.setWindowTitle("Data input not complete ")
#		msg.setDetailedText("The details are as follows:")
		msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
#		msg.buttonClicked.connect(msgbtn)
		retval = msg.exec_()

	def add_preferences(self):
		self.pref.preferences_save_pushButton.clicked.connect(self.saveprefOptions) 
		self.pref.preferences_discard_pushButton.clicked.connect(self.discardprefOptions) 
		self.pref.pref_auth_file_toolButton.clicked.connect(lambda : self.openDir(self.pref.pref_auth_file_lineEdit))
		self.pref.trafficfile_toolButton.clicked.connect(lambda : self.openDir(self.pref.traffic_file_lineEdit))
		self.pref.output_dir_toolButton.clicked.connect(lambda : self.openDir(self.pref.output_dir_lineEdit))
		self.pref.save_ini_toolButton.clicked.connect(lambda : self.openDir(self.pref.save_ini_lineEdit))
		self.widget.exec_()
		
	def openLog(self):
		self.widgetLog.exec_()
 
	def file_dialog(self):
		fd = QtGui.QFileDialog(self)
		self.filename = fd.getOpenFileName()
		from os.path import isfile
		if isfile(self.filename):
			import codecs
			s = codecs.open(self.filename,'r','utf-8').read()
			self.openlog.plainTextEdit.setPlainText(s)

	def file_save(self):
		from os.path import isfile
		if isfile(self.filename):
			import codecs
			s = codecs.open(self.filename,'w','utf-8')
			s.write(unicode(self.openlog.plainTextEdit.toPlainText()))
			s.close()

		
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	QtGui.QApplication.setStyle("fusion")
	window = MyApp()
	window.show()
	sys.exit(app.exec_())

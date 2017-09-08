# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openlog.ui'
#
# Created: Thu Jun 29 02:22:58 2017
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

class Ui_OpenLog(object):
    def setupUi(self, OpenLog):
        OpenLog.setObjectName(_fromUtf8("OpenLog"))
        OpenLog.setWindowModality(QtCore.Qt.WindowModal)
 #       OpenLog.resize(652, 557)
        OpenLog.resize(QtCore.QSize(QtCore.QRect(0,0,652,557).size()).expandedTo(OpenLog.minimumSizeHint()))
        self.plainTextEdit = QtGui.QTextEdit(OpenLog)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 631, 481))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
 #       self.toolButton = QtGui.QToolButton(OpenLog)
 #       self.toolButton.setGeometry(QtCore.QRect(30, 520, 101, 19))
  #      self.toolButton.setObjectName(_fromUtf8("toolButton"))
   #     self.lineEdit = QtGui.QLineEdit(OpenLog)
    #    self.lineEdit.setGeometry(QtCore.QRect(140, 520, 61, 20))
     #   self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_save = QtGui.QPushButton(OpenLog)
        self.pushButton_save.setGeometry(QtCore.QRect(250, 520, 75, 23))
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.pushButton_open = QtGui.QPushButton(OpenLog)
        self.pushButton_open.setGeometry(QtCore.QRect(340, 520, 75, 23))
        self.pushButton_open.setObjectName(_fromUtf8("pushButton_open"))
        self.pushButton_close = QtGui.QPushButton(OpenLog)
        self.pushButton_close.setGeometry(QtCore.QRect(440, 520, 75, 23))
        self.pushButton_close.setObjectName(_fromUtf8("pushButton_close"))

        self.retranslateUi(OpenLog)
        QtCore.QMetaObject.connectSlotsByName(OpenLog)
        QtCore.QObject.connect(self.pushButton_close,QtCore.SIGNAL("clicked()"),OpenLog.close)

    def retranslateUi(self, OpenLog):
        OpenLog.setWindowTitle(_translate("OpenLog", "OpenLog", None))
 #       self.toolButton.setText(_translate("OpenLog", "openLog", None))
        self.pushButton_save.setText(_translate("OpenLog", "Save", None))
        self.pushButton_open.setText(_translate("OpenLog", "Open", None))
        self.pushButton_close.setText(_translate("OpenLog", "Close", None))


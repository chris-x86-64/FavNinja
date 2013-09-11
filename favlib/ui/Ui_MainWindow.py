# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'favlib/ui/MainWindow.ui'
#
# Created: Thu Sep 12 03:59:32 2013
#      by: PyQt4 UI code generator 4.10
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1024, 768)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tweetButton = QtGui.QPushButton(self.centralwidget)
        self.tweetButton.setGeometry(QtCore.QRect(930, 680, 87, 27))
        self.tweetButton.setObjectName(_fromUtf8("tweetButton"))
        self.tweetToPost = QtGui.QLineEdit(self.centralwidget)
        self.tweetToPost.setGeometry(QtCore.QRect(10, 680, 861, 27))
        self.tweetToPost.setMaxLength(1024)
        self.tweetToPost.setObjectName(_fromUtf8("tweetToPost"))
        self.charCounter = QtGui.QLCDNumber(self.centralwidget)
        self.charCounter.setGeometry(QtCore.QRect(883, 680, 41, 23))
        self.charCounter.setFrameShape(QtGui.QFrame.Panel)
        self.charCounter.setFrameShadow(QtGui.QFrame.Sunken)
        self.charCounter.setNumDigits(3)
        self.charCounter.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.charCounter.setObjectName(_fromUtf8("charCounter"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "FavNinja", None))
        self.tweetButton.setText(_translate("MainWindow", "Tweet!", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))


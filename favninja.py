#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from favlib.ui.MainWindow import MainWindow

def main():
	process = QtGui.QApplication(sys.argv)
	favninja = MainWindow()
	favninja.show()

	sys.exit(process.exec_())

if __name__ == "__main__":
	main()

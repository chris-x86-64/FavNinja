from PyQt4 import QtGui, QtCore
from favlib.ui.Ui_MainWindow import Ui_MainWindow

class MainWindow(QtGui.QMainWindow):
	def __init__(self, parent = None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

from grafo import Grafo
from mwui import Ui_MainWindow
from PyQt4.QtGui import QMainWindow, QWidget
import sys

from PyQt4.QtGui import QApplication

class test(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None, name=None, fl=0):
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

w = test()
w.show()
a = QApplication(sys.argv)
a.exec()

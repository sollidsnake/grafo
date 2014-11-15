from PyQt4 import QtCore, uic
from PyQt4.QtGui import *
from subprocess import call
from uis.uiResultado import Ui_Resultado

class Resultado(QWidget, Ui_Resultado):
    def __init__(self, feliz, mainWindow, parent=None):
        self.mainWindow = mainWindow
        parent = None
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.tbResultado.setText(feliz)
        self.eventos()
        self.show()

    def eventos(self):
        QtCore.QObject.connect(self.pushFechar, QtCore.SIGNAL("clicked()"), self.fechar)

    def centerToMainWindow(self):
        rect = self.mainWindow.frameGeometry()
        center = rect.center()

        self.move(center.x() - self.width() / 2, center.y() - self.height() / 2)

    def fechar(self):
        self.close()

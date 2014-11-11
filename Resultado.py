from PyQt4 import QtCore, uic
from PyQt4.QtGui import *
from subprocess import call

class Resultado(QDialog):
    def __init__(self, feliz, parent=None):
    	if parent:
    		super(Resultado, self).__init__(parent)
    	else:
    		super(Resultado, self).__init__()

    	uic.loadUi('resultado.ui', self)
    	self.tbResultado.setText(feliz)
    	self.eventos()

    def eventos(self):
    	QtCore.QObject.connect(self.pushFechar, QtCore.SIGNAL("clicked()"), self.fechar)

    def fechar(self):
    	self.close()
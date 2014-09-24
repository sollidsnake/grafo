import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
from subprocess import call


class MainWindow(QtGui.QMainWindow):

    def alert(self):
        QtGui.QMessageBox.about(self, "TESTE", "TESTE")

    def addVertice(self):
        vertice = self.lineNomeVertice.text()
        self.modelVertice.appendRow(QStandardItem(vertice))
        self.listVertices.setModel(self.modelVertice)
        self.addToComboVertice(vertice)

    def addAresta(self):
        aresta = self.lineNomeAresta.text()
        self.modelAresta.appendRow(QStandardItem(aresta))
        self.listArestas.setModel(self.modelAresta)
        self.comboAresta.addItem(aresta)

    def addToComboVertice(self, text):
        self.comboVertice1.addItem(text)
        self.comboVertice2.addItem(text)

    def addConexao(self):
        pass

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('mainwindow.ui', self)
        self.modelVertice = QStandardItemModel(self.listVertices)
        self.modelAresta = QStandardItemModel(self.listArestas)
        self.modelConexao = QStandardItemModel(self.listConexoes)

        self.show()
        QtCore.QObject.connect(self.pushAddVertice, QtCore.SIGNAL("clicked()"), self.addVertice)
        QtCore.QObject.connect(self.pushAddAresta, QtCore.SIGNAL("clicked()"), self.addAresta)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

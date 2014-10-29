from PyQt4 import QtCore, uic
from PyQt4.QtGui import *
from subprocess import call
from grafo import Grafo

class MainWindow(QMainWindow):
    matrizAdjacencia = {}
    grafo = Grafo()

    def alert(self):
        QMessageBox.about(self, "TESTE", "TESTE")

    def addVertice(self, vertice):
        self.modelVertice.appendRow(QStandardItem(vertice))
        self.listVertices.setModel(self.modelVertice)
        self.addToComboVertice(vertice)

    def buttonAddVertice(self):
        self.addVertice(self.lineNomeVertice.text())

    def addAresta(self, aresta):
        self.modelAresta.appendRow(QStandardItem(aresta))
        self.listArestas.setModel(self.modelAresta)
        self.comboAresta.addItem(aresta)

    def buttonAddAresta(self):
        self.addAresta(self.lineNomeAresta.text())

    def addToComboVertice(self, text):
        self.comboVertice1.addItem(text)
        self.comboVertice2.addItem(text)

    def addConexao(self, v1, aresta, v2, peso = 1):
        conexao = v1 + '|' + aresta + '|' + v2 + '|' + str(peso)
        self.modelConexao.appendRow(QStandardItem(conexao))
        self.listConexoes.setModel(self.modelConexao)

    def buttonAddConexao(self):
        peso = int(self.linePesoNo.text())
        v1, aresta, v2, peso = self.comboVertice1.currentText(), self.comboAresta.currentText(), self.comboVertice2.currentText(), str(peso)
        self.addConexao(v1, aresta, v2, peso)

    def gerar(self):
        # ['1|2|1|1']
        # v1 | a | v2 | peso

        for indice in range(self.modelConexao.rowCount()):
             item = self.modelConexao.item(indice).text().split('|')
             self.matrizAdjacencia[(item[0], item[2])] = item[3]

        print(self.matrizAdjacencia)


    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('mainwindow.ui', self)
        self.modelVertice = QStandardItemModel(self.listVertices)
        self.modelAresta = QStandardItemModel(self.listArestas)
        self.modelConexao = QStandardItemModel(self.listConexoes)

        QtCore.QObject.connect(self.pushAddVertice, QtCore.SIGNAL("clicked()"), self.buttonAddVertice)
        QtCore.QObject.connect(self.pushAddAresta, QtCore.SIGNAL("clicked()"), self.buttonAddAresta)
        QtCore.QObject.connect(self.pushAddConexao, QtCore.SIGNAL("clicked()"), self.buttonAddConexao)
        QtCore.QObject.connect(self.pushGerar, QtCore.SIGNAL("clicked()"), self.gerar)

    def show(self):
        super().show()

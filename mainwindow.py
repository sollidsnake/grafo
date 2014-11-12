from PyQt4 import QtCore, uic
from PyQt4.QtGui import *
from subprocess import call
from grafo import Grafo
from mwui import Ui_MainWindow

from Resultado import Resultado

class MainWindow(Ui_MainWindow):
    matrizAdjacencia = {}
    grafo = Grafo()

    def alert(self):
        QMessageBox.about(self, "TESTE", "TESTE")

    def addVertice(self, vertice):
        self.modelVertice.appendRow(QStandardItem(vertice))
        self.listVertices.setModel(self.modelVertice)
        self.addToComboVertice(vertice)
        self.grafo.addVertice(vertice)

    def buttonAddVertice(self):
        self.addVertice(self.lineNomeVertice.text())

    def addAresta(self, aresta):
        self.modelAresta.appendRow(QStandardItem(aresta))
        self.listArestas.setModel(self.modelAresta)
        self.comboAresta.addItem(aresta)
        self.grafo.addAresta(aresta)

    def buttonAddAresta(self):
        self.addAresta(self.lineNomeAresta.text())

    def addToComboVertice(self, text):
        self.comboVertice1.addItem(text)
        self.comboVertice2.addItem(text)
        self.comboCaminhoInicio.addItem(text)
        self.comboCaminhoFim.addItem(text)

    def addConexao(self, v1, aresta, v2, peso = 1):
        conexao = v1 + '|' + aresta + '|' + v2 + '|' + str(peso)
        self.modelConexao.appendRow(QStandardItem(conexao))
        self.grafo.addConexao(v1, aresta, v2, peso)
        self.listConexoes.setModel(self.modelConexao)

    def buttonAddConexao(self):
        peso = int(self.linePesoNo.text())
        v1, aresta, v2, peso = self.comboVertice1.currentText(), self.comboAresta.currentText(), self.comboVertice2.currentText(), str(peso)
        self.addConexao(v1, aresta, v2, peso)

    def gerar(self):
        # ['1|2|1|1']
        # v1 | a | v2 | peso

        resList = []

        if self.checkDirecionado.isChecked():
            self.grafo.setDirecionado(True)

        if self.checkExisteLaco.isChecked():
            if self.grafo.existeLaco():
                resList.append("Existem lacos no grafo.")
            else:
                resList.append("Nao existem lacos no grafo.")

        if self.checkExisteParalela.isChecked():
            if self.grafo.existeArestaParalela():
                resList.append("Existem arestas paralelas")
            else:
                resList.append("Nao existem arestas paralelas")

        if self.checkExisteIsolado.isChecked():
            if self.grafo.existeVerticeIsolado():
                resList.append("Existem vertices isolados")
            else:
                resList.append("Nao existem vertices isolados")

        if self.checkOrdem.isChecked():
            resList.append("Ordem do grafo: " + str(self.grafo.getOrdem()))

        if self.checkExisteCiclo.isChecked():
            resList.append("Ciclos ainda nao implementado")

        if self.checkConexo.isChecked():
            resList.append("Grafo conexo ainda nao implementado")

        if self.checkCaminhoCurto.isChecked():
            v1 = self.comboCaminhoInicio.currentText()
            v2 = self.comboCaminhoFim.currentText()
            if self.grafo.existeCaminho(v1, v2):
                resList.append("Existe caminho entre o nó '" + v1 + "' e '" + v2 +"'")
            else:
                resList.append("Nao existe caminho entre o nó '" + v1 + "' e '" + v2 +"'")

        if self.checkGrau.isChecked():
            graus = self.grafo.getTodosGraus()
            resList.append("Grau de cada no:")
            for v in graus.keys():
                resList.append("'" + v + "':" + str(graus[v]))
            resList.append("")

        resultado = Resultado("\n".join(resList), self.qmw)
        resultado.show()

    def __init__(self, qmw, parent=None, name=None, fl=0):
        Ui_MainWindow.__init__(self)
        Ui_MainWindow.setupUi(self, qmw)
        self.qmw = qmw

        # uic.loadUi('mainwindow.ui', self)

        # self.listVertices.setEditTriggers(QApplication.NoEditTriggers)

        self.modelVertice = QStandardItemModel(self.listVertices)
        self.modelAresta = QStandardItemModel(self.listArestas)
        self.modelConexao = QStandardItemModel(self.listConexoes)

        QtCore.QObject.connect(self.pushAddVertice, QtCore.SIGNAL("clicked()"), self.buttonAddVertice)
        QtCore.QObject.connect(self.pushAddAresta, QtCore.SIGNAL("clicked()"), self.buttonAddAresta)
        QtCore.QObject.connect(self.pushAddConexao, QtCore.SIGNAL("clicked()"), self.buttonAddConexao)
        QtCore.QObject.connect(self.pushGerar, QtCore.SIGNAL("clicked()"), self.gerar)

    def show(self):
        super().show()

from PyQt4 import QtCore, uic
from PyQt4.QtGui import *
from subprocess import call
from grafo import Grafo
from uis.uiMainwindow import Ui_MainWindow
from sobre import SobreUi
import pdb

from resultado import Resultado

def debug_trace():
    '''Set a tracepoint in the Python debugger that works with Qt'''
    from PyQt4.QtCore import pyqtRemoveInputHook
    from pdb import set_trace
    pyqtRemoveInputHook()
    set_trace()

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
        try:
            peso = int(self.linePesoNo.text())
        except:
            peso = 1

        v1, v2 = self.comboVertice1.currentText(), self.comboVertice2.currentText()
        aresta = self.comboAresta.currentText()

        self.addConexao(v1, aresta, v2, peso)

    def gerar(self):
        # ['1|2|1|1']
        # v1 | a | v2 | peso

        resList = []

        if self.checkDirecionado.isChecked():
            self.grafo.setDirecionado(True)
        else:
            self.grafo.setDirecionado(False)

        if self.checkExisteLaco.isChecked():
            if self.grafo.existeLaco():
                resList.append("- Existem lacos no grafo.")
            else:
                resList.append("- Nao existem lacos no grafo.")

        if self.checkExisteParalela.isChecked():
            if self.grafo.existeArestaParalela():
                resList.append("- Existem arestas paralelas")
            else:
                resList.append("- Nao existem arestas paralelas")

        if self.checkExisteIsolado.isChecked():
            if self.grafo.existeVerticeIsolado():
                resList.append("- Existem vertices isolados")
            else:
                resList.append("- Nao existem vertices isolados")

        if self.checkOrdem.isChecked():
            resList.append("- Ordem do grafo: " + str(self.grafo.getOrdem()))

        if self.checkExisteCiclo.isChecked():
            ciclos = self.grafo.getCiclos()

            if ciclos:
                resList.append("- Existe(m) ciclo(s) para o(s) vértice(s): " + ", ".join(ciclos))
            else:
                resList.append("- Nao existem ciclos no grafo")

        if self.checkConexo.isChecked():
            if self.grafo.isConexo():
                resList.append("- Grafo é conexo")
            else:
                resList.append("- Grafo não é conexo")

        if self.checkCaminhoCurto.isChecked():
            v1 = self.comboCaminhoInicio.currentText()
            v2 = self.comboCaminhoFim.currentText()
            if self.grafo.existeCaminho(v1, v2, []):
                resList.append("- Existe caminho entre o vértice '" + v1 + "' e '" + v2 +"'")
            else:
                resList.append("- Nao existe caminho entre o vértice '" + v1 + "' e '" + v2 +"'")

        if self.checkGrau.isChecked():
            graus = self.grafo.getTodosGraus()
            if self.grafo.isDirecionado:
                resList.append("- Grau de cada vértice (emissão, recepção):")
            else:
                resList.append("- Grau de cada vértice:")

            for v in graus.keys():
                if self.grafo.isDirecionado:
                    resList.append("  '" + v + "': " + str(graus[v][0]) + ", " + str(graus[v][1]))
                else:
                    resList.append("  '" + v + "': " + str(graus[v]))
            resList.append("")

        if self.checkAdjacencia.isChecked():
            adjacencias = self.grafo.getTodasAdjacencias()
            resList.append("- Adjacências de cada vértice:")
            for v in adjacencias.keys():
                strAdj = "" + v + ": "
                verticesAdj = []
                for arestaAdj, vertAdj in adjacencias[v]:
                    verticesAdj.append(vertAdj)
                if verticesAdj:
                    resList.append(strAdj + ", ".join(verticesAdj))
                else:
                    resList.append(strAdj + "Nenhum")

        resultado = Resultado("\n".join(resList), self.qmw)
        resultado.centerToMainWindow()
        self.resultados.append(resultado)

    def buttonRemoveVertice(self):
        index = self.listVertices.currentIndex()
        text = self.modelVertice.itemFromIndex(index).text()
        self.removeVertice({'index': index.row(), 'value': text})

    def removeVertice(self, v):
        self.grafo.removeVertice(v['value'])
        self.modelVertice.removeRow(v['index'])

        eraseFrom = [self.comboVertice1,self.comboVertice2,self.comboCaminhoInicio,self.comboCaminhoFim]
        for combo in eraseFrom:
            combo.removeItem(combo.findText(v['value']))

        # for i in self.comboVertice1.count():
            # pass

        toErase = []
        for i in range(self.modelConexao.rowCount()):
            item = self.modelConexao.item(i)
            values = item.text().split('|')
            if values[0] == str(v['value']) or values[2] == str(v['value']):
                toErase.append(item)

        for item in toErase:
            index = self.modelConexao.indexFromItem(item)
            if False: index = QStandardItem
            self.modelConexao.removeRow(index.row())

    def removeConexao(self, a):
        self.grafo.removeConexao(a['value'].split('|')[1])
        self.modelConexao.removeRow(a['index'])

    def removeAresta(self, a):
        self.grafo.removeAresta(a['value'])
        self.modelAresta.removeRow(a['index'])

        self.comboAresta.removeItem(self.comboVertice2.findText(a['value']))

        toErase = []
        for i in range(self.modelConexao.rowCount()):
            item = self.modelConexao.item(i)
            values = item.text().split('|')
            if values[1] == str(a['value']):
                toErase.append(item)

        for item in toErase:
            index = self.modelConexao.indexFromItem(item)
            if False: index = QStandardItem
            self.modelConexao.removeRow(index.row())

    def listVerticesClicked(self, model):
        if False: model = QStandardItem
        self.modelVertice.removeRow(model.row())

    def __init__(self, qmw, parent=None, name=None, fl=0):
        if False: qmw = QMainWindow
        self.resultados = []
        Ui_MainWindow.__init__(self)
        Ui_MainWindow.setupUi(self, qmw)
        self.qmw = qmw

        self.menuArquivo.setTitle("&Arquivo")

        # uic.loadUi('mainwindow.ui', self)

        # self.listVertices.setEditTriggers(QApplication.NoEditTriggers)

        self.modelVertice = QStandardItemModel(self.listVertices)
        self.modelAresta = QStandardItemModel(self.listArestas)
        self.modelConexao = QStandardItemModel(self.listConexoes)

        self.sobreUi = SobreUi(self.qmw)
        self.sobreUi.tbAbout.setText("desenvolvido por mim")

        self.events()

    def buttonRemoveAresta(self):
        index = self.listArestas.currentIndex()
        text = self.modelAresta.itemFromIndex(index).text()
        self.removeAresta({'index': index.row(), 'value': text})

    def buttonRemoveConexao(self):
        index = self.listConexoes.currentIndex()
        text = self.modelConexao.itemFromIndex(index).text()
        self.removeConexao({'index': index.row(), 'value': text})

    def events(self):
        QtCore.QObject.connect(self.pushAddVertice,
                               QtCore.SIGNAL("clicked()"),
                               self.buttonAddVertice)
        QtCore.QObject.connect(self.pushAddAresta,
                               QtCore.SIGNAL("clicked()"),
                               self.buttonAddAresta)
        QtCore.QObject.connect(self.pushAddConexao,
                               QtCore.SIGNAL("clicked()"),
                               self.buttonAddConexao)
        QtCore.QObject.connect(self.pushRemoverVertice,
                               QtCore.SIGNAL("clicked()"),
                               self.buttonRemoveVertice)
        QtCore.QObject.connect(self.pushRemoverAresta,
                               QtCore.SIGNAL("clicked()"),
                               self.buttonRemoveAresta)
        QtCore.QObject.connect(self.pushRemoveConexao,
                               QtCore.SIGNAL("clicked()"),
                               self.buttonRemoveConexao)

        QtCore.QObject.connect(self.pushGerar, QtCore.SIGNAL("clicked()"), self.gerar)
        self.actionSobre.triggered.connect(self.showSobreUi)
        self.actionSair.triggered.connect(self.sair)

    def showSobreUi(self):
        self.sobreUi.show()
        self.sobreUi.centerToMainWindow()

    def sair(self):
        self.qmw.close()

    def show(self):
        super().show()

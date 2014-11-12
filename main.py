#!/usr/bin/env python3

from PyQt4.QtGui import QApplication, QMainWindow
import sys
from mainwindow import MainWindow
from Resultado import Resultado

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qmw = QMainWindow()
    window = MainWindow(qmw)

    # inserir para teste
    window.addAresta('a')
    window.addAresta('b')
    window.addAresta('c')
    window.addVertice('1')
    window.addVertice('2')
    window.addVertice('3')
    window.addConexao('1', 'a', '2')
    window.addConexao('1', 'b', '3')
    window.addConexao('3', 'c', '3')

    # chama a janela
    qmw.show()
    #resultado = Resultado("")
    #resultado.showMaximized()

    sys.exit(app.exec_())

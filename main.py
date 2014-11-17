#!/usr/bin/env python3

from PyQt4.QtGui import QApplication, QMainWindow
import sys
from mainwindow import MainWindow
from resultado import Resultado

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = MainWindow()

    # inserir para teste
    # window.addAresta('a')
    # window.addAresta('b')
    # window.addAresta('c')
    # window.addVertice('1')
    # window.addVertice('2')
    # window.addVertice('3')
    # window.addConexao('1', 'a', '2')
    # window.addConexao('1', 'b', '3')
    # window.addConexao('3', 'c', '3')

    # chama a janela principal
    wind.show()

    sys.exit(app.exec_())

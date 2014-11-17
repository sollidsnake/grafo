#!/usr/bin/env python3

from PyQt4.QtGui import QApplication, QMainWindow
import sys
from mainwindow import MainWindow
from resultado import Resultado

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = MainWindow()

    # inserir para teste
    wind.addAresta('a')
    wind.addAresta('b')
    wind.addAresta('c')
    wind.addVertice('1')
    wind.addVertice('2')
    wind.addVertice('3')
    wind.addConexao('1', 'a', '2')
    wind.addConexao('1', 'b', '3')
    wind.addConexao('3', 'c', '3')

    # chama a janela principal
    wind.show()

    sys.exit(app.exec_())

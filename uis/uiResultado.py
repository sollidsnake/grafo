# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/resultado.ui'
#
# Created: Sun Nov 16 19:20:24 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Resultado(object):
    def setupUi(self, Resultado):
        Resultado.setObjectName(_fromUtf8("Resultado"))
        Resultado.resize(340, 381)
        self.gridLayout = QtGui.QGridLayout(Resultado)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tbResultado = QtGui.QTextBrowser(Resultado)
        self.tbResultado.setTabStopWidth(40)
        self.tbResultado.setObjectName(_fromUtf8("tbResultado"))
        self.gridLayout.addWidget(self.tbResultado, 0, 0, 1, 1)
        self.pushFechar = QtGui.QPushButton(Resultado)
        self.pushFechar.setObjectName(_fromUtf8("pushFechar"))
        self.gridLayout.addWidget(self.pushFechar, 1, 0, 1, 1)

        self.retranslateUi(Resultado)
        QtCore.QMetaObject.connectSlotsByName(Resultado)

    def retranslateUi(self, Resultado):
        Resultado.setWindowTitle(_translate("Resultado", "Resultado", None))
        self.pushFechar.setText(_translate("Resultado", "&Fechar", None))


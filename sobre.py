from uis.uiAbout import Ui_Form
from PyQt4 import QtGui
from PyQt4.Qt import Qt
from PyQt4 import QtCore

class SobreUi(QtGui.QWidget, Ui_Form):

    def __init__(self, mainWindow, parent=None):
        self.mainWindow = mainWindow
        QtGui.QWidget.__init__(self, parent)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setupUi(self)

        self.setWindowFlags(Qt.WindowCloseButtonHint)

        QtCore.QObject.connect(self.pushFechar,
                               QtCore.SIGNAL("clicked()"), self.fechar)

    def centerToMainWindow(self):
        rect = self.mainWindow.frameGeometry()
        center = rect.center()

        self.move(center.x() - self.width() / 2, center.y() - self.height() / 2)

    def fechar(self):
        self.close()

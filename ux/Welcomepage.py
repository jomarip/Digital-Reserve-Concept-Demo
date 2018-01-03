import sys
from PyQt5 import QtCore, QtGui, uic , QtWidgets
from PyQt5.QtWidgets import QLabel
from genseed2 import GenerateSeed
from PyQt5.QtGui import QIcon, QPixmap

qtCreatorFile = "Welcome.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,MainWindow):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Lite_node.clicked.connect(self.LiteNode)
        self.Full_node.clicked.connect(self.FullNode)

        self.label = QLabel(self)
        pixmap = QPixmap('drl.png')
        self.label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height()) 

    def LiteNode(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = GenerateSeed()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def FullNode(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = GenerateSeed()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyApp()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

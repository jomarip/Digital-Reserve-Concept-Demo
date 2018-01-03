import sys
from PyQt5 import QtCore, QtGui, QtWidgets , uic
from generatekey1 import nouns
import random

qtCreatorFile = "generateseed.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class GenerateSeed(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.gen_seed.clicked.connect(self.GenSeed)

    def GenSeed(self):
        seed = " ".join([nouns[random.randrange(0, len(nouns))] for i in range(16)])
        f = open('digitalreserveseed.txt','w')
        f.write(" ".join([nouns[random.randrange(0, len(nouns))] for i in range(16)]))
        f.close()

        self.window = QtWidgets.QMainWindow()
        self.ui = GenerateSeed()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
  
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    SeedWindow = QtWidgets.QMainWindow()
    ui = GenerateSeed()
    ui.setupUi(SeedWindow)
    SeedWindow.show()
    sys.exit(app.exec_())

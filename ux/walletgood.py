import sys
from PyQt5 import QtCore, QtGui, QtWidgets , uic
from generatekey1 import nouns

qtCreatorFile = "walletmain2.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class WalletMain(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.dashboard_button.clicked.connect(self.dashBoard)
        self.stake_button.clicked.connect(self.stake)
        self.borrow_button.clicked.connect(self.borrow)
        self.send_button.clicked.connect(self.sendDenarii)
        self.request_button.clicked.connect(self.requestDenarii)

    def dashBoard(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = GenerateSeed()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def stake(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = GenerateSeed()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def borrow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = GenerateSeed()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def sendDenarii(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = GenerateSeed()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def requestDenarii(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = GenerateSeed()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
  
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    WalletWindow = QtWidgets.QMainWindow()
    ui = WalletMain()
    ui.setupUi(WalletWindow)
    WalletWindow.show()
    sys.exit(app.exec_())

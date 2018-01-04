import sys
from PyQt5 import QtCore, QtGui, QtWidgets , uic
from generatekey1 import nouns
from genpublicprivatekey import *
import random

qtCreatorFile = "publicprivatekeypage.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class pubPrivateKey(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self, MainWindow)
        self.public_private_button.clicked.connect(self.Genpubpriv)

    def Genpubpriv(self):
        makeKeyFiles('Digital_Reserve', 512)
        p = rabinMiller.generateLargePrime(keySize)
        q = rabinMiller.generateLargePrime(keySize)
        n = p * q

        # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
        print('Generating e that is relatively prime to (p-1)*(q-1)...')
        while True:
            # Keep trying random numbers for e until one is valid.
            e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
            if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
                break
        
        # Step 3: Calculate d, the mod inverse of e.
        print('Calculating d that is mod inverse of e...')
        d = cryptomath.findModInverse(e, (p - 1) * (q - 1))

        publicKey = (n, e)
        privateKey = (n, d)

        print('Public key:', publicKey)
        print('Private key:', privateKey)

        return (publicKey, privateKey)

        if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
            sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete these files and re-run this program.' % (name, name))

        publicKey, privateKey = generateKey(keySize)

        print()
        print('The public key is a %s and a %s digit number.' %
(len(str(publicKey[0])), len(str(publicKey[1]))))
        print('Writing public key to file %s_pubkey.txt...' % (name))
        fo = open('%s_pubkey.txt' % (name), 'w')
        fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))

        fo.close()

        print()
        print('The private key is a %s and a %s digit number.' %
(len(str(publicKey[0])), len(str(publicKey[1]))))
        print('Writing private key to file %s_privkey.txt...' % (name))
        fo = open('%s_privkey.txt' % (name), 'w')
        fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
        fo.close()

       

        self.window = QtWidgets.QMainWindow()
        self.ui = GenerateSeed()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
  
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    pubprivwindow = QtWidgets.QMainWindow()
    ui = pubPrivateKey
    ui.setupUi(pubprivwindow)
    pubprivwindow.show()
    sys.exit(app.exec_())

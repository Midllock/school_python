import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

class Encryptor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # vytvoření tlačítek a výběru souboru
        self.setGeometry(100, 100, 350, 200)
        self.setWindowTitle('Souborový šifrování')
        self.browseButton = QPushButton('Vybrat soubor', self)
        self.browseButton.clicked.connect(self.browseFile)
        self.encryptButton = QPushButton('Šifrovat soubor', self)
        self.encryptButton.clicked.connect(self.encryptFile)
        self.decryptButton = QPushButton('Dešifrovat soubor', self)
        self.decryptButton.clicked.connect(self.decryptFile)
        self.passwordLabel = QLabel('Zadejte heslo:', self)
        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.filePathLabel = QLabel('', self)
        self.filePathLabel.setWordWrap(True)

        # uspořádání ovládacích prvků v okně
        layout = QVBoxLayout()
        layout.addWidget(self.browseButton)
        layout.addWidget(self.filePathLabel)
        layout.addWidget(self.passwordLabel)
        layout.addWidget(self.passwordEdit)
        layout.addWidget(self.encryptButton)
        layout.addWidget(self.decryptButton)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def browseFile(self):
        # výběr souboru pomocí dialogového okna
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Vyberte soubor", "", "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            self.filePathLabel.setText(fileName)

    def encryptFile(self):
        # kontrola, zda je vybrán soubor a zadané heslo
        if self.filePathLabel.text() == '':
            QMessageBox.warning(self, 'Chyba', 'Vyberte soubor pro šifrování.')
            return
        if self.passwordEdit.text() == '':
            QMessageBox.warning(self, 'Chyba', 'Zadejte heslo pro šifrování.')
            return

    def decryptFile(self):
        # kontrola, zda je vybrán soubor a zadané heslo
        if self.filePathLabel.text() == '':
            QMessageBox.warning(self, 'Chyba', 'Vyberte soubor pro dešifrování.')
            return
        if self.passwordEdit.text() == '':
            QMessageBox.warning(self, 'Chyba', 'Zadejte heslo pro dešifrování.')
            return

#Otevři příkazovou řádku/cmd/terminál
#Přejdi do složky, kde se nachází soubor se skriptem (použij příkaz cd)
#Napiš příkaz python jméno_souboru.py, kde "jméno_souboru.py" je název tvého souboru se skriptem.
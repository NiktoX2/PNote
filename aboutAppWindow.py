from PyQt5.QtWidgets import *

class aboutAppWindow(QDialog):
    def __init__(self, parent=None):
        super(aboutAppWindow, self).__init__(parent)

        self.pushButton = QPushButton(self)
        self.pushButton.clicked.connect(self.btnClosed)
        self.setWindowTitle("Об приложение")
        self.resize(300, 150)

    def btnClosed(self):
        self.close()
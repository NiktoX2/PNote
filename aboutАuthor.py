from PyQt5.QtWidgets import *

class aboutАuthor(QDialog):
    def __init__(self, parent=None):
        super(aboutАuthor, self).__init__(parent)

        self.pushButton = QPushButton(self)
        self.pushButton.clicked.connect(self.btnClosed)
        self.setWindowTitle("Автор")
        self.resize(300, 150)

    def btnClosed(self):
        self.close()
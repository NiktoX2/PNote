from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot


class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('mainWindow.ui', self)
        self.setWindowTitle("Блокнот")
        self.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.setMinimumSize(220, 200)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.closse.clicked.connect(self.closeApp)
        self.setting.clicked.connect(self.openSetting)
        self.open.clicked.connect(self.openFile)
        self.open.setShortcut("Ctrl+O")
        self.seve.clicked.connect(self.saveFile)
        self.seve.setShortcut("Ctrl+S")
        self.winSetting = openWindowSetting()
        self.dragPos = QtCore.QPoint()
        self.f = self.textEdit.font()
        self.f = QtGui.QFont("Arial", 16)
        self.textEdit.setFont(self.f)

        self.fileSeve = None

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def closeApp(self):
        self.close()

    def openSetting(self):
        self.winSetting.show()

    @pyqtSlot()
    def openFile(self):
        falname = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть", '', "Все файлы (*.*);;Текстовый файл (*.txt);;Python файлы (*.py)")[0]
        try:
            file = open(falname, 'r', encoding='utf-8')
            with file:
                data = file.read()
                self.textEdit.setText(data)
            file.close()
        except FileNotFoundError:
            pass

    @pyqtSlot()
    def saveFile(self):
        if self.fileSeve is None:
            self.falnameRu = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить", '', 'Текстовый файл (*.txt);;Python файлы (*.py);;lost (*.niktox2)')[0]
            try:
                file = open(self.falnameRu, 'w', encoding='utf-8')
                text = self.textEdit.toPlainText()
                file.write(text)
                file.close()
            except FileNotFoundError:
                pass
            self.fileSeve = 1
        else:
            file = open(self.falnameRu, 'w', encoding='utf-8')
            text = self.textEdit.toPlainText()
            file.write(text)
            file.close()


class openWindowSetting(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('settingWindow.ui', self)
        self.setWindowTitle("Настройки")
        self.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.no.clicked.connect(self.closeApp)
        self.yes.clicked.connect(self.closeApp)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def closeApp(self):
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = mainWindow()
    main.show()
    app.exec_()

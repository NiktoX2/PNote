from PyQt5 import QtCore, QtGui, QtWidgets, uic


class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('mainWindow.ui', self)
        self.setMinimumSize(220, 200)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.closse.clicked.connect(self.closeApp)
        self.setting.clicked.connect(self.openSetting)
        self.winSetting = openWindowSetting()
        self.dragPos = QtCore.QPoint()
        self.f = self.textEdit.font()
        self.f = QtGui.QFont("Arial", 16)
        self.textEdit.setFont(self.f)

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


class openWindowSetting(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('settingWindow.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
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

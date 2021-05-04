from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Window(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.resize(700, 400)
        self.setWindowTitle("Блокнот")
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        f = self.text_edit.font()
        f.setPointSize(16)
        self.text_edit.setFont(f)

        self.styleFont = self.text_edit

        self.Toolbar()
        self.Menubar()
        self.appStile()

    def Menubar(self):
        self.menubar = self.menuBar()
        self.file = self.menubar.addMenu("Файл")
        self.setting = self.menubar.addMenu("Настройки")
        self.lang = self.menubar.addMenu("Язык")
        self.about = self.menubar.addMenu("Помощь")

        self.file.addAction(self.newAction)
        self.file.addAction(self.openAction)
        self.file.addAction(self.saveAction)

        self.setting.addAction(self.fontAction)

        self.lang.addAction(self.langRu)
        self.lang.addAction(self.langEng)

        self.about.addAction(self.aboutAuthor)
        self.about.addAction(self.aboutApp)

    def Toolbar(self):
        self.newAction = QAction("Новый файл", self)
        self.newAction.triggered.connect(self.new)
        self.newAction.setShortcut("Ctrl+N")

        self.openAction = QAction("Открыть", self)
        self.openAction.triggered.connect(self.open)
        self.openAction.setShortcut("Ctrl+O")

        self.saveAction = QAction("Сохранить", self)
        self.saveAction.triggered.connect(self.save)
        self.saveAction.setShortcut("Ctrl+S")

        self.fontAction = QAction("Шрифт", self)
        self.fontAction.triggered.connect(self.fontText)

        self.langRu = QAction("Ru", self)
        self.langRu.triggered.connect(self.setLangRu)
        self.langEng = QAction("Eng", self)
        self.langEng.triggered.connect(self.setLangEng)

        self.aboutAuthor = QAction("Автор", self)
        self.aboutAuthor.triggered.connect(self.openAboutAuthor)
        self.aboutApp = QAction("Об приложении", self)
        self.aboutApp.triggered.connect(self.openAboutApp)

    def new(self):
        window = Window(self)
        window.show()

    @pyqtSlot()
    def open(self):
        falname = QFileDialog.getOpenFileName(self, 'Открыть файл', '',
                                              'Все файлы (*.*);;Текстовый файл (*.txt);;Python файлы (*.py)')[0]
        try:
            fa = open(falname, 'r')
            with fa:
                data = fa.read()
                self.text_edit.setText(data)
            fa.close()
        except FileNotFoundError:
            print("Отмена")

    @pyqtSlot()
    def save(self):
        falname = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                              'Все файлы (*.*);;Текстовый файл (*.txt);;Python файлы (*.py)')[0]
        try:
            fa = open(falname, 'w')
            text = self.text_edit.toPlainText()
            fa.write(text)
            fa.close()
        except FileNotFoundError:
            print("Отмена")

    @pyqtSlot()
    def fontText(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.styleFont.setFont(font)

    def setLangRu(self):
        translate = QCoreApplication.translate
        self.setWindowTitle(translate("self", "Блокнот"))

        self.file.setTitle(translate("self", "Файл"))
        self.newAction.setText(translate("self", "Новый файл"))
        self.openAction.setText(translate("self", "Открыть"))
        self.saveAction.setText(translate("self", "Сохранить"))

        self.setting.setTitle(translate("self", "Настройки"))
        self.fontAction.setText(translate("self", "Шрифт"))

        self.lang.setTitle(translate("self", "Язык"))

        self.about.setTitle(translate("self", "Помощь"))

    def setLangEng(self):
        translate = QCoreApplication.translate
        self.setWindowTitle(translate("self", "Note"))

        self.file.setTitle(translate("self", "File"))
        self.newAction.setText(translate("self", "New"))
        self.openAction.setText(translate("self", "Open"))
        self.saveAction.setText(translate("self", "Save"))

        self.setting.setTitle(translate("self", "Setting"))
        self.fontAction.setText(translate("self", "Font"))

        self.lang.setTitle(translate("self", "Lang"))

        self.about.setTitle(translate("self", "Help"))

    def appStile(self):
        self.setStyleSheet("background-color: #000")
        self.text_edit.setStyleSheet('''color: #fff; border-style: none''')
        self.menubar.setStyleSheet('''color: #fff; background-color: #000''')
        self.file.setStyleSheet('''color: #fff; background-color: #000''')
        self.setting.setStyleSheet('''color: #fff; background-color: #000''')

    def openAboutAuthor(self):
        textAboutAuthor = "Автор:<br/>" \
                         "NiktoX2 (НиктоХ2)<br/>" \
                         "Интернет"

        self.msgBoxAboutAuthor = QMessageBox()
        self.msgBoxAboutAuthor.setText(textAboutAuthor)
        self.msgBoxAboutAuthor.setWindowTitle("Автор")
        self.msgBoxAboutAuthor.exec()

    def openAboutApp(self):
        text_about_app = "Блокнот<br/>" \
                         "Версия 1.0" \
                         ""
        self.msgBoxAboutApp = QMessageBox()
        self.msgBoxAboutApp.setText(text_about_app)
        self.msgBoxAboutApp.setWindowTitle("Об приложении")
        self.msgBoxAboutApp.exec()

def appstart():
    import sys
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    appstart()

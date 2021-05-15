import webbrowser

from PyQt5.QtCore import pyqtSlot
import PyQt5.QtWidgets
from PyQt5.QtGui import QFont

textAboutAppRu = "Блокнот<br/>Версия 1.0<br/>Автор: NiktoX2 (НиктоХ2)<br/>"
textAboutAppEng = "Note<br/>Version 1.0<br/>Author: NiktoX2 (НиктоХ2)<br/>"
openFileSelectionRu = 'Все файлы (*.*);;Текстовый файл (*.txt);;Python файлы (*.py)'
openFileSelectionEng = 'All files (*.*);;Text file (*.txt);;Python файлы (*.py)'
saveFileSelectionRu = 'Текстовый файл (*.txt);;Python файлы (*.py);;lost (*.niktox2)'
saveFileSelectionEng = 'Text file (*.txt);;Python files (*.py);;lost (*.niktox2)'


class Window(PyQt5.QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        PyQt5.QtWidgets.QMainWindow.__init__(self, parent)
        # размер / имя / текстовый редактор
        self.resize(700, 400)
        # self.setWindowTitle("Блокнот")
        self.text_edit = PyQt5.QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # по умолчанию размер
        self.f = self.text_edit.font()
        self.f.setPointSize(16)
        self.f.setFamily("Arial")
        self.text_edit.setFont(self.f)

        # установка стиля для редактора
        self.styleFont = self.text_edit

        # menu
        self.menubar = self.menuBar()
        self.file = self.menubar.addMenu("")
        # self.file = self.menubar.addMenu("Файл")
        self.setting = self.menubar.addMenu("")
        # self.setting = self.menubar.addMenu("Настройки")
        self.lang = self.menubar.addMenu("")
        # self.lang = self.menubar.addMenu("Язык")
        self.about = self.menubar.addMenu("")
        # self.about = self.menubar.addMenu("Помощь")

        # Toolbar
        self.newAction = PyQt5.QtWidgets.QAction("", self)
        # self.newAction = PyQt5.QtWidgets.QAction("Новый файл", self)
        self.openAction = PyQt5.QtWidgets.QAction("", self)
        # self.openAction = PyQt5.QtWidgets.QAction("Открыть", self)
        self.saveAction = PyQt5.QtWidgets.QAction("", self)
        # self.saveAction = PyQt5.QtWidgets.QAction("Сохранить", self)
        self.fontAction = PyQt5.QtWidgets.QAction("", self)
        # self.fontAction = PyQt5.QtWidgets.QAction("Шрифт", self)
        self.langRu = PyQt5.QtWidgets.QAction("Ru", self)
        self.langEng = PyQt5.QtWidgets.QAction("Eng", self)
        self.aboutApp = PyQt5.QtWidgets.QAction("", self)
        # self.aboutApp = PyQt5.QtWidgets.QAction("Об приложении", self)
        self.siteVk = PyQt5.QtWidgets.QAction("", self)
        # self.siteVk = PyQt5.QtWidgets.QAction("Vk Автора", self)
        self.siteGithub = PyQt5.QtWidgets.QAction("", self)
        # self.siteGithub = PyQt5.QtWidgets.QAction("Исходный код (Github)", self)
        self.msgBoxAboutAuthor = PyQt5.QtWidgets.QMessageBox()
        self.msgBoxAboutApp = PyQt5.QtWidgets.QMessageBox()

        # variables язык \почти/ по умолчанию
        # rus = 0, "rus"
        # eng = 1, "eng"
        # запуск с выбраным языком
        self.setGlobalLang = 0
        # переключение языка в приложении
        self.langVariables = self.setGlobalLang

        # подключить
        self.Toolbar()
        self.Menubar()
        self.appStile()

        if self.setGlobalLang == 0:
            self.setWindowTitle("Блокнот")
            self.file.setTitle("Файл")
            self.newAction.setText("Новый файл")
            self.openAction.setText("Открыть")
            self.saveAction.setText("Сохранить")
            self.setting.setTitle("Настройки")
            self.fontAction.setText("Шрифт")
            self.lang.setTitle("Язык")
            self.about.setTitle("Помощь")
            self.aboutApp.setText("Об приложении")
            self.siteVk.setText("Vk Автора")
            self.siteGithub.setText("Исходный код (Github)")
        else:
            self.setWindowTitle("Note")
            self.file.setTitle("File")
            self.newAction.setText("New")
            self.openAction.setText("Open")
            self.saveAction.setText("Save")
            self.setting.setTitle("Setting")
            self.fontAction.setText("Font")
            self.lang.setTitle("Lang")
            self.about.setTitle("Help")
            self.aboutApp.setText("About the app")
            self.siteVk.setText("Vk About")
            self.siteGithub.setText("Source (Github)")

    def Menubar(self):
        self.file.addAction(self.newAction)
        self.file.addAction(self.openAction)
        self.file.addAction(self.saveAction)
        self.setting.addAction(self.fontAction)
        self.lang.addAction(self.langRu)
        self.lang.addAction(self.langEng)
        self.about.addAction(self.aboutApp)
        self.about.addAction(self.siteVk)
        self.about.addAction(self.siteGithub)

    def Toolbar(self):
        self.newAction.triggered.connect(self.new)
        self.newAction.setShortcut("Ctrl+N")
        self.openAction.triggered.connect(self.open)
        self.openAction.setShortcut("Ctrl+O")
        self.saveAction.triggered.connect(self.save)
        self.saveAction.setShortcut("Ctrl+S")
        self.fontAction.triggered.connect(self.fontText)
        self.langRu.triggered.connect(self.setLangRu)
        self.langEng.triggered.connect(self.setLangEng)
        self.aboutApp.triggered.connect(self.openAboutApp)
        self.siteVk.triggered.connect(lambda: webbrowser.open('https://vk.com/niktox2'))
        self.siteGithub.triggered.connect(lambda: webbrowser.open('https://github.com/NiktoX2/note-pythone'))

    def new(self):
        window = Window(self)
        window.resize(600, 300)
        window.show()

    @pyqtSlot()
    def open(self):
        if self.langVariables == 0:
            falname = PyQt5.QtWidgets.QFileDialog.getOpenFileName(self, "Открыть", '', openFileSelectionRu)[0]
            try:
                fa = open(falname, 'r', encoding='utf-8')
                with fa:
                    data = fa.read()
                    self.text_edit.setText(data)
                fa.close()
            except FileNotFoundError:
                print("FileNotFoundError")
        else:
            falname = PyQt5.QtWidgets.QFileDialog.getOpenFileName(self, "Open", '', openFileSelectionEng)[0]
            try:
                fa = open(falname, 'r', encoding='utf-8')
                with fa:
                    data = fa.read()
                    self.text_edit.setText(data)
                fa.close()
            except FileNotFoundError:
                print("FileNotFoundError")

    @pyqtSlot()
    def save(self):
        if self.langVariables == 0:
            falname = PyQt5.QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить", '', saveFileSelectionRu)[0]
            try:
                fa = open(falname, 'w', encoding='utf-8')
                text = self.text_edit.toPlainText()
                fa.write(text)
                fa.close()
            except FileNotFoundError:
                print("FileNotFoundError")
        else:
            falname = PyQt5.QtWidgets.QFileDialog.getSaveFileName(self, "Save", '', saveFileSelectionEng)[0]
            try:
                fa = open(falname, 'w', encoding='utf-8')
                text = self.text_edit.toPlainText()
                fa.write(text)
                fa.close()
            except FileNotFoundError:
                print("FileNotFoundError")

    @pyqtSlot()
    def fontText(self):
        self.f, ok = PyQt5.QtWidgets.QFontDialog.getFont(QFont(self.f), self)
        if ok:
            self.styleFont.setFont(self.f)

    def setLangRu(self):
        if self.langVariables == 1:
            self.setWindowTitle("Блокнот")
            self.file.setTitle("Файл")
            self.newAction.setText("Новый файл")
            self.openAction.setText("Открыть")
            self.saveAction.setText("Сохранить")
            self.setting.setTitle("Настройки")
            self.fontAction.setText("Шрифт")
            self.lang.setTitle("Язык")
            self.about.setTitle("Помощь")
            self.aboutApp.setText("Об приложении")
            self.siteVk.setText("Vk Автора")
            self.siteGithub.setText("Исходный код (Github)")
            self.langVariables = 0

    def setLangEng(self):
        if self.langVariables == 0:
            self.setWindowTitle("Note")
            self.file.setTitle("File")
            self.newAction.setText("New")
            self.openAction.setText("Open")
            self.saveAction.setText("Save")
            self.setting.setTitle("Setting")
            self.fontAction.setText("Font")
            self.lang.setTitle("Lang")
            self.about.setTitle("Help")
            self.aboutApp.setText("About the app")
            self.siteVk.setText("Vk About")
            self.siteGithub.setText("Source (Github)")
            self.langVariables = 1

    def openAboutApp(self):
        if self.langVariables == 0:
            self.msgBoxAboutApp.setText(textAboutAppRu)
            self.msgBoxAboutApp.setWindowTitle("Об приложении")
            self.msgBoxAboutApp.exec()
        else:
            self.msgBoxAboutApp.setText(textAboutAppEng)
            self.msgBoxAboutApp.setWindowTitle("About the app")
            self.msgBoxAboutApp.exec()

    def appStile(self):
        self.setStyleSheet("""
        /* текстовый редактор */
        QTextEdit {background-color: #000; color: #fff; border-style: #000}
        /* фон скрола */
        QScrollBar {width: 8px; background-color: #000}
        /* фон скрола чтоб точно установился*/
        QScrollBar::add-page, QScrollBar::sub-page{background: none}
        /* сам скрол */
        QScrollBar::handle {background-color: #fff; border-radius: 4px}
        /* кнопки чтоб видно не было, но они все равно работают :( */
        QScrollBar::add-line, QScrollBar::sub-line {border: none;background: none}
        /* меню в целом */
        QMenuBar {background-color: #000;color: #fff;}
        /* кнопки */
        QMenuBar::item {background-color: #000;color: rgb(255,255,255)}
        /* цвет кнопок при наведении */
        QMenuBar::item::selected {background-color: #262626}
        /* цвет всплывающего меню */
        QMenu {background-color: #000;color: rgb(255,255,255)}
        /* в меню кнопки при наведении */
        QMenu::item::selected {background-color: #262626}
        QFontDialog {}
        """)


def appStart():
    app = PyQt5.QtWidgets.QApplication([])
    main = Window()
    main.show()
    app.exec_()


if __name__ == "__main__":
    appStart()

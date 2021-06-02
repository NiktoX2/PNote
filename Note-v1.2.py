from PyQt5.QtCore import pyqtSlot, QTimer
import PyQt5.QtWidgets
from PyQt5.QtGui import QFont
import webbrowser

appNameRu = "Блокнот"
appNameEng = "Note"
textAboutAppRu = "<center>" \
                 "<h3>Блокнот</h3>" \
                 "Автор: NiktoX2 (НиктоХ2)<br/>" \
                 "Версия 1.2" \
                 "<center><h3>Изменено:<h3></center>" \
                 "Минимальный размер окна<br/>" \
                 "Прочие незначительные изменение в коде" \
                 "</center>"
textAboutAppEng = "<center>" \
                  "<h3>Note</h3>" \
                  "Author: NiktoX2 (НиктоХ2)<br/>" \
                  "Version 1.2" \
                  "<center><h3>Changed:<h3></center>" \
                  "Minimum window size<br/>" \
                  "Other minor code changes" \
                  "</center>"
openFileSelectionRu = 'Все файлы (*.*);;Текстовый файл (*.txt);;Python файлы (*.py)'
openFileSelectionEng = 'All files (*.*);;Text file (*.txt);;Python файлы (*.py)'
saveFileSelectionRu = 'Текстовый файл (*.txt);;Python файлы (*.py);;lost (*.niktox2)'
saveFileSelectionEng = 'Text file (*.txt);;Python files (*.py);;lost (*.niktox2)'
setStyleBlack = """
        /* текстовый редактор */
        QTextEdit {background-color: #000; color: #fff; border-style: #000}
        /* фон скрола */
        QScrollBar {width: 8px; background-color: #000}
        /* фон скрола чтоб точно установился*/
        QScrollBar::add-page, QScrollBar::sub-page{background: none}
        /* сам скрол */
        QScrollBar::handle {background-color: #fff; border-radius: 4px}
        /* кнопки чтоб видно не было, но они все равно работают :( */
        QScrollBar::add-line, QScrollBar::sub-line {border: none; background: none}
        /* меню в целом */
        QMenuBar {background-color: #000; color: #fff;}
        /* кнопки */
        QMenuBar::item {background-color: #000; color: rgb(255,255,255)}
        /* цвет кнопок при наведении */
        QMenuBar::item::selected {background-color: #262626}
        /* цвет всплывающего меню */
        QMenu {background-color: #000; color: rgb(255,255,255)}
        /* в меню кнопки при наведении */
        QMenu::item::selected {background-color: #262626}
        """
setStyleWrite = """
        /* текстовый редактор */
        QTextEdit {background-color: #fff; color: #000; border-style: #fff}
        /* фон скрола */
        QScrollBar {width: 8px; background-color: #fff}
        /* фон скрола чтоб точно установился*/
        QScrollBar::add-page, QScrollBar::sub-page{background: none}
        /* сам скрол */
        QScrollBar::handle {background-color: #000; border-radius: 4px}
        /* кнопки чтоб видно не было, но они все равно работают :( */
        QScrollBar::add-line, QScrollBar::sub-line {border: none;background: none}
        /* меню в целом */
        QMenuBar {background-color: #fff; color: #000;}
        /* кнопки */
        QMenuBar::item {background-color: #fff; color: #000}
        /* цвет кнопок при наведении */
        QMenuBar::item::selected {background-color: #858585}
        /* цвет всплывающего меню */
        QMenu {background-color: #fff; color: #000}
        /* в меню кнопки при наведении */
        QMenu::item::selected {background-color: #858585}
        """


class Window(PyQt5.QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        PyQt5.QtWidgets.QMainWindow.__init__(self, parent)
        self.resize(700, 400)
        # QPlainTextEdit ? | QTextEdit
        self.textEdit = PyQt5.QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        # минимальный размер по ширене и высоте
        self.setMinimumWidth(220)
        self.setMinimumHeight(200)
        # по умолчанию размер шрифта
        self.f = self.textEdit.font()
        self.f = QFont("Arial", 16)
        self.textEdit.setFont(self.f)

        # установка стиля для редактора
        self.styleFont = self.textEdit

        # menu
        self.menubar = self.menuBar()
        self.file = self.menubar.addMenu("")
        self.newAction = PyQt5.QtWidgets.QAction("", self)
        self.openAction = PyQt5.QtWidgets.QAction("", self)
        self.saveAction = PyQt5.QtWidgets.QAction("", self)
        self.setting = self.menubar.addMenu("")
        self.fontAction = PyQt5.QtWidgets.QAction("", self)
        self.lang = self.setting.addMenu("")
        self.langRu = PyQt5.QtWidgets.QAction("Ru", self)
        self.langEng = PyQt5.QtWidgets.QAction("Eng", self)
        self.setStyleApp = self.setting.addMenu("")
        self.setBlack = PyQt5.QtWidgets.QAction("", self)
        self.setWrite = PyQt5.QtWidgets.QAction("", self)
        self.about = self.menubar.addMenu("")
        self.aboutApp = PyQt5.QtWidgets.QAction("", self)
        self.siteVk = PyQt5.QtWidgets.QAction("", self)
        self.siteGithub = PyQt5.QtWidgets.QAction("", self)
        self.msgBoxAboutAuthor = PyQt5.QtWidgets.QMessageBox()
        self.msgBoxAboutApp = PyQt5.QtWidgets.QMessageBox()

        # стиль приложения по умалчанию
        # Black = 0 \\\ черный
        # Write = 1 \\\ белый
        self.styleApp = 0
        if self.styleApp == 0:
            self.setStyleSheet(setStyleBlack)
        else:
            self.setStyleSheet(setStyleWrite)

        # variables язык \почти/ по умолчанию
        # rus = 0, "rus"
        # eng = 1, "eng"
        # запуск с выбраным языком
        self.setGlobalLang = 0
        # переключение языка в приложении
        self.langVariables = self.setGlobalLang
        if self.setGlobalLang == 0:
            self.setWindowTitle(appNameRu)
            self.file.setTitle("Файл")
            self.newAction.setText("Новый файл")
            self.openAction.setText("Открыть")
            self.saveAction.setText("Сохранить")
            self.setting.setTitle("Настройки")
            self.fontAction.setText("Шрифт")
            self.lang.setTitle("Язык")
            self.setStyleApp.setTitle("Тема")
            self.setBlack.setText("Черная")
            self.setWrite.setText("Белая")
            self.about.setTitle("Помощь")
            self.aboutApp.setText("Об приложении")
            self.siteVk.setText("Vk Автора")
            self.siteGithub.setText("Исходный код (Github)")
        else:
            self.setWindowTitle(appNameEng)
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

        # инфа о том, сохранен ли файл
        self.fileSeve = None

        # подключить
        self.Menubar()

    def Menubar(self):
        # новый
        self.file.addAction(self.newAction)
        self.newAction.triggered.connect(self.new)
        self.newAction.setShortcut("Ctrl+N")
        # открыть файл
        self.file.addAction(self.openAction)
        self.openAction.triggered.connect(self.open)
        self.openAction.setShortcut("Ctrl+O")
        # сохранить файл
        self.file.addAction(self.saveAction)
        self.saveAction.triggered.connect(self.save)
        self.saveAction.setShortcut("Ctrl+S")
        # # установить шрифт
        self.setting.addAction(self.fontAction)
        self.fontAction.triggered.connect(self.fontText)
        # установить русский язык
        self.lang.addAction(self.langRu)
        self.langRu.triggered.connect(self.setLangRu)
        # установить английский язык
        self.lang.addAction(self.langEng)
        self.langEng.triggered.connect(self.setLangEng)
        # установить черный цвет
        self.setStyleApp.addAction(self.setBlack)
        self.setBlack.triggered.connect(self.setBlackApp)
        # установить белый цвет
        self.setStyleApp.addAction(self.setWrite)
        self.setWrite.triggered.connect(self.setWriteApp)
        # открыть о приложении
        self.about.addAction(self.aboutApp)
        self.aboutApp.triggered.connect(self.openAboutApp)
        # открыть в браузере сайт
        self.about.addAction(self.siteVk)
        self.siteVk.triggered.connect(lambda: webbrowser.open('https://vk.com/niktox2'))
        # открыть в браузере сайт
        self.about.addAction(self.siteGithub)
        self.siteGithub.triggered.connect(lambda: webbrowser.open('https://github.com/NiktoX2/note-pythone'))

    def new(self):
        window = Window(self)
        window.resize(600, 300)
        window.show()

    def setWinTiRu(self):
        self.setWindowTitle(appNameRu)

    def setWinTiEng(self):
        self.setWindowTitle(appNameEng)

    def setBlackApp(self):
        self.setStyleSheet(setStyleBlack)

    def setWriteApp(self):
        self.setStyleSheet(setStyleWrite)

    @pyqtSlot()
    def open(self):
        if self.langVariables == 0:
            falname = PyQt5.QtWidgets.QFileDialog.getOpenFileName(self, "Открыть", '', openFileSelectionRu)[0]
            try:
                fa = open(falname, 'r', encoding='utf-8')
                with fa:
                    data = fa.read()
                    self.textEdit.setText(data)
                fa.close()
            except FileNotFoundError:
                pass
        else:
            falname = PyQt5.QtWidgets.QFileDialog.getOpenFileName(self, "Open", '', openFileSelectionEng)[0]
            try:
                fa = open(falname, 'r', encoding='utf-8')
                with fa:
                    data = fa.read()
                    self.textEdit.setText(data)
                fa.close()
            except FileNotFoundError:
                pass

    @pyqtSlot()
    def save(self):
        if self.langVariables == 0:
            if self.fileSeve is None:
                self.falnameRu = PyQt5.QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить", '', saveFileSelectionRu)[0]
                try:
                    fa = open(self.falnameRu, 'w', encoding='utf-8')
                    text = self.textEdit.toPlainText()
                    fa.write(text)
                    fa.close()
                except FileNotFoundError:
                    pass
                self.fileSeve = 1
            else:
                fa = open(self.falnameRu, 'w', encoding='utf-8')
                text = self.textEdit.toPlainText()
                fa.write(text)
                fa.close()
                self.setWindowTitle("Блокнот - Файл сохранен")
                QTimer.singleShot(3000, self.setWinTiRu)
        else:
            if self.fileSeve is None:
                self.falnameEng = PyQt5.QtWidgets.QFileDialog.getSaveFileName(self, "Save", '', saveFileSelectionEng)[0]
                try:
                    fa = open(self.falnameEng, 'w', encoding='utf-8')
                    text = self.textEdit.toPlainText()
                    fa.write(text)
                    fa.close()
                except FileNotFoundError:
                    pass
                self.fileSeve = 1
            else:
                fa = open(self.falnameEng, 'w', encoding='utf-8')
                text = self.textEdit.toPlainText()
                fa.write(text)
                fa.close()
                self.setWindowTitle("Note - File saved")
                QTimer.singleShot(3000, self.setWinTiEng)

    @pyqtSlot()
    def fontText(self):
        self.f, ok = PyQt5.QtWidgets.QFontDialog.getFont(QFont(self.f), self)
        if ok:
            self.styleFont.setFont(self.f)

    def setLangRu(self):
        if self.langVariables == 1:
            self.setWindowTitle(appNameRu)
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
            self.setWindowTitle(appNameEng)
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


if __name__ == "__main__":
    # import sys
    # app = PyQt5.QtWidgets.QApplication(sys.argv)
    app = PyQt5.QtWidgets.QApplication([])
    main = Window()
    main.show()
    # sys.exit(app.exec_())
    app.exec_()

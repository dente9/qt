from PySide6.QtWidgets import QWidget,QVBoxLayout,QApplication,QPushButton
from Ui_translate import Ui_Form
from translate_api import connect
class MyWindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()
        self.fromlang = 0
        self.tolang = 0

    def bind(self):
        self.pushButton.clicked.connect(self.translate)
        self.radioButton.toggled.connect(lambda:self.setfromlang(0))
        self.radioButton_2.toggled.connect(lambda:self.setfromlang(1))
        self.radioButton_3.toggled.connect(lambda:self.setfromlang(2))
        self.comboBox.currentIndexChanged.connect(lambda:self.settolang(self.comboBox.currentIndex()+1))
        self.comboBox.setCurrentIndex(0)


    def setfromlang(self,lang):
        self.fromlang = lang

    def settolang(self,lang):
        self.tolang = lang


    def translate(self):
        text = self.textEdit.toPlainText()
        result = connect(text,fromLanguage=self.fromlang,toLanguage=self.tolang)

        self.textEdit_2.setText(result[0])
        self.textEdit_3.setText(str(result[1]))


if __name__ == '__main__':
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()

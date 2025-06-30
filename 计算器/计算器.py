from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QWidget
import sys

from Ui_cal import Ui_Form as Ui_cal
from Ui_login import Ui_Form as Ui_login

class MyWindow(QWidget,Ui_cal,):
    def __init__(self):
        super().__init__()

       # self.login = Ui_Form()
        self.setupUi(self)
        self.bing()
        self.result=""

    def bing(self):
        self.pushButton_0.clicked.connect(lambda : self.addnumber("0"))
        self.pushButton_1.clicked.connect(lambda : self.addnumber("1"))
        self.pushButton_2.clicked.connect(lambda : self.addnumber("2"))
        self.pushButton_3.clicked.connect(lambda : self.addnumber("3"))
        self.pushButton_4.clicked.connect(lambda : self.addnumber("4"))
        self.pushButton_5.clicked.connect(lambda : self.addnumber("5"))
        self.pushButton_6.clicked.connect(lambda : self.addnumber("6"))
        self.pushButton_7.clicked.connect(lambda : self.addnumber("7"))
        self.pushButton_8.clicked.connect(lambda : self.addnumber("8"))
        self.pushButton_9.clicked.connect(lambda : self.addnumber("9"))
        self.pushButton_add.clicked.connect(lambda : self.addnumber("+"))
        self.pushButton_sub.clicked.connect(lambda : self.addnumber("-"))
        self.pushButton_mul.clicked.connect(lambda : self.addnumber("*"))
        self.pushButton_div.clicked.connect(lambda : self.addnumber("/"))
        self.pushButton_dot.clicked.connect(lambda : self.addnumber("."))
        self.pushButton_enter.clicked.connect(self.equal)
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_back.clicked.connect(self.back)


    def addnumber(self,number):
        self.lineEdit.clear()
        self.result+= number
        self.lineEdit.setText(self.result)

    def equal(self):
        self.lineEdit.clear()
        self.lineEdit.setText(str(eval(self.result)))
        self.result = ""

    def clear(self):
        self.lineEdit.clear()
        self.result = ""

    def back(self):
        self.result = self.result[:-1]
        self.lineEdit.setText(self.result)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

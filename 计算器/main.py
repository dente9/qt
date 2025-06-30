from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QWidget
import sys

from Ui_cal import Ui_Form as Ui_cal
from Ui_login import Ui_Form as Ui_login

class MyWindow(QWidget,Ui_login,Ui_cal,):
    def __init__(self):
        super().__init__()

       # self.login = Ui_Form()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.loginfnc)

    def loginfnc(self):
            account = self.lineEdit.text()
            password = self.lineEdit_2.text()

            if account == "admin" and password == "admin":
                self.pushButton.setText("登录成功")
            else:
                self.pushButton.setText("登录失败")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget,QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtCore import Signal

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("设置页面")


        self.lbusername = QLabel("用户名")
        self.lineeditusername = QLabel()
        self.lbpassword = QLabel("密码")
        self.lineeditpassword = QLabel()

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.lbusername)
        self.mainlayout.addWidget(self.lineeditusername)
        self.mainlayout.addWidget(self.lbpassword)
        self.mainlayout.addWidget(self.lineeditpassword)

        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        self.subwindow = SubWindow(self)
        self.subwindow.show()
    def show_value(self,value):
        self.lineeditusername.setText(value[0])
        self.lineeditpassword.setText(value[1])

class SubWindow(QWidget):
    send_value_to_mainwindow = Signal(list)
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("input")

        self.lineaccount = QLineEdit()
        self.linepassword = QLineEdit()
        self.btnsend = QPushButton("发送")

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.lineaccount)
        self.mainlayout.addWidget(self.linepassword)
        self.mainlayout.addWidget(self.btnsend)
        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        self.send_value_to_mainwindow.connect(self.parent.show_value)

        self.btnsend.clicked.connect(self.send_value)
    def send_value(self):
        value = [self.lineaccount.text(),self.linepassword.text()]
        self.send_value_to_mainwindow.emit(value)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

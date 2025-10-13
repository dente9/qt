import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget,QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtCore import Signal

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("设置页面")

        self.lbusername = QLabel("用户名")
        self.lbpassword = QLabel("密码")
        self.pbsetvalue = QPushButton("设置值")

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.lbusername)
        self.mainlayout.addWidget(self.lbpassword)
        self.mainlayout.addWidget(self.pbsetvalue)
        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        self.subwindow = SubWindow(self)
        self.pbsetvalue.clicked.connect(self.set_valur_subwindow)
        self.subwindow.show()
    def set_valur_subwindow(self):
        self.subwindow.lbvalue.setText("this is a value from subwindow")


class SubWindow(QWidget):
    send_value_to_mainwindow = Signal(list)
    def __init__(self,parent):
        super().__init__()
        self.move(50,50)
        self.parent = parent
        self.setWindowTitle("input")

        self.lineaccount = QLineEdit()
        self.linepassword = QLineEdit()
        self.btnsend = QPushButton("发送")
        self.lbvalue = QLabel("value")

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.lineaccount)
        self.mainlayout.addWidget(self.linepassword)
        self.mainlayout.addWidget(self.btnsend)
        self.mainlayout.addWidget(self.lbvalue)

        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        self.btnsend.clicked.connect(self.setvalue_to_main)
    def setvalue_to_main(self):
        self.parent.lbusername.setText(self.lineaccount.text())
        self.parent.lbpassword.setText(self.linepassword.text())





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

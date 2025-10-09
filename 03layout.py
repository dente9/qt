import sys
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QFormLayout,QLabel,QPushButton,QLineEdit,QLabel
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
# 水平布局
        # self.userlayout = QHBoxLayout()
        # self.userlayout.addWidget(QLabel("用户名"))
        # self.userlayout.addWidget(QLineEdit())
        # self.layout.addLayout(self.userlayout)

        # self.passwordlayout = QHBoxLayout()
        # self.passwordlayout.addWidget(QLabel("密码"))
        # self.passwordlayout.addWidget(QLineEdit())
        # self.layout.addLayout(self.passwordlayout)

        # self.layout.addWidget(QPushButton("登录"))
# 表单布局
        # self.fromlayout = QFormLayout()
        # self.fromlayout.addRow(QLabel("用户名"),QLineEdit())
        # self.fromlayout.addRow(QLabel("密码"),QLineEdit())
        # self.fromlayout.addRow(QPushButton("登录"))
        # self.layout.addLayout(self.fromlayout)

#格子布局
        self.gridlayout = QGridLayout()
        self.gridlayout.addWidget(QLabel("用户名"),0,0)
        self.gridlayout.addWidget(QLineEdit(),0,1)
        self.gridlayout.addWidget(QLabel("密码"),1,0)
        self.gridlayout.addWidget(QLineEdit(),1,1)
        self.gridlayout.addWidget(QPushButton("登录"),2,0,1,2)
        self.layout.addLayout(self.gridlayout)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

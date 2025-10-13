import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget,QHBoxLayout
from PySide6.QtCore import Qt,Signal

class MyWindow(QWidget):
    send_value_to_subwindow = Signal(str)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("main window")

        self.lineeditshow = QLineEdit()
        self.pb_main_to_sub = QPushButton("发送")
        self.label_main_show = QLabel("show the value for subwindow")

        self.window_layout = QHBoxLayout()
        self.btnclose = QPushButton("关闭子窗口")
        self.btnopen = QPushButton("打开子窗口")
        self.btnhide = QPushButton("隐藏子窗口")
        self.window_layout.addWidget(self.btnopen)
        self.window_layout.addWidget(self.btnhide)
        self.window_layout.addWidget(self.btnclose)

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.lineeditshow)
        self.mainlayout.addWidget(self.pb_main_to_sub)
        self.mainlayout.addWidget(self.label_main_show)
        self.mainlayout.addLayout(self.window_layout)

        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        self.subwindow = Subwondow(self)
        #自定义信号绑定
        self.send_value_to_subwindow.connect(self.subwindow.lineedit.setText)
        self.pb_main_to_sub.clicked.connect(self.send_value)
        self.btnopen.clicked.connect(lambda:self.subwindow.show())
        self.btnhide.clicked.connect(lambda:self.subwindow.hide())
        self.btnclose.clicked.connect(lambda:self.subwindow.close())

        self.subwindow.show()

    def send_value(self):
        self.send_value_to_subwindow.emit(self.lineeditshow.text())

class Subwondow(QWidget):
    send_value_to_mainwindow = Signal(str)
    def __init__(self,parent=None):
        super().__init__()
        self.parent = parent
        self.move(50,50)
        self.label = QLabel("子窗口")
        self.lineedit = QLineEdit()
        self.btnsend = QPushButton("发送")

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.label)
        self.mainlayout.addWidget(self.lineedit)
        self.mainlayout.addWidget(self.btnsend)

        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        self.send_value_to_mainwindow.connect(self.parent.label_main_show.setText)
        self.btnsend.clicked.connect(self.send_value)
    def send_value(self):
        self.send_value_to_mainwindow.emit(self.lineedit.text())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

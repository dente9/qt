import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.lb = QLabel("main window")
        self.subwindow =Subwindow()

        self.btnclose = QPushButton("关闭子窗口")
        self.btnopen = QPushButton("打开子窗口")
        self.btnhide = QPushButton("隐藏子窗口")

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.lb)
        self.mainlayout.addWidget(self.btnopen)
        self.mainlayout.addWidget(self.btnhide)
        self.mainlayout.addWidget(self.btnclose)

        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        self.btnopen.clicked.connect(lambda:self.subwindow.show())
        self.btnhide.clicked.connect(lambda:self.subwindow.hide())
        self.btnclose.clicked.connect(lambda:self.subwindow.close())

class Subwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.lb=QLabel("子窗口")
        self.lineedit = QLineEdit()
        self.lineedit.setText("子窗口的文本框")

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.lb)
        self.mainlayout.addWidget(self.lineedit)

        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        pass




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

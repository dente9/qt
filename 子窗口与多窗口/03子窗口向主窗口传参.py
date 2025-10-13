import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget
from PySide6.QtCore import Qt,Signal

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.lineeditshow = QLineEdit()

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.lineeditshow)

        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        self.subwindow = Subwondow(self)
        self.subwindow.show()

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
        self.send_value_to_mainwindow.connect(self.parent.lineeditshow.setText)
        self.btnsend.clicked.connect(self.send_value)
    def send_value(self):
        self.send_value_to_mainwindow.emit(self.lineedit.text())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

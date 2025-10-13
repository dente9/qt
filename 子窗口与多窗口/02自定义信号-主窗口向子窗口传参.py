import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget
from PySide6.QtCore import Qt,Signal

class MyWindow(QWidget):
    send_value_to_subwindow = Signal(str)
    def __init__(self):
        super().__init__()
        self.lineeditsend = QLineEdit()
        self.btn_send = QPushButton("发送")

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.lineeditsend)
        self.mainlayout.addWidget(self.btn_send)

        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        self.subwindow = Subwindow()
        self.send_value_to_subwindow.connect(self.subwindow.lineedit.setText)
        self.btn_send.clicked.connect(self.send_value)
        self.subwindow.show()

    def send_value(self):
        self.send_value_to_subwindow.emit(self.lineeditsend.text())

class Subwindow(QWidget):
    def __init__(self):
        super().__init__()
        #接受信号
        self.lineedit = QLineEdit()


        self.mainlayout = QVBoxLayout()
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

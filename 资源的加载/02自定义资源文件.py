import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import hello_rc
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.lb = QLabel()
        self.lb.setPixmap(QPixmap(":/image/image.png"))

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.lb)

        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        pass




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

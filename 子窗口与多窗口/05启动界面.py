import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget
from PySide6.QtCore import Qt,QTimer
from PySide6.QtGui import QFont

class loadingwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.lbwait = QLabel("正在加载...")
        self.lbwait.setFont(QFont("微软雅黑",50))
        self.lbwait.setAlignment(Qt.AlignCenter)

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.lbwait)

        self.setLayout(self.mainlayout)
        self.bind()
        QTimer.singleShot(3000,self.openmainwindow)

    def bind(self):
        pass

    def openmainwindow(self):
        self.mainwindow = mainwindow()
        self.mainwindow.show()
        self.close()

class mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.lbwelcome = QLabel("welcome to my program")
        self.lbwelcome.setFont(QFont("微软雅黑",50))
        self.lbwelcome.setAlignment(Qt.AlignCenter)

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.lbwelcome)

        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        pass




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = loadingwindow()
    window.show()
    sys.exit(app.exec())

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget,QStyle
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.lb = QLabel()
        self.lb.setPixmap(self.style().standardPixmap(QStyle.StandardPixmap.SP_DialogSaveButton))

        self.lb1 = QLabel()
        self.lb1.setPixmap(self.style().standardPixmap(QStyle.StandardPixmap.SP_DialogOpenButton))

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.lb)
        self.mainlayout.addWidget(self.lb1)

        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        pass




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QWidget,QVBoxLayout, QHBoxLayout,QPushButton,QLabel,QLineEdit,QComboBox
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.mainlayout = QVBoxLayout()
        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        pass




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

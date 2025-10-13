import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget
from PySide6.QtCore import Qt
from Ui_menus import Ui_MainWindow

class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()




    def bind(self):
        self.actionopen.triggered.connect(lambda: print("打开"))
        self.actionexit.triggered.connect(self.close)
        self.actionadd_something.triggered.connect(lambda: print("添加"))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

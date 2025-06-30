import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        cb=QComboBox()
        cb.addItems(["1","2","fsd"])
        cb.currentTextChanged.connect(self.showname)
        #cb.currentIndexChanged.connect(self.showname)

        mainlayout = QVBoxLayout()
        mainlayout.addWidget(cb)
        self.setLayout(mainlayout)

    def showname(self,name):
        print(name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

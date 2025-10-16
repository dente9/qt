import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QWidget,QVBoxLayout, QHBoxLayout,QPushButton,QLabel,QLineEdit,QComboBox,QListWidget,QListWidgetItem
from PySide6.QtCore import Qt
from faker import Faker

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.fake = Faker(locale='zh_CN')
        self.listwidget = QListWidget()
        self.listwidget.addItem(QListWidgetItem("first"))
        self.listwidget.addItems([self.fake.name() for i in range(20)])
        self.listwidget.insertItem(3, QListWidgetItem("aaaaaaaaaaa"))
        self.listwidget.insertItems(4, [str(i) for i in range(3)])

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.listwidget)
        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        pass




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

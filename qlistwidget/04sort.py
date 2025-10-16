import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QWidget,QVBoxLayout, QHBoxLayout,QPushButton,QLabel,QLineEdit,QComboBox,QListWidget,QListWidgetItem
from PySide6.QtCore import Qt
from faker import Faker
import random
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.listwidget = QListWidget()
        self.listwidget.insertItems(0,[str(random.randint(0,100)) for i in range(10)])
        self.lbsort = QPushButton("排序")


        self.lbclear = QPushButton("清空")


        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.listwidget)
        self.mainlayout.addWidget(self.lbsort)
        self.mainlayout.addWidget(self.lbclear)
        self.setLayout(self.mainlayout)
        self.bind()



    def bind(self):
        self.lbclear.clicked.connect(self.listwidget.clear)
        self.lbsort.clicked.connect(lambda: self.listwidget.sortItems(Qt.SortOrder.AscendingOrder))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

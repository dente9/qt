import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QWidget,QVBoxLayout, QHBoxLayout,QPushButton,QLabel,QLineEdit,QComboBox,QTableWidget,QTableWidgetItem
from PySide6.QtCore import Qt
from faker import Faker

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800,600)
        self.fake = Faker(locale='zh_CN')
        self.data = [[self.fake.name(),self.fake.address(),self.fake.ascii_free_email()] for _ in range(80)]
        self.table = QTableWidget()
        self.table.setRowCount(len(self.data))
        self.table.setColumnCount(3)
        self.table.setItem(0,0,QTableWidgetItem("姓名"))
        for row_index,item in enumerate(self.data):
            for col_index,value in enumerate(item):
                self.table.setItem(row_index,col_index,QTableWidgetItem(value))

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.table)
        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        pass




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

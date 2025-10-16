import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QWidget,QVBoxLayout, QHBoxLayout,QPushButton,QLabel,QLineEdit,QComboBox,QListWidget,QListWidgetItem
from PySide6.QtCore import Qt
from faker import Faker

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.fake = Faker(locale='zh_CN')
        self.listwidget = QListWidget()
        self.listwidget.addItems([self.fake.name() for i in range(20)])
        #插入
        self.listwidget.insertItems(0,["110","120","130"])
       # self.listwidget.removeItemWidget(self.listwidget.item(0)) #错误方法
       # 删除
        self.listwidget.takeItem(1)
        #修改
        itemget = self.listwidget.item(0)
        itemget.setText("111")
        self.listwidget.item(2).setText("222")
        #查找
        result = self.listwidget.findItems("张",Qt.MatchFlag.MatchContains)
        print([i.text() for i in result ])

        for i in range(self.listwidget.count()):
            print(self.listwidget.item(i).text())

        self.lbclear = QPushButton("清空")


        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.listwidget)
        self.mainlayout.addWidget(self.lbclear)
        self.setLayout(self.mainlayout)
        self.bind()

    def listchanged(self,item,previous):
        print(previous.text())
        print(item.text())

    def bind(self):
        self.lbclear.clicked.connect(self.listwidget.clear)
        self.listwidget.currentItemChanged.connect(self.listchanged)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

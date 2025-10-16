import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QWidget,QVBoxLayout, QHBoxLayout,QPushButton,QLabel,QLineEdit,QComboBox,QListWidget,QListWidgetItem
from PySide6.QtCore import Qt
from faker import Faker
from PySide6.QtGui import QAction

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.fake = Faker(locale='zh_CN')
        self.listwidget = QListWidget()
        self.listwidget.addItems([self.fake.name() for i in range(20)])
        self.lbclear = QPushButton("清空")
        #窗体上下文菜单

        self.sayhello = QAction("hello")
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.addAction(self.sayhello)
        #控件上下文菜单
        self.outputcurrent = QAction("输出当前项")
        self.delcurrent = QAction("删除当前项")
        self.listwidget.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.listwidget.addAction(self.outputcurrent)
        self.listwidget.addAction(self.delcurrent)

        self.listwidget.item(0).setCheckState(Qt.CheckState.Unchecked)



        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.listwidget)
        self.mainlayout.addWidget(self.lbclear)
        self.setLayout(self.mainlayout)
        self.bind()

    def listchanged(self,item,previous):
        # print(previous.text())
        # print(item.text())
        pass

    def outputcurrentltem(self):
        print(self.listwidget.currentItem().text())

    def bind(self):
        self.lbclear.clicked.connect(self.listwidget.clear)

        self.sayhello.triggered.connect(lambda: print("hello"))
        self.outputcurrent.triggered.connect(self.outputcurrentltem)
        self.delcurrent.triggered.connect(lambda:self.listwidget.takeItem(self.listwidget.currentRow()))

        self.listwidget.currentItemChanged.connect(self.listchanged)
        # 选中状态
        self.listwidget.itemChanged.connect(lambda item:print(item.checkState()))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

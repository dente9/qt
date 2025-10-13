import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget,QToolBox,QStyle
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.toolbox = QToolBox()
        self.arrowright = self.style().standardPixmap(QStyle.StandardPixmap.SP_ArrowRight)
        self.arrowdown = self.style().standardPixmap(QStyle.StandardPixmap.SP_ArrowDown)

        #折叠选项卡内容
        self.widget1 = QWidget()
        self.widget1laout = QVBoxLayout()
        self.widget1laout.addWidget(QLabel("item1"))
        self.widget1laout.addWidget(QPushButton("pushbotton 1"))
        self.widget1.setLayout(self.widget1laout)

        self.widget2 = QWidget()
        self.widget2laout = QVBoxLayout()
        self.widget2laout.addWidget(QLabel("item2"))
        self.widget2laout.addWidget(QPushButton("pushbotton 2"))
        self.widget2.setLayout(self.widget2laout)

        self.widget3 = QWidget()
        self.widget3laout = QVBoxLayout()
        self.widget3laout.addWidget(QLabel("item3"))
        self.widget3laout.addWidget(QPushButton("pushbotton 3"))
        self.widget3.setLayout(self.widget3laout)

        self.toolbox.addItem(self.widget1,self.arrowright,"折叠选项卡1")
        self.toolbox.addItem(self.widget2,self.arrowright,"折叠选项卡2")
        self.toolbox.addItem(self.widget3,self.arrowright,"折叠选项卡3")

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.toolbox)

        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        self.toolbox.currentChanged.connect(self.toolbox_currentChanged)

    def toolbox_currentChanged(self,index):
        for i in range(self.toolbox.count()):
            self.toolbox.setItemIcon(i,self.arrowright)
        self.toolbox.setItemIcon(index,self.arrowdown)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

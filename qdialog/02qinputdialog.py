import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget,QInputDialog
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.mainlayout = QVBoxLayout()
        self.btn = QPushButton("get a int number")
        self.btn1 = QPushButton("get a float number")
        self.btn2 = QPushButton("get a item")
        self.btn3 = QPushButton("get a string")
        self.btn4 = QPushButton("get a string list")



        self.mainlayout.addWidget(self.btn)
        self.mainlayout.addWidget(self.btn1)
        self.mainlayout.addWidget(self.btn2)
        self.mainlayout.addWidget(self.btn3)
        self.mainlayout.addWidget(self.btn4)

        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        self.btn.clicked.connect(self.btn_click)
        self.btn1.clicked.connect(self.btn1_click)
        self.btn2.clicked.connect(lambda:print(QInputDialog.getItem(self,"输入对话框","请输入内容",["哇哈哈","可乐","冰红茶"],0,False))) #指针,标题,内容,项目,默认索引,是否可编辑
        self.btn3.clicked.connect(lambda:print(QInputDialog.getText(self,"输入对话框","请输入内容",QLineEdit.EchoMode.Normal,"默认值")))
        self.btn4.clicked.connect(lambda:print(QInputDialog.getMultiLineText(self,"输入对话框","请输入内容","默认值")))

    def btn_click(self):
        reply,ok = QInputDialog.getInt(self,"输入对话框","请输入内容",1,0,100,1)# defeault value,min,max,step
        if ok:
            print(reply)

    def btn1_click(self):
        reply,ok = QInputDialog.getDouble(self,"输入对话框","请输入内容",1.0,0.0,100.0,1)# defeault value,min,max,step
        if ok:
            print(reply)

    def btn2_click(self):
        reply,ok = QInputDialog.getItem(self,"输入对话框","请输入内容",["1","2","3"],0,True)# defeault value





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

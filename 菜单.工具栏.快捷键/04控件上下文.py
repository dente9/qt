import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget,QMenuBar,QMenu,QStyle
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.openfie = QAction("打开文件")
        self.closefile = QAction("关闭文件")
        self.addActions([self.openfie,self.closefile])

        self.lineedit = QLineEdit()
        self.lineedit2 = QLineEdit()
        self.lineedit.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.sendvalur = QAction("发送")
        self.shouwcurrentvalur = QAction("显示当前值")
        self.lineedit.addActions([self.sendvalur,self.shouwcurrentvalur])

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.lineedit)
        self.mainlayout.addWidget(self.lineedit2)

        central = QWidget()
        central.setLayout(self.mainlayout)
        self.setCentralWidget(central)


        self.bind()

    def bind(self):
        self.openfie.triggered.connect(lambda: print("打开文件"))
        self.closefile.triggered.connect(lambda: print("关闭文件"))
        self.sendvalur.triggered.connect(lambda:self.lineedit2.setText(self.lineedit.text()))
        self.shouwcurrentvalur.triggered.connect(lambda: print(self.lineedit.text()))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

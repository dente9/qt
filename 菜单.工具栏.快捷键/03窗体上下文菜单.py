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
        self.addAction(self.openfie)
        self.addAction(self.closefile)
        #self.addActions([self.openfie,self.closefile])

        self.bind()

    def bind(self):
        self.openfie.triggered.connect(lambda: print("打开文件"))
        self.closefile.triggered.connect(lambda: print("关闭文件"))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

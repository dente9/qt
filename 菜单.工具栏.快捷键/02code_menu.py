import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget,QMenuBar,QMenu,QStyle
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menuBar = self.menuBar()
        self.menu = QMenu("文件")
        self.openfile = QAction(self.style().standardIcon(QStyle.SP_DialogOpenButton),"打开文件")
        self.closefile = QAction(self.style().standardIcon(QStyle.SP_DialogCloseButton),"关闭文件")
        self.menu.addAction(self.openfile)
        self.menu.addAction(self.closefile)

        self.moremuenu = QMenu("更多")
        self.morefile = QAction("更多文件")
        self.moremuenu.addAction(self.morefile)
        self.menu.addMenu(self.moremuenu)

        self.menuBar.addMenu(self.menu)

        self.bind()

    def bind(self):
        self.openfile.triggered.connect(lambda: print("打开文件"))
        self.closefile.triggered.connect(lambda: print("关闭文件"))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

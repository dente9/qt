import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget,QMessageBox
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300,200)
        self.mainlayout = QVBoxLayout()

        self.btn= QPushButton("按钮")
        self.mainlayout.addWidget(self.btn)
        self.setLayout(self.mainlayout)

        self.bind()
    def bind(self):
        self.btn.clicked.connect(self.btn_click)

    def btn_click(self):
        #QMessageBox.information(self,"提示","这是一个信息提示框") #窗口指针,标题,内容,按钮组,默认按钮
        reply=QMessageBox.information(self,"提示","这是一个信息提示框",QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Cancel,QMessageBox.StandardButton.Ok)
        if reply==QMessageBox.StandardButton.Ok:
            print("点击了确定")
        else:
            print("点击了取消")
        # QMessageBox.warning(self,"警告","这是一个警告框")
        # QMessageBox.critical(self,"错误","这是一个错误框")
        # QMessageBox.question(self,"提示","这是一个询问框")
        # QMessageBox.about(self,"关于","这是一个关于框")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

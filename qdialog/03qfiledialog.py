import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget,QFileDialog
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.mainlayout = QVBoxLayout()
        self.btn = QPushButton("select a file")
        self.btn1 = QPushButton("select many file")
        self.btn2 = QPushButton("select a folder")
        self.btn3 = QPushButton("select a file and save")


        self.mainlayout.addWidget(self.btn)
        self.mainlayout.addWidget(self.btn1)
        self.mainlayout.addWidget(self.btn2)
        self.mainlayout.addWidget(self.btn3)
        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        self.btn.clicked.connect(lambda: print(QFileDialog.getOpenFileName(self,"选择文件","","All Files (*);;music Files (*.mp3 *.mp4)"))) #指针,标题,路劲,文件类型
        self.btn1.clicked.connect(lambda: print(QFileDialog.getOpenFileNames(self,"选择文件","","All Files (*);;music Files (*.mp3 *.mp4)")))
        self.btn2.clicked.connect(lambda: print(QFileDialog.getExistingDirectory(self,"选择文件夹","")))
        self.btn3.clicked.connect(lambda: print(QFileDialog.getSaveFileName(self,"选择文件并保存","","All Files (*);;music Files (*.mp3 *.mp4)")))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget,QSlider,QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PIL import Image,ImageFilter,ImageQt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.mainlayout = QVBoxLayout()
        self.btn = QPushButton("选择图片")
        self.lbshowimg = QLabel()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,20)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(2)

        self.setLayout(self.mainlayout)
        self.mainlayout.addWidget(self.btn)
        self.mainlayout.addWidget(self.lbshowimg)
        self.mainlayout.addWidget(self.slider)
        self.bind()

    def bind(self):
        self.btn.clicked.connect(lambda:self.openfile())
        self.slider.valueChanged.connect(self.sildervaulechange)

    def sildervaulechange(self,value):
        self.blurimg = self.img.filter(ImageFilter.GaussianBlur(radius=value))
        self.lbshowimg.setPixmap(ImageQt.toqpixmap(self.blurimg))

    def openfile(self):
        file, _ = QFileDialog.getOpenFileName(self, "选择图片", "", "Image Files (*.png *.jpg *.bmp)")
        if file:
            self.img = Image.open(file)
            self.lbshowimg.setPixmap(ImageQt.toqpixmap(self.img))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

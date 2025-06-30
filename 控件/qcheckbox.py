import sys
from PySide6.QtWidgets import QApplication,QVBoxLayout,QWidget,QCheckBox,QPushButton
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        cbox  = QCheckBox("Check me")
        cbox.stateChanged.connect(lambda: self.showname(cbox.text()))

        bth  = QPushButton("getstate")
        bth.clicked.connect(lambda: self.showname(cbox.isChecked()))


        mainlayout = QVBoxLayout()
        mainlayout.addWidget(cbox)
        mainlayout.addWidget(bth)
        self.setLayout(mainlayout)

    def showname(self,name):
        print(name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

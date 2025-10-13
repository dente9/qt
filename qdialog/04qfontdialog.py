import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,QVBoxLayout,QWidget,QFontDialog,QTextEdit
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.edit = QTextEdit()
        self.btn = QPushButton("选择字体")

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.edit)
        self.mainlayout.addWidget(self.btn)

        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        self.btn.clicked.connect(self.changefont)

    def changefont(self):
        ok, font = QFontDialog.getFont()
        if not ok: return
        self.edit.setFont(font)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

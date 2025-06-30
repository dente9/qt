import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QVBoxLayout,QWidget
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainlayout = QVBoxLayout()
        self.bth= QPushButton("Click Me!")
        self.bth.clicked.connect(self.on_button_click)

        mainlayout.addWidget(self.bth)
        self.setLayout(mainlayout)



    def on_button_click(self):
        self.bth.setText("Clicked!")
        print("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit
from PySide6.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Test")
        self.setGeometry(0, 0, 400, 600)

        self.button = QPushButton("Click Me!", self)
        self.button.setGeometry(100, 100, 100, 40)
        self.button.setToolTip("This is a button")

        self.button.clicked.connect(self.on_button_click)

        self.label = QLabel("Hello, World!", self)
        self.label.setGeometry(0, 0, 100, 40)
        self.label.setAlignment(Qt.AlignCenter)

        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(0, 40, 100, 40)
        self.line_edit.setPlaceholderText("Enter text...")

    def on_button_click(self):
        self.button.setText("Clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

from PySide6.QtWidgets import QApplication, QWidget,QVBoxLayout,QTextEdit,QPlainTextEdit,QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        textedit = QTextEdit()
        textedit.setPlainText("这是文本框")
        textedit.append("这是追加的文本")

        btn = QPushButton("add text")
        btn.clicked.connect(lambda:textedit.append("这是追加的文本"))

        layout = QVBoxLayout()
        layout.addWidget(textedit)
        layout.addWidget(btn)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()

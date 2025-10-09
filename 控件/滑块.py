from PySide6.QtWidgets import QApplication,QWidget,QSlider,QVBoxLayout
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("滑块")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.slider = QSlider(Qt.Orientation.Horizontal)

        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.slider_value_changed)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)

        layout.addWidget(self.slider)
        self.setLayout(layout)

    def slider_value_changed(self,value):
        print(value)

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
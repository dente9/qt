import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QComboBox,
                               QVBoxLayout,QWidget,QCheckBox,QRadioButton,QButtonGroup,
                               QTextEdit,QPlainTextEdit,QSlider)
from PySide6.QtCore import Qt
from qt_material import apply_stylesheet

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.mainlayout = QVBoxLayout()

        self.label1 = QLabel("标签1")

        self.btn1 = QPushButton("按钮1")

        self.lineedit1 = QLineEdit()
        self.lineedit1.setPlaceholderText("请输入内容")
        self.lineedit1.setEchoMode(QLineEdit.Password)

        self.cb1 = QComboBox()
        self.cb1.setPlaceholderText("请选择内容")
        self.cb1.addItems(["选项1","选项2","选项3"])
        self.cb1.removeItem(0)

        self.checkbox1 = QCheckBox("复选框1")
        self.checkbox1.setCheckable(False)

        self.checkbox2 = QCheckBox("复选框2")
        self.checkbox2.setChecked(True)

        self.gendernan = QRadioButton("男")
        self.gendernv = QRadioButton("女")

        self.favourite = QButtonGroup()
        self.rbmath = QRadioButton("数学")
        self.rbchinese = QRadioButton("语文")
        self.favourite.addButton(self.rbmath)
        self.favourite.addButton(self.rbchinese)

        self.richtext = QTextEdit()
        self.richtext.setPlaceholderText("请输入内容")
        self.richtext.setMarkdown("# 标题\n## 标题2\n### 标题3")

        self.plaintext = QPlainTextEdit()

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,200)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)



        #统一添加布局
        self.add_widget_to_layout(self.label1,self.btn1,self.lineedit1,self.cb1,
                                 self.checkbox1,self.checkbox2,self.gendernan,self.gendernv,
                                 self.rbmath,self.rbchinese,self.richtext,self.plaintext,self.slider)
        # self.mainlayout.addWidget(self.label1)
        # self.mainlayout.addWidget(self.btn1)
        # self.mainlayout.addWidget(self.lineedit1)
        # self.mainlayout.addWidget(self.cb1)
        # self.mainlayout.addWidget(self.checkbox1)
        # self.mainlayout.addWidget(self.checkbox2)
        # self.mainlayout.addWidget(self.gendernan)
        # self.mainlayout.addWidget(self.gendernv)
        # self.mainlayout.addWidget(self.rbmath)
        # self.mainlayout.addWidget(self.rbchinese)
        # self.mainlayout.addWidget(self.richtext)
        # self.mainlayout.addWidget(self.plaintext)
        # self.mainlayout.addWidget(self.slider)
        self.setLayout(self.mainlayout)
        self.bind()

    def bind(self):
        self.btn1.clicked.connect(self.btn1_click)
        self.lineedit1.textChanged.connect(self.lineedit1_changed)
        self.lineedit1.returnPressed.connect(self.lineedit1_returnPressed)
        self.cb1.currentTextChanged.connect(self.cb1_changed)
        self.checkbox1.stateChanged.connect(self.checkbox1_changed)
        self.checkbox2.stateChanged.connect(self.checkbox2_changed)
        self.gendernan.clicked.connect(lambda:print("点击了男"))
        self.gendernv.clicked.connect(lambda:print("点击了女"))
        self.favourite.buttonClicked.connect(self.whick_is_clicked)
        self.richtext.textChanged.connect(lambda:print("richtext changed"))
        self.slider.valueChanged.connect(lambda:print(self.slider.value()))

    def add_widget_to_layout(self,*widgets):
        for widget in widgets:
            self.mainlayout.addWidget(widget)

    def whick_is_clicked(self,button):
        print(f"点击了{button.text()}")
        print(f"点击了{self.favourite.checkedButton().text()}")

    def cb1_changed(self,text):
        print(text)

    def checkbox1_changed(self,state):
        print(f"check changed{state}")

    def checkbox2_changed(self):
        print(f"check state like :{self.checkbox2.isChecked()}")



    def btn1_click(self):
        print("点击了按钮1")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setText("标签1 has been changed")

    def lineedit1_changed(self,text):
        print(text)

    def lineedit1_returnPressed(self):
        print("按下了回车键")
        print(f"这个里面的内容是{self.lineedit1.text()}")
        self.lineedit1.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app,theme='dark_teal.xml')
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

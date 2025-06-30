import sys
from PySide6.QtWidgets import QApplication, QWidget

from Ui_trains import Ui_Form

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 单位定义
        self.length = {"千米": 100 * 100, "米": 100, "厘米": 1, "分米": 10}
        self.weight = {"斤": 500, "克": 1, "千克": 1000}
        self.type = {"长度": self.length, "重量": self.weight}

        # 绑定事件
        self.bind()

    def bind(self):
        self.data_type_comboBox.addItems(self.type.keys())
        self.comboBox_one.addItems(self.length.keys())
        self.comboBox_twe.addItems(self.length.keys())
        self.data_type_comboBox.currentTextChanged.connect(self.typechange)

        # 设置默认选择项
        self.comboBox_one.setCurrentIndex(0)
        self.comboBox_twe.setCurrentIndex(1)

        # 连接输入框的文本变化信号到槽函数
        self.one_lineEdit.textChanged.connect(lambda: self.update_other_lineedit(self.one_lineEdit))
        self.twe_lineEdit.textChanged.connect(lambda: self.update_other_lineedit(self.twe_lineEdit))

        self.comboBox_one.currentTextChanged.connect(lambda: self.update_other_lineedit(self.one_lineEdit))
        self.comboBox_twe.currentTextChanged.connect(lambda: self.update_other_lineedit(self.twe_lineEdit))

    def format_float(self, num):
        """将浮点数格式化为字符串，去除多余的零"""
        if num.is_integer():
            return str(int(num))
        return f"{num:.10f}".rstrip('0').rstrip('.')

    def calc(self, source_line_edit):
        # 获取大类型
        bigtype = self.data_type_comboBox.currentText()
        current_type = self.comboBox_one.currentText()
        trains_type = self.comboBox_twe.currentText()

        if source_line_edit == self.one_lineEdit:
            input_value = self.one_lineEdit.text()
            if not input_value:
                return None
            try:
                standardization = float(input_value) * self.type[bigtype][current_type]
                result = standardization / self.type[bigtype][trains_type]
                return result
            except (ValueError, ZeroDivisionError):
                return None
        else:
            input_value = self.twe_lineEdit.text()
            if not input_value:
                return None
            try:
                standardization = float(input_value) * self.type[bigtype][trains_type]
                result = standardization / self.type[bigtype][current_type]
                return result
            except (ValueError, ZeroDivisionError):
                return None

    def update_other_lineedit(self, source_line_edit):
        result = self.calc(source_line_edit)
        if result is not None:
            formatted_result = self.format_float(result)

            if source_line_edit == self.one_lineEdit:
                self.twe_lineEdit.blockSignals(True)
                self.twe_lineEdit.setText(formatted_result)
                self.twe_lineEdit.blockSignals(False)

                self.oring_data_label.setText(f"{self.one_lineEdit.text()}{self.comboBox_one.currentText()}=")
                self.trans_data_label.setText(f"{formatted_result}{self.comboBox_twe.currentText()}")
            else:
                self.one_lineEdit.blockSignals(True)
                self.one_lineEdit.setText(formatted_result)
                self.one_lineEdit.blockSignals(False)

                self.oring_data_label.setText(f"{formatted_result}{self.comboBox_one.currentText()}=")
                self.trans_data_label.setText(f"{self.twe_lineEdit.text()}{self.comboBox_twe.currentText()}")

    def typechange(self, text):
        # 在清除前阻塞信号
        self.comboBox_one.blockSignals(True)
        self.comboBox_twe.blockSignals(True)

        self.comboBox_one.clear()
        self.comboBox_twe.clear()

        self.comboBox_one.addItems(self.type[text].keys())
        self.comboBox_twe.addItems(self.type[text].keys())

        # 设置默认选择项
        self.comboBox_one.setCurrentIndex(0)
        self.comboBox_twe.setCurrentIndex(1)

        # 恢复信号
        self.comboBox_one.blockSignals(False)
        self.comboBox_twe.blockSignals(False)

        # 切换类型后立即更新显示
        if self.one_lineEdit.text():
            self.update_other_lineedit(self.one_lineEdit)
        elif self.twe_lineEdit.text():
            self.update_other_lineedit(self.twe_lineEdit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
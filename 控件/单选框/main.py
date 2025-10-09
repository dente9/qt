# -*- coding: utf-8 -*-
# 文件名 demo_radio.py
import os, sys
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
from PySide6.QtWidgets import QApplication, QTextEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt
from PySide6.QtWidgets import QButtonGroup   # 只用它“分组”和“读 id”

class DemoWindow:
    def __init__(self):
        # 1. 加载 QtDesigner 生成的 ui
        ui_file = QFile("demo.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = QUiLoader().load(ui_file)
        ui_file.close()

        # 2. 把 4 个 radio 按钮分别装进两个 ButtonGroup
        #    这样我们就不用自己去记录“谁被选中了”，
        #    直接 buttonGroup.checkedButton() 就能拿到对象。
        self.sex_group   = QButtonGroup(self.ui)   # 性别组
        self.sex_group.addButton(self.ui.rbMale,   0)   # id 0
        self.sex_group.addButton(self.ui.rbFemale, 1)   # id 1

        self.region_group = QButtonGroup(self.ui)  # 地区组
        self.region_group.addButton(self.ui.rbCN, 0)
        self.region_group.addButton(self.ui.rbUS, 1)

        # 3. 任意按钮被点击，都触发同一个刷新函数
        self.sex_group.buttonClicked.connect(self.refresh_output)
        self.region_group.buttonClicked.connect(self.refresh_output)

        # 4. 初始手动刷一次，避免窗口刚弹出来是空的
        self.refresh_output()

        # 5. 显示窗口
        self.ui.show()

    # --------------------------------------------------
    def refresh_output(self):
        """根据当前选中的按钮，拼接字符串并显示"""
        sex_btn   = self.sex_group.checkedButton()
        region_btn = self.region_group.checkedButton()

        sex_text   = sex_btn.text()   if sex_btn   else "未知"
        region_text = region_btn.text() if region_btn else "未知"

        self.ui.textOut.setPlainText(f"性别：{sex_text} | 地区：{region_text}")

# --------------------------------------------------
if __name__ == '__main__':
    app = QApplication([])
    win = DemoWindow()
    app.exec()
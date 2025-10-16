import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                               QHBoxLayout, QVBoxLayout)
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 1. 去掉系统标题栏
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 2. 创建控件
        self.titlelabel = QLabel("标题栏 - 按住我可拖动")
        self.mini_btn   = QPushButton("最小化")
        self.max_btn    = QPushButton("最大化")
        self.close_btn  = QPushButton("关闭")

        # 3. 布局
        title_layout = QHBoxLayout()
        title_layout.addWidget(self.titlelabel, 1)   # 1 表示拉伸
        title_layout.addWidget(self.mini_btn)
        title_layout.addWidget(self.max_btn)
        title_layout.addWidget(self.close_btn)
        title_layout.setContentsMargins(0, 0, 0, 0)

        # 4. 主窗口布局（再套一层，方便以后扩展）
        main_layout = QVBoxLayout(self)
        main_layout.addLayout(title_layout)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # 5. 信号绑定
        self.bind()

        # 6. 拖动所需变量
        self._drag_active = False
        self._drag_start_pos = None

    # 7. 按钮功能
    def bind(self):
        self.mini_btn.clicked.connect(self.showMinimized)
        self.max_btn.clicked.connect(self.showMaximized)
        self.close_btn.clicked.connect(self.close)

    # 8. 鼠标拖动三件套
    def mousePressEvent(self, event):
        # 仅左键 + 在标题栏区域触发
        if (event.button() == Qt.LeftButton and
            self.childAt(event.position().toPoint()) is self.titlelabel):
            self._drag_active = True
            self._drag_start_pos = event.globalPosition().toPoint()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._drag_active:
            delta = event.globalPosition().toPoint() - self._drag_start_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self._drag_start_pos = event.globalPosition().toPoint()
            event.accept()

    def mouseReleaseEvent(self, event):
        if self._drag_active:
            self._drag_active = False
            event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.resize(400, 120)
    w.show()
    sys.exit(app.exec())
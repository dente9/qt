# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trains.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(401, 300)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 401, 301))
        self.gridLayoutWidget.setMinimumSize(QSize(195, 0))
        self.gridLayoutWidget.setMaximumSize(QSize(1000000, 16777215))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox_twe = QComboBox(self.gridLayoutWidget)
        self.comboBox_twe.setObjectName(u"comboBox_twe")
        self.comboBox_twe.setMinimumSize(QSize(195, 0))
        self.comboBox_twe.setMaximumSize(QSize(1000000, 16777215))

        self.gridLayout.addWidget(self.comboBox_twe, 4, 1, 1, 1)

        self.one_lineEdit = QLineEdit(self.gridLayoutWidget)
        self.one_lineEdit.setObjectName(u"one_lineEdit")

        self.gridLayout.addWidget(self.one_lineEdit, 3, 0, 1, 1)

        self.twe_lineEdit = QLineEdit(self.gridLayoutWidget)
        self.twe_lineEdit.setObjectName(u"twe_lineEdit")

        self.gridLayout.addWidget(self.twe_lineEdit, 4, 0, 1, 1)

        self.oring_data_label = QLabel(self.gridLayoutWidget)
        self.oring_data_label.setObjectName(u"oring_data_label")
        self.oring_data_label.setMinimumSize(QSize(0, 0))
        self.oring_data_label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(22)
        self.oring_data_label.setFont(font)
        self.oring_data_label.setStyleSheet(u"color: rgb(120, 120, 120);")

        self.gridLayout.addWidget(self.oring_data_label, 0, 0, 1, 2)

        self.trans_data_label = QLabel(self.gridLayoutWidget)
        self.trans_data_label.setObjectName(u"trans_data_label")
        self.trans_data_label.setMinimumSize(QSize(0, 0))
        self.trans_data_label.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(33)
        self.trans_data_label.setFont(font1)
        self.trans_data_label.setStyleSheet(u"color: rgb(120, 120, 120);")

        self.gridLayout.addWidget(self.trans_data_label, 1, 0, 1, 2)

        self.comboBox_one = QComboBox(self.gridLayoutWidget)
        self.comboBox_one.setObjectName(u"comboBox_one")
        self.comboBox_one.setMinimumSize(QSize(195, 0))
        self.comboBox_one.setMaximumSize(QSize(1000000, 16777215))

        self.gridLayout.addWidget(self.comboBox_one, 3, 1, 1, 1)

        self.data_type_comboBox = QComboBox(self.gridLayoutWidget)
        self.data_type_comboBox.setObjectName(u"data_type_comboBox")

        self.gridLayout.addWidget(self.data_type_comboBox, 2, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5355\u4f4d\u6362\u7b97\u5668", None))
        self.oring_data_label.setText(QCoreApplication.translate("Form", u"0=", None))
        self.trans_data_label.setText(QCoreApplication.translate("Form", u"0", None))
    # retranslateUi


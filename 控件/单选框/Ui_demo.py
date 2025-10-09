# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demo.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QRadioButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(627, 495)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 30, 451, 81))
        self.rbMale = QRadioButton(self.groupBox)
        self.rbMale.setObjectName(u"rbMale")
        self.rbMale.setEnabled(True)
        self.rbMale.setGeometry(QRect(30, 40, 98, 20))
        self.rbMale.setCheckable(True)
        self.rbFemale = QRadioButton(self.groupBox)
        self.rbFemale.setObjectName(u"rbFemale")
        self.rbFemale.setGeometry(QRect(220, 40, 98, 20))
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(40, 160, 451, 81))
        self.rbCN = QRadioButton(self.groupBox_2)
        self.rbCN.setObjectName(u"rbCN")
        self.rbCN.setEnabled(True)
        self.rbCN.setGeometry(QRect(30, 40, 98, 20))
        self.rbCN.setCheckable(True)
        self.rbUS = QRadioButton(self.groupBox_2)
        self.rbUS.setObjectName(u"rbUS")
        self.rbUS.setGeometry(QRect(220, 40, 98, 20))
        self.textOut = QTextEdit(Form)
        self.textOut.setObjectName(u"textOut")
        self.textOut.setGeometry(QRect(40, 270, 431, 64))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.rbMale.setText(QCoreApplication.translate("Form", u"\u7537", None))
        self.rbFemale.setText(QCoreApplication.translate("Form", u"\u5973", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.rbCN.setText(QCoreApplication.translate("Form", u"\u4e2d\u56fd", None))
        self.rbUS.setText(QCoreApplication.translate("Form", u"\u7f8e\u56fd", None))
    # retranslateUi


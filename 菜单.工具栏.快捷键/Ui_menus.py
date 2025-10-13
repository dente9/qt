# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menus.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        self.actionexit = QAction(MainWindow)
        self.actionexit.setObjectName(u"actionexit")
        self.actionadd_something = QAction(MainWindow)
        self.actionadd_something.setObjectName(u"actionadd_something")
        self.actiondelete_all = QAction(MainWindow)
        self.actiondelete_all.setObjectName(u"actiondelete_all")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menufds = QMenu(self.menubar)
        self.menufds.setObjectName(u"menufds")
        self.menumore = QMenu(self.menufds)
        self.menumore.setObjectName(u"menumore")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menufds.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menufds.addAction(self.actionopen)
        self.menufds.addAction(self.actionsave)
        self.menufds.addSeparator()
        self.menufds.addAction(self.actionexit)
        self.menufds.addAction(self.menumore.menuAction())
        self.menumore.addAction(self.actionadd_something)
        self.menu.addAction(self.actiondelete_all)
        self.toolBar.addAction(self.actionopen)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#if QT_CONFIG(shortcut)
        self.actionopen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.actionexit.setText(QCoreApplication.translate("MainWindow", u"exit", None))
#if QT_CONFIG(shortcut)
        self.actionexit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionadd_something.setText(QCoreApplication.translate("MainWindow", u"add something", None))
        self.actiondelete_all.setText(QCoreApplication.translate("MainWindow", u"delete all", None))
        self.menufds.setTitle(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
        self.menumore.setTitle(QCoreApplication.translate("MainWindow", u"more", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi


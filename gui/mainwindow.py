# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import gui.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 186)
        MainWindow.setMinimumSize(QSize(500, 186))
        MainWindow.setMaximumSize(QSize(500, 186))
        icon = QIcon()
        icon.addFile(u":/icons/icons/BlackTraxIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: #383838;\n"
"	color: #fff;\n"
"	selection-background-color: #b78620;\n"
"	selection-color: #000;\n"
"\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"	color: rgb(91, 189, 234);\n"
"\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgba(138, 231, 250, 20%);\n"
"	border: 1px solid #B3F2FF;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"	border: 1px solid #B3F2FF;\n"
"\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.oldWYGLabel = QLabel(self.centralwidget)
        self.oldWYGLabel.setObjectName(u"oldWYGLabel")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.oldWYGLabel.setFont(font)

        self.gridLayout.addWidget(self.oldWYGLabel, 1, 0, 1, 1)

        self.oldWYGFile = QLabel(self.centralwidget)
        self.oldWYGFile.setObjectName(u"oldWYGFile")
        self.oldWYGFile.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.oldWYGFile, 1, 1, 1, 1)

        self.oldWYGBrowseButton = QPushButton(self.centralwidget)
        self.oldWYGBrowseButton.setObjectName(u"oldWYGBrowseButton")
        self.oldWYGBrowseButton.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.oldWYGBrowseButton, 1, 2, 1, 1)

        self.newWYGLabel = QLabel(self.centralwidget)
        self.newWYGLabel.setObjectName(u"newWYGLabel")
        self.newWYGLabel.setFont(font)

        self.gridLayout.addWidget(self.newWYGLabel, 2, 0, 1, 1)

        self.newWYGFile = QLabel(self.centralwidget)
        self.newWYGFile.setObjectName(u"newWYGFile")
        self.newWYGFile.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.newWYGFile, 2, 1, 1, 1)

        self.newWYGBrowseButton = QPushButton(self.centralwidget)
        self.newWYGBrowseButton.setObjectName(u"newWYGBrowseButton")
        self.newWYGBrowseButton.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.newWYGBrowseButton, 2, 2, 1, 1)

        self.btCalLabel = QLabel(self.centralwidget)
        self.btCalLabel.setObjectName(u"btCalLabel")
        self.btCalLabel.setFont(font)

        self.gridLayout.addWidget(self.btCalLabel, 3, 0, 1, 1)

        self.btCalFile = QLabel(self.centralwidget)
        self.btCalFile.setObjectName(u"btCalFile")
        self.btCalFile.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.btCalFile, 3, 1, 1, 1)

        self.btCalBrowseButton = QPushButton(self.centralwidget)
        self.btCalBrowseButton.setObjectName(u"btCalBrowseButton")
        self.btCalBrowseButton.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.btCalBrowseButton, 3, 2, 1, 1)

        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.generateButton, 4, 2, 1, 1)

        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.btIcon = QLabel(self.centralwidget)
        self.btIcon.setObjectName(u"btIcon")
        self.btIcon.setMinimumSize(QSize(32, 32))
        self.btIcon.setMaximumSize(QSize(32, 32))
        self.btIcon.setPixmap(QPixmap(u":/icons/icons/BlackTraxIcon.png"))
        self.btIcon.setScaledContents(True)

        self.headerLayout.addWidget(self.btIcon)

        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.titleLabel.setFont(font1)

        self.headerLayout.addWidget(self.titleLabel)


        self.gridLayout.addLayout(self.headerLayout, 0, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BlackTrax Auto Patcher", None))
        self.oldWYGLabel.setText(QCoreApplication.translate("MainWindow", u"Old WYG CSV Export:", None))
        self.oldWYGFile.setText(QCoreApplication.translate("MainWindow", u"No File Loaded", None))
        self.oldWYGBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.newWYGLabel.setText(QCoreApplication.translate("MainWindow", u"New WYG CSV Export:", None))
        self.newWYGFile.setText(QCoreApplication.translate("MainWindow", u"No File Loaded", None))
        self.newWYGBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.btCalLabel.setText(QCoreApplication.translate("MainWindow", u"Old BlackTrax Calibration:", None))
        self.btCalFile.setText(QCoreApplication.translate("MainWindow", u"No File Loaded", None))
        self.btCalBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Re-Patch", None))
        self.btIcon.setText("")
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"BlackTrax Auto Patcher", None))
    # retranslateUi


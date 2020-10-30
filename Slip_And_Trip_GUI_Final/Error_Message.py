# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Error_MessageGTnFZT.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_Error_Message_Screen(object):
    def setupUi(self, Error_Message_Screen):
        if Error_Message_Screen.objectName():
            Error_Message_Screen.setObjectName(u"Error_Message_Screen")
        Error_Message_Screen.resize(401, 246)
        Error_Message_Screen.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);")
        self.Label = QLabel(Error_Message_Screen)
        self.Label.setObjectName(u"Label")
        self.Label.setGeometry(QRect(40, 20, 321, 41))
        font = QFont()
        font.setFamily(u"MS Reference Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Label.setFont(font)
        self.Label.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt;\n"
"    font-weight: bold;\n"
"}")
        self.Label.setAlignment(Qt.AlignCenter)
        self.Error_Message = QTextBrowser(Error_Message_Screen)
        self.Error_Message.setObjectName(u"Error_Message")
        self.Error_Message.setGeometry(QRect(40, 70, 321, 91))
        font1 = QFont()
        font1.setFamily(u"MS Reference Sans Serif")
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.Error_Message.setFont(font1)
        self.Error_Message.setStyleSheet(u"QTextBrowser {\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 8pt\n"
"}")
        self.Close_Error = QPushButton(Error_Message_Screen)
        self.Close_Error.setObjectName(u"Close_Error")
        self.Close_Error.setGeometry(QRect(40, 170, 321, 71))
        font2 = QFont()
        font2.setFamily(u"MS Reference Sans Serif")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.Close_Error.setFont(font2)
        self.Close_Error.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"    font: 12pt\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.retranslateUi(Error_Message_Screen)

        QMetaObject.connectSlotsByName(Error_Message_Screen)
    # setupUi

    def retranslateUi(self, Error_Message_Screen):
        Error_Message_Screen.setWindowTitle(QCoreApplication.translate("Error_Message_Screen", u"Dialog", None))
        self.Label.setText(QCoreApplication.translate("Error_Message_Screen", u"Error", None))
        self.Close_Error.setText(QCoreApplication.translate("Error_Message_Screen", u"Close", None))
    # retranslateUi


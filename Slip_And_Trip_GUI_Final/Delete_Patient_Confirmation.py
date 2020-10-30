# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Delete_Patient_ConfirmationXNbRXf.ui'
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


class Ui_Delete_Patient_Screen(object):
    def setupUi(self, Delete_Patient_Screen):
        if Delete_Patient_Screen.objectName():
            Delete_Patient_Screen.setObjectName(u"Delete_Patient_Screen")
        Delete_Patient_Screen.resize(401, 160)
        Delete_Patient_Screen.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);")
        self.Yes_Button = QPushButton(Delete_Patient_Screen)
        self.Yes_Button.setObjectName(u"Yes_Button")
        self.Yes_Button.setGeometry(QRect(40, 90, 151, 51))
        font = QFont()
        font.setFamily(u"MS Reference Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Yes_Button.setFont(font)
        self.Yes_Button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"    font: 12pt\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.No_Button = QPushButton(Delete_Patient_Screen)
        self.No_Button.setObjectName(u"No_Button")
        self.No_Button.setGeometry(QRect(210, 90, 151, 51))
        self.No_Button.setFont(font)
        self.No_Button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"    font: 12pt\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Label = QLabel(Delete_Patient_Screen)
        self.Label.setObjectName(u"Label")
        self.Label.setGeometry(QRect(40, 20, 321, 41))
        self.Label.setFont(font)
        self.Label.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.retranslateUi(Delete_Patient_Screen)

        QMetaObject.connectSlotsByName(Delete_Patient_Screen)
    # setupUi

    def retranslateUi(self, Delete_Patient_Screen):
        Delete_Patient_Screen.setWindowTitle(QCoreApplication.translate("Delete_Patient_Screen", u"Dialog", None))
        self.Yes_Button.setText(QCoreApplication.translate("Delete_Patient_Screen", u"Yes", None))
        self.No_Button.setText(QCoreApplication.translate("Delete_Patient_Screen", u"No", None))
        self.Label.setText(QCoreApplication.translate("Delete_Patient_Screen", u"Do you want to remove this patient?", None))
    # retranslateUi


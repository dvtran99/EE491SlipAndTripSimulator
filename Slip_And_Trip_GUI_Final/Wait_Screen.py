# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Wait_ScreenWnybkw.ui'
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
import time


class Ui_Wait_Screen(object):
    def setupUi(self, Wait_Screen):
        if Wait_Screen.objectName():
            Wait_Screen.setObjectName(u"Wait_Screen")
        Wait_Screen.resize(641, 251)
        Wait_Screen.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);")
        self.Label = QLabel(Wait_Screen)
        self.Label.setObjectName(u"Label")
        self.Label.setGeometry(QRect(0, 0, 641, 251))
        font = QFont()
        font.setFamily(u"MS Reference Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Label.setFont(font)
        self.Label.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt;\n"
"    font-weight: bold;\n"
"}")
        self.Label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Wait_Screen)

        QMetaObject.connectSlotsByName(Wait_Screen)
    # setupUi

    def retranslateUi(self, Wait_Screen):
        Wait_Screen.setWindowTitle(QCoreApplication.translate("Wait_Screen", u"Dialog", None))
        self.Label.setText(QCoreApplication.translate("Wait_Screen", u"Running Simulation. Please wait for the Simulation to finish.", None))
    # retranslateUi




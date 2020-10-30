# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add_PatientmtZSny.ui'
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


class Ui_Add_Patient_Screen(object):
    def setupUi(self, Add_Patient_Screen):
        if Add_Patient_Screen.objectName():
            Add_Patient_Screen.setObjectName(u"Add_Patient_Screen")
        Add_Patient_Screen.resize(400, 300)
        Add_Patient_Screen.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);")
        self.formLayoutWidget = QWidget(Add_Patient_Screen)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 391, 201))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.genderLabel = QLabel(self.formLayoutWidget)
        self.genderLabel.setObjectName(u"genderLabel")
        font = QFont()
        font.setFamily(u"MS Reference Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.genderLabel.setFont(font)
        self.genderLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.genderLabel)

        self.heightLabel_2 = QLabel(self.formLayoutWidget)
        self.heightLabel_2.setObjectName(u"heightLabel_2")
        self.heightLabel_2.setFont(font)
        self.heightLabel_2.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.heightLabel_2)

        self.ageLabel_2 = QLabel(self.formLayoutWidget)
        self.ageLabel_2.setObjectName(u"ageLabel_2")
        self.ageLabel_2.setFont(font)
        self.ageLabel_2.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.ageLabel_2)

        self.shoeSizeLabel = QLabel(self.formLayoutWidget)
        self.shoeSizeLabel.setObjectName(u"shoeSizeLabel")
        self.shoeSizeLabel.setFont(font)
        self.shoeSizeLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.shoeSizeLabel)

        self.weightLabel_2 = QLabel(self.formLayoutWidget)
        self.weightLabel_2.setObjectName(u"weightLabel_2")
        self.weightLabel_2.setFont(font)
        self.weightLabel_2.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.weightLabel_2)

        self.weightLabel = QLabel(self.formLayoutWidget)
        self.weightLabel.setObjectName(u"weightLabel")
        self.weightLabel.setFont(font)
        self.weightLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.weightLabel)

        self.genderLineEdit = QLineEdit(self.formLayoutWidget)
        self.genderLineEdit.setObjectName(u"genderLineEdit")
        self.genderLineEdit.setMinimumSize(QSize(0, 19))
        self.genderLineEdit.setFont(font)
        self.genderLineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.genderLineEdit)

        self.genderLineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.genderLineEdit_2.setObjectName(u"genderLineEdit_2")
        self.genderLineEdit_2.setMinimumSize(QSize(0, 19))
        self.genderLineEdit_2.setFont(font)
        self.genderLineEdit_2.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.genderLineEdit_2)

        self.genderLineEdit_3 = QLineEdit(self.formLayoutWidget)
        self.genderLineEdit_3.setObjectName(u"genderLineEdit_3")
        self.genderLineEdit_3.setMinimumSize(QSize(0, 19))
        self.genderLineEdit_3.setFont(font)
        self.genderLineEdit_3.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.genderLineEdit_3)

        self.genderLineEdit_4 = QLineEdit(self.formLayoutWidget)
        self.genderLineEdit_4.setObjectName(u"genderLineEdit_4")
        self.genderLineEdit_4.setMinimumSize(QSize(0, 19))
        self.genderLineEdit_4.setFont(font)
        self.genderLineEdit_4.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.genderLineEdit_4)

        self.genderLineEdit_5 = QLineEdit(self.formLayoutWidget)
        self.genderLineEdit_5.setObjectName(u"genderLineEdit_5")
        self.genderLineEdit_5.setMinimumSize(QSize(0, 19))
        self.genderLineEdit_5.setFont(font)
        self.genderLineEdit_5.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.genderLineEdit_5)

        self.genderLineEdit_6 = QLineEdit(self.formLayoutWidget)
        self.genderLineEdit_6.setObjectName(u"genderLineEdit_6")
        self.genderLineEdit_6.setMinimumSize(QSize(0, 19))
        self.genderLineEdit_6.setFont(font)
        self.genderLineEdit_6.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.genderLineEdit_6)

        self.Add_Patient_2 = QPushButton(Add_Patient_Screen)
        self.Add_Patient_2.setObjectName(u"Add_Patient_2")
        self.Add_Patient_2.setGeometry(QRect(0, 220, 391, 71))
        self.Add_Patient_2.setFont(font)
        self.Add_Patient_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"    font: 12pt\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.retranslateUi(Add_Patient_Screen)

        QMetaObject.connectSlotsByName(Add_Patient_Screen)
    # setupUi

    def retranslateUi(self, Add_Patient_Screen):
        Add_Patient_Screen.setWindowTitle(QCoreApplication.translate("Add_Patient_Screen", u"Dialog", None))
        self.genderLabel.setText(QCoreApplication.translate("Add_Patient_Screen", u"Gender", None))
        self.heightLabel_2.setText(QCoreApplication.translate("Add_Patient_Screen", u"Height (in)", None))
        self.ageLabel_2.setText(QCoreApplication.translate("Add_Patient_Screen", u"Age", None))
        self.shoeSizeLabel.setText(QCoreApplication.translate("Add_Patient_Screen", u"Shoe Size", None))
        self.weightLabel_2.setText(QCoreApplication.translate("Add_Patient_Screen", u"Weight (lbs)", None))
        self.weightLabel.setText(QCoreApplication.translate("Add_Patient_Screen", u"Subject ID", None))
        self.Add_Patient_2.setText(QCoreApplication.translate("Add_Patient_Screen", u"Add Patient", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add_SimulationpGNHFq.ui'
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


class Ui_Add_Simulation_Screen(object):
    def setupUi(self, Add_Simulation_Screen):
        if Add_Simulation_Screen.objectName():
            Add_Simulation_Screen.setObjectName(u"Add_Simulation_Screen")
        Add_Simulation_Screen.resize(391, 300)
        Add_Simulation_Screen.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);")
        self.formLayoutWidget = QWidget(Add_Simulation_Screen)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 391, 141))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.nameLabel = QLabel(self.formLayoutWidget)
        self.nameLabel.setObjectName(u"nameLabel")
        font = QFont()
        font.setFamily(u"MS Reference Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nameLabel.setFont(font)
        self.nameLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(self.formLayoutWidget)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setMinimumSize(QSize(0, 19))
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameLineEdit)

        self.distanceLabel = QLabel(self.formLayoutWidget)
        self.distanceLabel.setObjectName(u"distanceLabel")
        self.distanceLabel.setFont(font)
        self.distanceLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.distanceLabel)

        self.distLineEdit = QLineEdit(self.formLayoutWidget)
        self.distLineEdit.setObjectName(u"distLineEdit")
        self.distLineEdit.setMinimumSize(QSize(0, 19))
        self.distLineEdit.setFont(font)
        self.distLineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.distLineEdit)

        self.speedLabel = QLabel(self.formLayoutWidget)
        self.speedLabel.setObjectName(u"speedLabel")
        self.speedLabel.setFont(font)
        self.speedLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.speedLabel)

        self.speedLineEdit = QLineEdit(self.formLayoutWidget)
        self.speedLineEdit.setObjectName(u"speedLineEdit")
        self.speedLineEdit.setMinimumSize(QSize(0, 19))
        self.speedLineEdit.setFont(font)
        self.speedLineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.speedLineEdit)

        self.directionLabel = QLabel(self.formLayoutWidget)
        self.directionLabel.setObjectName(u"directionLabel")
        self.directionLabel.setFont(font)
        self.directionLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.directionLabel)

        self.dirLineEdit = QLineEdit(self.formLayoutWidget)
        self.dirLineEdit.setObjectName(u"dirLineEdit")
        self.dirLineEdit.setMinimumSize(QSize(0, 19))
        self.dirLineEdit.setFont(font)
        self.dirLineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dirLineEdit)

        self.Add_Simulation = QPushButton(Add_Simulation_Screen)
        self.Add_Simulation.setObjectName(u"Add_Simulation")
        self.Add_Simulation.setGeometry(QRect(0, 220, 391, 71))
        self.Add_Simulation.setFont(font)
        self.Add_Simulation.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"    font: 12pt\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.label = QLabel(Add_Simulation_Screen)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 140, 391, 41))
        self.label.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")
        self.label_2 = QLabel(Add_Simulation_Screen)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 180, 191, 31))
        self.label_2.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")
        self.label_3 = QLabel(Add_Simulation_Screen)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 180, 201, 31))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.retranslateUi(Add_Simulation_Screen)

        QMetaObject.connectSlotsByName(Add_Simulation_Screen)
    # setupUi

    def retranslateUi(self, Add_Simulation_Screen):
        Add_Simulation_Screen.setWindowTitle(QCoreApplication.translate("Add_Simulation_Screen", u"Dialog", None))
        self.nameLabel.setText(QCoreApplication.translate("Add_Simulation_Screen", u"Name", None))
        self.distanceLabel.setText(QCoreApplication.translate("Add_Simulation_Screen", u"Distance (cm)", None))
        self.speedLabel.setText(QCoreApplication.translate("Add_Simulation_Screen", u"Speed (cm/s)", None))
        self.directionLabel.setText(QCoreApplication.translate("Add_Simulation_Screen", u"Direction", None))
        self.Add_Simulation.setText(QCoreApplication.translate("Add_Simulation_Screen", u"Add Simulation", None))
        self.label.setText(QCoreApplication.translate("Add_Simulation_Screen", u"1 for Forward, 2 for Backwards, 3 for Right, 4 for Left", None))
        self.label_2.setText(QCoreApplication.translate("Add_Simulation_Screen", u"Max Distance: 14 cm", None))
        self.label_3.setText(QCoreApplication.translate("Add_Simulation_Screen", u"Max Speed: 70 cm/s", None))
    # retranslateUi


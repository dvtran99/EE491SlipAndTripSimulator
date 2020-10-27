# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_WindowcPweGt.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"MS Reference Sans Serif")
        self.Btn_Toggle.setFont(font)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Patient = QPushButton(self.frame_top_menus)
        self.Patient.setObjectName(u"Patient")
        self.Patient.setMinimumSize(QSize(0, 40))
        self.Patient.setFont(font)
        self.Patient.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Patient.setAutoDefault(True)

        self.verticalLayout_4.addWidget(self.Patient)

        self.Platform = QPushButton(self.frame_top_menus)
        self.Platform.setObjectName(u"Platform")
        self.Platform.setMinimumSize(QSize(0, 40))
        self.Platform.setFont(font)
        self.Platform.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Platform.setAutoDefault(True)

        self.verticalLayout_4.addWidget(self.Platform)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Patient_Information = QWidget()
        self.Patient_Information.setObjectName(u"Patient_Information")
        self.Add_Patient = QPushButton(self.Patient_Information)
        self.Add_Patient.setObjectName(u"Add_Patient")
        self.Add_Patient.setGeometry(QRect(0, 0, 251, 71))
        font1 = QFont()
        font1.setFamily(u"MS Reference Sans Serif")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.Add_Patient.setFont(font1)
        self.Add_Patient.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"    font: 12pt\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.listWidget = QListWidget(self.Patient_Information)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 70, 251, 361))
        self.listWidget.setFont(font1)
        self.listWidget.setMouseTracking(True)
        self.listWidget.setTabletTracking(True)
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")
        self.formLayoutWidget = QWidget(self.Patient_Information)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(260, 0, 641, 392))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(28)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.genderLabel = QLabel(self.formLayoutWidget)
        self.genderLabel.setObjectName(u"genderLabel")
        self.genderLabel.setFont(font1)
        self.genderLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.genderLabel)

        self.genderLineEdit = QLineEdit(self.formLayoutWidget)
        self.genderLineEdit.setObjectName(u"genderLineEdit")
        self.genderLineEdit.setMinimumSize(QSize(0, 19))
        self.genderLineEdit.setFont(font1)
        self.genderLineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.genderLineEdit)

        self.heightLabel = QLabel(self.formLayoutWidget)
        self.heightLabel.setObjectName(u"heightLabel")
        self.heightLabel.setFont(font1)
        self.heightLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.heightLabel)

        self.heightLineEdit = QLineEdit(self.formLayoutWidget)
        self.heightLineEdit.setObjectName(u"heightLineEdit")
        self.heightLineEdit.setFont(font1)
        self.heightLineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.heightLineEdit)

        self.ageLabel = QLabel(self.formLayoutWidget)
        self.ageLabel.setObjectName(u"ageLabel")
        self.ageLabel.setFont(font1)
        self.ageLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.ageLabel)

        self.ageLineEdit = QLineEdit(self.formLayoutWidget)
        self.ageLineEdit.setObjectName(u"ageLineEdit")
        self.ageLineEdit.setFont(font1)
        self.ageLineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ageLineEdit)

        self.shoeSizeLabel = QLabel(self.formLayoutWidget)
        self.shoeSizeLabel.setObjectName(u"shoeSizeLabel")
        self.shoeSizeLabel.setFont(font1)
        self.shoeSizeLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.shoeSizeLabel)

        self.shoeSizeLineEdit = QLineEdit(self.formLayoutWidget)
        self.shoeSizeLineEdit.setObjectName(u"shoeSizeLineEdit")
        self.shoeSizeLineEdit.setFont(font1)
        self.shoeSizeLineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.shoeSizeLineEdit)

        self.weightLabel = QLabel(self.formLayoutWidget)
        self.weightLabel.setObjectName(u"weightLabel")
        self.weightLabel.setFont(font1)
        self.weightLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.weightLabel)

        self.weightLineEdit = QLineEdit(self.formLayoutWidget)
        self.weightLineEdit.setObjectName(u"weightLineEdit")
        self.weightLineEdit.setFont(font1)
        self.weightLineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.weightLineEdit)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label)

        self.Save_Patient_Info = QPushButton(self.Patient_Information)
        self.Save_Patient_Info.setObjectName(u"Save_Patient_Info")
        self.Save_Patient_Info.setGeometry(QRect(260, 290, 321, 141))
        self.Save_Patient_Info.setFont(font1)
        self.Save_Patient_Info.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"    font: 12pt\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Delete_Patient_Info = QPushButton(self.Patient_Information)
        self.Delete_Patient_Info.setObjectName(u"Delete_Patient_Info")
        self.Delete_Patient_Info.setGeometry(QRect(590, 290, 311, 141))
        self.Delete_Patient_Info.setFont(font1)
        self.Delete_Patient_Info.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"    font: 12pt\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.stackedWidget.addWidget(self.Patient_Information)
        self.Platform_Running = QWidget()
        self.Platform_Running.setObjectName(u"Platform_Running")
        self.Run_Simulation = QPushButton(self.Platform_Running)
        self.Run_Simulation.setObjectName(u"Run_Simulation")
        self.Run_Simulation.setGeometry(QRect(660, 0, 241, 431))
        font2 = QFont()
        font2.setFamily(u"MS Reference Sans Serif")
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setWeight(50)
        self.Run_Simulation.setFont(font2)
        self.Run_Simulation.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.simulationlist = QListWidget(self.Platform_Running)
        self.simulationlist.setObjectName(u"simulationlist")
        self.simulationlist.setGeometry(QRect(0, 70, 251, 361))
        self.simulationlist.setFont(font1)
        self.simulationlist.setStyleSheet(u"QListWidget {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")
        self.Add_Simulation = QPushButton(self.Platform_Running)
        self.Add_Simulation.setObjectName(u"Add_Simulation")
        self.Add_Simulation.setGeometry(QRect(0, 0, 251, 71))
        self.Add_Simulation.setFont(font1)
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
        self.Save_Simulation = QPushButton(self.Platform_Running)
        self.Save_Simulation.setObjectName(u"Save_Simulation")
        self.Save_Simulation.setGeometry(QRect(250, 290, 201, 141))
        self.Save_Simulation.setFont(font1)
        self.Save_Simulation.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"    font: 12pt\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.formLayoutWidget_2 = QWidget(self.Platform_Running)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(260, 0, 391, 201))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(50)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.distanceLabel = QLabel(self.formLayoutWidget_2)
        self.distanceLabel.setObjectName(u"distanceLabel")
        self.distanceLabel.setFont(font1)
        self.distanceLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.distanceLabel)

        self.distanceLineEdit_2 = QLineEdit(self.formLayoutWidget_2)
        self.distanceLineEdit_2.setObjectName(u"distanceLineEdit_2")
        self.distanceLineEdit_2.setMinimumSize(QSize(0, 19))
        self.distanceLineEdit_2.setFont(font1)
        self.distanceLineEdit_2.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.distanceLineEdit_2)

        self.speedLabel_2 = QLabel(self.formLayoutWidget_2)
        self.speedLabel_2.setObjectName(u"speedLabel_2")
        self.speedLabel_2.setFont(font1)
        self.speedLabel_2.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.speedLabel_2)

        self.speedLineEdit_2 = QLineEdit(self.formLayoutWidget_2)
        self.speedLineEdit_2.setObjectName(u"speedLineEdit_2")
        self.speedLineEdit_2.setMinimumSize(QSize(0, 19))
        self.speedLineEdit_2.setFont(font1)
        self.speedLineEdit_2.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.speedLineEdit_2)

        self.directionLabel_2 = QLabel(self.formLayoutWidget_2)
        self.directionLabel_2.setObjectName(u"directionLabel_2")
        self.directionLabel_2.setFont(font1)
        self.directionLabel_2.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.directionLabel_2)

        self.directionLineEdit_2 = QLineEdit(self.formLayoutWidget_2)
        self.directionLineEdit_2.setObjectName(u"directionLineEdit_2")
        self.directionLineEdit_2.setMinimumSize(QSize(0, 19))
        self.directionLineEdit_2.setFont(font1)
        self.directionLineEdit_2.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.directionLineEdit_2)

        self.label_2 = QLabel(self.Platform_Running)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 200, 391, 41))
        font3 = QFont()
        font3.setFamily(u"MS Reference Sans Serif")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 10pt\n"
"}")
        self.Delete_Simulation = QPushButton(self.Platform_Running)
        self.Delete_Simulation.setObjectName(u"Delete_Simulation")
        self.Delete_Simulation.setGeometry(QRect(450, 290, 211, 141))
        self.Delete_Simulation.setFont(font1)
        self.Delete_Simulation.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"    font: 12pt\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.stackedWidget.addWidget(self.Platform_Running)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"SCREENS", None))
        self.Patient.setText(QCoreApplication.translate("MainWindow", u"Patient", None))
        self.Platform.setText(QCoreApplication.translate("MainWindow", u"Platform", None))
        self.Add_Patient.setText(QCoreApplication.translate("MainWindow", u"Add Patient", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.listWidget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.genderLabel.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.heightLabel.setText(QCoreApplication.translate("MainWindow", u"Height (in)", None))
        self.ageLabel.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.shoeSizeLabel.setText(QCoreApplication.translate("MainWindow", u"Shoe Size", None))
        self.weightLabel.setText(QCoreApplication.translate("MainWindow", u"Weight (lbs)", None))
        self.label.setText("")
        self.Save_Patient_Info.setText(QCoreApplication.translate("MainWindow", u"Save Patient Information", None))
        self.Delete_Patient_Info.setText(QCoreApplication.translate("MainWindow", u"Delete Patient Information", None))
        self.Run_Simulation.setText(QCoreApplication.translate("MainWindow", u"RUN SIMULATION", None))
        self.Add_Simulation.setText(QCoreApplication.translate("MainWindow", u"Add Simulation", None))
        self.Save_Simulation.setText(QCoreApplication.translate("MainWindow", u"Save Simulation", None))
        self.distanceLabel.setText(QCoreApplication.translate("MainWindow", u"Distance (cm)", None))
        self.speedLabel_2.setText(QCoreApplication.translate("MainWindow", u"Speed (cm/s)", None))
        self.directionLabel_2.setText(QCoreApplication.translate("MainWindow", u"Direction", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Input Number: 1:Forward, 2:Backwards, 3:Right, 4:Left", None))
        self.Delete_Simulation.setText(QCoreApplication.translate("MainWindow", u"Delete Simulation", None))
    # retranslateUi

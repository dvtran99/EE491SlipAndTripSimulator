import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QTimer)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
import Database

## ==> SPLASH SCREEN
from SplashScreen import Ui_SplashScreen

## ==> MAIN WINDOW
from Main_Window import Ui_MainWindow
from Main_Window_Functions import *

## ==> Add Dialogs
from Add_Patient import *
from Add_Simulation import *
from Delete_Patient_Confirmation import *
from Delete_Simulation_Confirmation import *
from Error_Message import *
from Wait_Screen import *
import time

## ==> Add PMW Library
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

myPWM = "P8_13"
myPWM2 = "P8_19"

dir1 = "P8_10"
GPIO.setup(dir1, GPIO.OUT)
dir2 = "P8_12"
GPIO.setup(dir2, GPIO.OUT)
dir3 = "P8_14"
GPIO.setup(dir3, GPIO.OUT)
dir4 = "P8_16"
GPIO.setup(dir4, GPIO.OUT)

## ==> GLOBALS
counter = 0
simulation = "" ##Used to run the simulation

# YOUR APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # MAIN WINDOW LABEL
        self.ui.Patient.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Patient_Information))
        self.ui.Platform.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Platform_Running))
        self.ui.Add_Patient.clicked.connect(self.Add_Patient)
        self.ui.Add_Simulation.clicked.connect(self.Add_Simulation)
        self.ui.Save_Patient_Info.clicked.connect(self.Save_Patient)
        self.ui.Save_Simulation.clicked.connect(self.Save_Simulation)
        self.ui.Delete_Patient_Info.clicked.connect(self.Delete_Patient_Screen)
        self.ui.Delete_Simulation.clicked.connect(self.Delete_Simulation_Screen)
        self.ui.Run_Simulation.clicked.connect(self.Run_Simulation)

        # Populate lists
        self.Reload_Lists()
        self.ui.listWidget.itemSelectionChanged.connect(self.Update_Patient_Fields)
        self.ui.simulationlist.itemSelectionChanged.connect(self.Update_Simulation_Fields)

    # ADD PATIENT WINDOW
    def Add_Patient(self):
        self.Add_Patient_Screen = QDialog()
        self.Add_Patient_Screen.ui = Ui_Add_Patient_Screen()
        self.Add_Patient_Screen.ui.setupUi(self.Add_Patient_Screen)
        self.Add_Patient_Screen.ui.Add_Patient_2.clicked.connect(self.Write_New_Patient)
        self.Add_Patient_Screen.exec_()

    def Write_New_Patient(self):
        if (self.Add_Patient_Screen.ui.genderLineEdit.text() != '') and \
        (self.Add_Patient_Screen.ui.genderLineEdit_2.text() != '') and \
        (self.Add_Patient_Screen.ui.genderLineEdit_3.text() != '') and \
        (self.Add_Patient_Screen.ui.genderLineEdit_4.text() != '') and \
        (self.Add_Patient_Screen.ui.genderLineEdit_5.text() != '') and \
        (self.Add_Patient_Screen.ui.genderLineEdit_6.text() != ''):
            Subject_ID = self.Add_Patient_Screen.ui.genderLineEdit.text()
            New_Patient = {
                self.Add_Patient_Screen.ui.genderLabel.text() : self.Add_Patient_Screen.ui.genderLineEdit_2.text(),
                self.Add_Patient_Screen.ui.heightLabel_2.text() : self.Add_Patient_Screen.ui.genderLineEdit_3.text(),
                self.Add_Patient_Screen.ui.ageLabel_2.text() : self.Add_Patient_Screen.ui.genderLineEdit_4.text(),
                self.Add_Patient_Screen.ui.shoeSizeLabel.text() : self.Add_Patient_Screen.ui.genderLineEdit_5.text(),
                self.Add_Patient_Screen.ui.weightLabel_2.text() : self.Add_Patient_Screen.ui.genderLineEdit_6.text()
            }
            Database.patient_information[Subject_ID] = New_Patient
            Database.write_to_database()
            self.Reload_Lists()
            self.Add_Patient_Screen.close()

    # PATIENT TAB
    def Save_Patient(self):
        if (self.ui.genderLineEdit.text() != '') and \
        (self.ui.heightLineEdit.text() != '') and \
        (self.ui.ageLineEdit.text() != '') and \
        (self.ui.shoeSizeLineEdit.text() != '') and \
        (self.ui.weightLineEdit.text() != ''):
            Subject_ID = self.ui.listWidget.currentItem().text()
            Patient = {
                self.ui.genderLabel.text() : self.ui.genderLineEdit.text(),
                self.ui.heightLabel.text() : self.ui.heightLineEdit.text(),
                self.ui.ageLabel.text() : self.ui.ageLineEdit.text(),
                self.ui.shoeSizeLabel.text() : self.ui.shoeSizeLineEdit.text(),
                self.ui.weightLabel.text() : self.ui.weightLineEdit.text()
            }
            Database.patient_information[Subject_ID] = Patient
            Database.write_to_database()
    def Delete_Patient_Screen(self):
        if (self.ui.genderLineEdit.text() != '') and \
        (self.ui.heightLineEdit.text() != '') and \
        (self.ui.ageLineEdit.text() != '') and \
        (self.ui.shoeSizeLineEdit.text() != '') and \
        (self.ui.weightLineEdit.text() != ''):
            self.Delete_Patient_Screen = QDialog()
            self.Delete_Patient_Screen.ui = Ui_Delete_Patient_Screen()
            self.Delete_Patient_Screen.ui.setupUi(self.Delete_Patient_Screen)
            self.Delete_Patient_Screen.ui.Yes_Button.clicked.connect(self.Delete_Patient)
            self.Delete_Patient_Screen.ui.No_Button.clicked.connect(self.close_delete_patient_screen)
            self.Delete_Patient_Screen.exec_()

    def Delete_Patient(self):
        Subject_ID = self.ui.listWidget.currentItem().text()
        # Clear selection and line edits
        self.ui.listWidget.clearSelection()
        self.ui.genderLineEdit.setText("")
        self.ui.heightLineEdit.setText("")
        self.ui.ageLineEdit.setText("")
        self.ui.shoeSizeLineEdit.setText("")
        self.ui.weightLineEdit.setText("")
        # Delete from local data structure and database
        del Database.patient_information[Subject_ID]
        Database.write_to_database()
        self.Reload_Lists()
        self.Delete_Patient_Screen.close()

    def close_delete_patient_screen(self):
        self.Delete_Patient_Screen.close()

    def close_delete_simulation_screen(self):
        self.Delete_Simulation_Screen.close()

    def Reload_Lists(self):
        # Patient Information
        self.ui.listWidget.clear()
        for patient in Database.patient_information:
            self.ui.listWidget.addItem(patient)
        # Custom Simulation
        self.ui.simulationlist.clear()
        for simulation in Database.custom_simulation:
            self.ui.simulationlist.addItem(simulation)
    def Update_Patient_Fields(self):
        patient = self.ui.listWidget.currentItem().text()
        self.ui.genderLineEdit.setText(Database.patient_information[patient][self.ui.genderLabel.text()])
        self.ui.heightLineEdit.setText(Database.patient_information[patient][self.ui.heightLabel.text()])
        self.ui.ageLineEdit.setText(Database.patient_information[patient][self.ui.ageLabel.text()])
        self.ui.shoeSizeLineEdit.setText(Database.patient_information[patient][self.ui.shoeSizeLabel.text()])
        self.ui.weightLineEdit.setText(Database.patient_information[patient][self.ui.weightLabel.text()])

    def Add_Simulation(self):
        self.Add_Simulation_Screen = QDialog()
        self.Add_Simulation_Screen.ui = Ui_Add_Simulation_Screen()
        self.Add_Simulation_Screen.ui.setupUi(self.Add_Simulation_Screen)
        self.Add_Simulation_Screen.ui.Add_Simulation.clicked.connect(self.Write_New_Simulation)
        self.Add_Simulation_Screen.exec_()

    def Write_New_Simulation(self):
        error = 0;
        if (self.Add_Simulation_Screen.ui.nameLineEdit.text() != '') and \
        (self.Add_Simulation_Screen.ui.distLineEdit.text() != '') and \
        (self.Add_Simulation_Screen.ui.speedLineEdit.text() != '') and \
        (self.Add_Simulation_Screen.ui.dirLineEdit.text() != ''):
            try:
                int(self.Add_Simulation_Screen.ui.distLineEdit.text())
            except ValueError:
                self.Add_Simulation_Screen.close()
                self.Error_Message_Screen = QDialog()
                self.Error_Message_Screen.ui = Ui_Error_Message_Screen()
                self.Error_Message_Screen.ui.setupUi(self.Error_Message_Screen)
                self.Error_Message_Screen.ui.Close_Error.clicked.connect(self.Error_Message_Screen.close)
                self.Error_Message_Screen.ui.Error_Message.append('Distance value not accepted. Please enter whole numbers only with no units. For example: 12.')
                self.Error_Message_Screen.exec_()
                error = 1;
            try:
                int(self.Add_Simulation_Screen.ui.speedLineEdit.text())
            except ValueError:
                self.Add_Simulation_Screen.close()
                self.Error_Message_Screen = QDialog()
                self.Error_Message_Screen.ui = Ui_Error_Message_Screen()
                self.Error_Message_Screen.ui.setupUi(self.Error_Message_Screen)
                self.Error_Message_Screen.ui.Close_Error.clicked.connect(self.Error_Message_Screen.close)
                self.Error_Message_Screen.ui.Error_Message.append('Speed value not accepted. Please enter whole numbers only with no units. For example: 50.')
                self.Error_Message_Screen.exec_()
                error = 1;
            try:
                int(self.Add_Simulation_Screen.ui.dirLineEdit.text())
            except ValueError:
                self.Add_Simulation_Screen.close()
                self.Error_Message_Screen = QDialog()
                self.Error_Message_Screen.ui = Ui_Error_Message_Screen()
                self.Error_Message_Screen.ui.setupUi(self.Error_Message_Screen)
                self.Error_Message_Screen.ui.Close_Error.clicked.connect(self.Error_Message_Screen.close)
                self.Error_Message_Screen.ui.Error_Message.append('Direction value not accepted. Please enter whole numbers only with no units. For example: 3.')
                self.Error_Message_Screen.exec_()
                error = 1;
            if(error == 0):
                if int(self.Add_Simulation_Screen.ui.distLineEdit.text()) > 14 or int(self.Add_Simulation_Screen.ui.distLineEdit.text()) <= 0:
                    self.Add_Simulation_Screen.close()
                    self.Error_Message_Screen = QDialog()
                    self.Error_Message_Screen.ui = Ui_Error_Message_Screen()
                    self.Error_Message_Screen.ui.setupUi(self.Error_Message_Screen)
                    self.Error_Message_Screen.ui.Close_Error.clicked.connect(self.Error_Message_Screen.close)
                    self.Error_Message_Screen.ui.Error_Message.append('Distance value is out of range. Please enter a number between 1 and 14.')
                    self.Error_Message_Screen.exec_()
                    error = 1;
                if int(self.Add_Simulation_Screen.ui.speedLineEdit.text()) > 70 or int(self.Add_Simulation_Screen.ui.speedLineEdit.text()) <= 0:
                    self.Add_Simulation_Screen.close()
                    self.Error_Message_Screen = QDialog()
                    self.Error_Message_Screen.ui = Ui_Error_Message_Screen()
                    self.Error_Message_Screen.ui.setupUi(self.Error_Message_Screen)
                    self.Error_Message_Screen.ui.Close_Error.clicked.connect(self.Error_Message_Screen.close)
                    self.Error_Message_Screen.ui.Error_Message.append('Speed value is out of range. Please enter a number between 1 and 70')
                    self.Error_Message_Screen.exec_()
                    error = 1;
                if int(self.Add_Simulation_Screen.ui.dirLineEdit.text()) > 4 or int(self.Add_Simulation_Screen.ui.dirLineEdit.text()) < 1:
                    self.Add_Simulation_Screen.close()
                    self.Error_Message_Screen = QDialog()
                    self.Error_Message_Screen.ui = Ui_Error_Message_Screen()
                    self.Error_Message_Screen.ui.setupUi(self.Error_Message_Screen)
                    self.Error_Message_Screen.ui.Close_Error.clicked.connect(self.Error_Message_Screen.close)
                    self.Error_Message_Screen.ui.Error_Message.append('Direction value is out of range. Please enter a number between 1 and 4.')
                    self.Error_Message_Screen.exec_()
                    error = 1;
            if(error == 0):
                Simulation_Name = self.Add_Simulation_Screen.ui.nameLineEdit.text()
                New_Simulation = {
                    self.Add_Simulation_Screen.ui.distanceLabel.text() : self.Add_Simulation_Screen.ui.distLineEdit.text(),
                    self.Add_Simulation_Screen.ui.speedLabel.text() : self.Add_Simulation_Screen.ui.speedLineEdit.text(),
                    self.Add_Simulation_Screen.ui.directionLabel.text() : self.Add_Simulation_Screen.ui.dirLineEdit.text()
                }
                Database.custom_simulation[Simulation_Name] = New_Simulation
                Database.write_to_database()
                self.Reload_Lists()
                self.Add_Simulation_Screen.close()

    def Save_Simulation(self):
        error = 0;
        if (self.ui.distanceLineEdit_2.text() != '') and \
        (self.ui.speedLineEdit_2.text() != '') and \
        (self.ui.directionLineEdit_2.text() != ''):
            try:
                int(self.ui.distanceLineEdit_2.text())
            except ValueError:
                self.Error_Message_Screen = QDialog()
                self.Error_Message_Screen.ui = Ui_Error_Message_Screen()
                self.Error_Message_Screen.ui.setupUi(self.Error_Message_Screen)
                self.Error_Message_Screen.ui.Close_Error.clicked.connect(self.Error_Message_Screen.close)
                self.Error_Message_Screen.ui.Error_Message.append('Distance value not accepted. Please enter whole numbers only with no units. For example: 50.')
                self.Error_Message_Screen.exec_()
                error = 1;
            try:
                int(self.ui.speedLineEdit_2.text())
            except ValueError:
                self.Error_Message_Screen = QDialog()
                self.Error_Message_Screen.ui = Ui_Error_Message_Screen()
                self.Error_Message_Screen.ui.setupUi(self.Error_Message_Screen)
                self.Error_Message_Screen.ui.Close_Error.clicked.connect(self.Error_Message_Screen.close)
                self.Error_Message_Screen.ui.Error_Message.append('Speed value not accepted. Please enter whole numbers only with no units. For example: 50.')
                self.Error_Message_Screen.exec_()
                error = 1;
            try:
                int(self.ui.directionLineEdit_2.text())
            except ValueError:
                self.Error_Message_Screen = QDialog()
                self.Error_Message_Screen.ui = Ui_Error_Message_Screen()
                self.Error_Message_Screen.ui.setupUi(self.Error_Message_Screen)
                self.Error_Message_Screen.ui.Close_Error.clicked.connect(self.Error_Message_Screen.close)
                self.Error_Message_Screen.ui.Error_Message.append('Direction value not accepted. Please enter whole numbers only with no units. For example: 3.')
                self.Error_Message_Screen.exec_()
                error = 1;
            if(error == 0):
                if int(self.ui.distanceLineEdit_2.text()) > 14 or int(self.ui.distanceLineEdit_2.text()) < 0:
                    self.Error_Message_Screen = QDialog()
                    self.Error_Message_Screen.ui = Ui_Error_Message_Screen()
                    self.Error_Message_Screen.ui.setupUi(self.Error_Message_Screen)
                    self.Error_Message_Screen.ui.Close_Error.clicked.connect(self.Error_Message_Screen.close)
                    self.Error_Message_Screen.ui.Error_Message.append('Distance value is out of range. Please enter a number between 1 and 14.')
                    self.Error_Message_Screen.exec_()
                    error = 1;
                if int(self.ui.speedLineEdit_2.text()) > 70 or int(self.ui.speedLineEdit_2.text()) < 0:
                    self.Error_Message_Screen = QDialog()
                    self.Error_Message_Screen.ui = Ui_Error_Message_Screen()
                    self.Error_Message_Screen.ui.setupUi(self.Error_Message_Screen)
                    self.Error_Message_Screen.ui.Close_Error.clicked.connect(self.Error_Message_Screen.close)
                    self.Error_Message_Screen.ui.Error_Message.append('Speed value is out of range. Please enter a number between 1 and 70')
                    self.Error_Message_Screen.exec_()
                    error = 1;
                if int(self.ui.directionLineEdit_2.text()) > 4 or int(self.ui.directionLineEdit_2.text()) < 1:
                    self.Error_Message_Screen = QDialog()
                    self.Error_Message_Screen.ui = Ui_Error_Message_Screen()
                    self.Error_Message_Screen.ui.setupUi(self.Error_Message_Screen)
                    self.Error_Message_Screen.ui.Close_Error.clicked.connect(self.Error_Message_Screen.close)
                    self.Error_Message_Screen.ui.Error_Message.append('Direction value is out of range. Please enter a number between 1 and 4.')
                    self.Error_Message_Screen.exec_()
                    error = 1;
            if (error == 0):
                Simulation_Name = self.ui.simulationlist.currentItem().text()
                Simulation = {
                    self.ui.distanceLabel.text(): self.ui.distanceLineEdit_2.text(),
                    self.ui.speedLabel_2.text(): self.ui.speedLineEdit_2.text(),
                    self.ui.directionLabel_2.text(): self.ui.directionLineEdit_2.text()
                }
                Database.custom_simulation[Simulation_Name] = Simulation
                Database.write_to_database()

    def Update_Simulation_Fields(self):
        Simulation = self.ui.simulationlist.currentItem().text()
        self.ui.distanceLineEdit_2.setText(Database.custom_simulation[Simulation][self.ui.distanceLabel.text()])
        self.ui.speedLineEdit_2.setText(Database.custom_simulation[Simulation][self.ui.speedLabel_2.text()])
        self.ui.directionLineEdit_2.setText(Database.custom_simulation[Simulation][self.ui.directionLabel_2.text()])

    def Delete_Simulation_Screen(self):
        if (self.ui.distanceLineEdit_2.text() != '') and \
        (self.ui.speedLineEdit_2.text() != '') and \
        (self.ui.directionLineEdit_2.text() != ''):
            self.Delete_Simulation_Screen = QDialog()
            self.Delete_Simulation_Screen.ui = Ui_Delete_Simulation_Screen()
            self.Delete_Simulation_Screen.ui.setupUi(self.Delete_Simulation_Screen)
            self.Delete_Simulation_Screen.ui.Yes_Button.clicked.connect(self.Delete_Simulation)
            self.Delete_Simulation_Screen.ui.No_Button.clicked.connect(self.close_delete_simulation_screen)
            self.Delete_Simulation_Screen.exec_()

    def Delete_Simulation(self):
        Simulation_Name = self.ui.simulationlist.currentItem().text()
        # Clear selection and line edits
        self.ui.simulationlist.clearSelection()
        self.ui.distanceLineEdit_2.setText("")
        self.ui.speedLineEdit_2.setText("")
        self.ui.directionLineEdit_2.setText("")
        # Delete from local data structure and database
        del Database.custom_simulation[Simulation_Name]
        Database.write_to_database()
        self.Reload_Lists()
        self.Delete_Simulation_Screen.close()

    def Run_Simulation(self):
        self.Wait_Screen = QDialog()
        self.Wait_Screen.ui = Ui_Wait_Screen()
        self.Wait_Screen.ui.setupUi(self.Wait_Screen)

        from time import sleep

        Simulation = self.ui.simulationlist.currentItem().text()
        requiredSpeed = Database.custom_simulation[Simulation][self.ui.speedLabel_2.text()]
        requiredDistance = Database.custom_simulation[Simulation][self.ui.distanceLabel.text()]
        direction = Database.custom_simulation[Simulation][self.ui.directionLabel_2.text()]

        R = 0.05
        maxRPM = 200
        maxSpeed = (2 * 3.14 * R) * (maxRPM / 60)
        simTime = (requiredDistance / requiredSpeed) / (2 * 3.14 * R)
        dutyCycle = (requiredSpeed / (maxSpeed * 100)) * 100
        if dutyCycle > 100:
            dutyCycle = 100
        simTime2 = (simTime * dutyCycle) / 10
        if direction == 1:
            GPIO.output(dir1, GPIO.HIGH)
            GPIO.output(dir3, GPIO.HIGH)
            PWM.start(myPWM, dutyCycle, 1000)
            PWM.start(myPWM2, dutyCycle, 1000)
            sleep(simTime)
            PWM.stop(myPWM)
            PWM.stop(myPWM2)
            GPIO.output(dir1, GPIO.LOW)
            GPIO.output(dir3, GPIO.LOW)
            sleep(5)
            GPIO.output(dir2, GPIO.HIGH)
            GPIO.output(dir4, GPIO.HIGH)
            PWM.start(myPWM, 10, 1000)
            PWM.start(myPWM2, 10, 1000)
            sleep(simTime2)
            PWM.stop(myPWM)
            PWM.stop(myPWM2)
            GPIO.output(dir2, GPIO.LOW)
            GPIO.output(dir4, GPIO.LOW)
        elif direction == 2:
            GPIO.output(dir2, GPIO.HIGH)
            GPIO.output(dir4, GPIO.HIGH)
            PWM.start(myPWM, dutyCycle, 1000)
            PWM.start(myPWM2, dutyCycle, 1000)
            sleep(simTime)
            PWM.stop(myPWM)
            PWM.stop(myPWM2)
            GPIO.output(dir2, GPIO.LOW)
            GPIO.output(dir4, GPIO.LOW)
            sleep(5)
            GPIO.output(dir1, GPIO.HIGH)
            GPIO.output(dir3, GPIO.HIGH)
            PWM.start(myPWM, 10, 1000)
            PWM.start(myPWM2, 10, 1000)
            sleep(simTime2)
            PWM.stop(myPWM)
            PWM.stop(myPWM2)
            GPIO.output(dir1, GPIO.LOW)
            GPIO.output(dir3, GPIO.LOW)
        elif direction == 3:
            GPIO.output(dir1, GPIO.HIGH)
            GPIO.output(dir2, GPIO.HIGH)
            PWM.start(myPWM, dutyCycle, 1000)
            PWM.start(myPWM2, dutyCycle, 1000)
            sleep(simTime)
            PWM.stop(myPWM)
            PWM.stop(myPWM2)
            GPIO.output(dir1, GPIO.LOW)
            GPIO.output(dir2, GPIO.LOW)
            sleep(5)
            GPIO.output(dir3, GPIO.HIGH)
            GPIO.output(dir4, GPIO.HIGH)
            PWM.start(myPWM, 10, 1000)
            PWM.start(myPWM2, 10, 1000)
            sleep(simTime2)
            PWM.stop(myPWM)
            PWM.stop(myPWM2)
            GPIO.output(dir3, GPIO.LOW)
            GPIO.output(dir4, GPIO.LOW)
        elif direction == 4:
            GPIO.output(dir3, GPIO.HIGH)
            GPIO.output(dir4, GPIO.HIGH)
            PWM.start(myPWM, dutyCycle, 1000)
            PWM.start(myPWM2, dutyCycle, 1000)
            sleep(simTime)
            PWM.stop(myPWM)
            PWM.stop(myPWM2)
            GPIO.output(dir3, GPIO.LOW)
            GPIO.output(dir4, GPIO.LOW)
            sleep(5)
            GPIO.output(dir1, GPIO.HIGH)
            GPIO.output(dir2, GPIO.HIGH)
            PWM.start(myPWM, 10, 1000)
            PWM.start(myPWM2, 10, 1000)
            sleep(simTime2)
            PWM.stop(myPWM)
            PWM.stop(myPWM2)
            GPIO.output(dir1, GPIO.LOW)
            GPIO.output(dir2, GPIO.LOW)
        PWM.cleanup()
        GPIO.cleanup()

       # QtCore.QTimer.singleShot(2000, self.Wait_Screen.close)
       # self.Wait_Screen.exec_()

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
       # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREEN AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


if __name__ == "__main__":
    Database.load_database()
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())

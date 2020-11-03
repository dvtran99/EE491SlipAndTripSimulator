import sys
import dummyUI
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal

class SelectAPatientError(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Select a Patient'
        self.left = 10
        self.top = 10
        self.width = 260
        self.height = 150
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel('ERROR: Select a patient to add/view notes.', self)
        label.adjustSize()
        label.move(30, 50)

        button = QPushButton('OK', self)
        button.move(80, 100)
        button.clicked.connect(self.close_window)

        self.show()

    def close_window(self):
        self.close()

class NoPatientNotesError(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'No Patient Notes'
        self.left = 10
        self.top = 10
        self.width = 250
        self.height = 150
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel('ERROR: Patient has no notes yet.', self)
        label.adjustSize()
        label.move(40, 50)

        button = QPushButton('OK', self)
        button.move(75, 100)
        button.clicked.connect(self.close_window)

        self.show()

    def close_window(self):
        self.close()

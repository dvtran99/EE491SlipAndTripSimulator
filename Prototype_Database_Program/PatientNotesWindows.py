import sys
import dummyUI
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal

class AddPatientNotesWindowError(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Add Patient Notes'
        self.left = 10
        self.top = 10
        self.width = 250
        self.height = 150
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel('ERROR: Please fill in every required field.', self)
        label.adjustSize()
        label.move(50, 50)

        button = QPushButton('OK', self)
        button.move(75, 100)
        button.clicked.connect(self.close_window)

        self.show()

    def close_window(self):
        self.close()

class AddPatientNotesWindow(QMainWindow):
        new_notes = pyqtSignal(str)

        def __init__(self, subject_id):
            super().__init__()
            self.title = 'Add Patient Notes'
            self.left = 10
            self.top = 10
            self.width = 420
            self.height = 260
            self.initUI(subject_id)

        def initUI(self, subject_id):
            label_width = 60
            text_width = 260
            label_text_height = 25

            self.setWindowTitle(self.title)
            self.setGeometry(self.left, self.top, self.width, self.height)
            # Subject ID
            self.id_label = QLabel('Subject ID', self)
            self.id_label.setGeometry(20, 20, label_width, label_text_height)
            self.id_label.setAlignment(Qt.AlignRight | Qt.AlignCenter)

            self.id_text = QLabel(subject_id, self)
            self.id_text.setGeometry(90, 20, text_width, label_text_height)

            # Notes
            self.notes_label = QLabel('Notes', self)
            self.notes_label.setGeometry(20, 60, label_width, label_text_height)
            self.notes_label.setAlignment(Qt.AlignRight | Qt.AlignCenter)

            self.notes_text = QPlainTextEdit(self)
            self.notes_text.setGeometry(90, 60, text_width, label_text_height * 5)

            button = QPushButton('Add', self)
            button.setGeometry(150, 220, label_width * 2, label_text_height)
            button.clicked.connect(self.close_window)

        def close_window(self, event):
            # Check if any of the text fields are empty
            if (self.notes_text.toPlainText() == ''):
                self.error_window = AddPatientNotesWindowError()
                self.error_window.show()
            else:
                self.new_notes.emit(self.notes_text.toPlainText())
                self.close()


class ViewPatientNotesWindow(QMainWindow):

    def __init__(self, subject_id, patient_notes):
        super().__init__()
        self.title = 'View Patient Notes'
        self.left = 10
        self.top = 10
        self.width = 350
        self.height = 400
        self.initUI(subject_id, patient_notes)

    def initUI(self, subject_id, patient_notes):
        label_width = 60
        text_width = 260
        label_text_height = 25

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create scroll area to show the patient notes
        self.centralWidget = QWidget()
        layout = QVBoxLayout(self.centralWidget)
        self.scrollArea = QScrollArea(self.centralWidget)
        layout.addWidget(self.scrollArea)
        self.scrollAreaWidgetContents = QListWidget()

        # Add patient notes to the list
        for date in sorted(patient_notes.keys(), reverse = True):
            self.scrollAreaWidgetContents.addItem(date + "\n    " + patient_notes[date])

        self.scrollAreaWidgetContents.setGeometry(20, 20, self.width - 20, self.height - 105)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        layout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.setCentralWidget(self.centralWidget)

        # Subject ID
        self.id_label = QLabel('Subject ID', self)
        self.id_label.setGeometry(20, self.height - 85, label_width, label_text_height)
        self.id_label.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.id_text = QLabel(subject_id, self)
        self.id_text.setGeometry(90, self.height - 85, text_width, label_text_height)

        button = QPushButton('Exit', self)
        button.move(125, self.height - 50)
        button.clicked.connect(self.close_window)

        self.show()

    def close_window(self):
        self.close()

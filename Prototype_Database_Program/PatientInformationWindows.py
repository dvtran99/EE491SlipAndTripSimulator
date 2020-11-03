import sys
import dummyUI
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal

class CreatePatientWindowError(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Create Patient'
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
        label.move(25, 50)

        button = QPushButton('OK', self)
        button.move(75, 100)
        button.clicked.connect(self.close_window)

        self.show()

    def close_window(self):
        self.close()

class CreatePatientWindow(QMainWindow):

    new_patient = pyqtSignal(str, dict)

    def __init__(self):
        super().__init__()
        self.title = 'Create Patient'
        self.left = 10
        self.top = 10
        self.width = 420
        self.height = 260
        self.initUI()

    def initUI(self):
        label_width = 120
        text_width = 200
        label_text_height = 25

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # Subject ID
        self.id_label = QLabel('Subject ID', self)
        self.id_label.setGeometry(20, 20, label_width, label_text_height)
        self.id_label.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.id_text = QLineEdit(self)
        self.id_text.setGeometry(150, 20, text_width, label_text_height)

        # Gender
        self.gender_label = QLabel('Gender', self)
        self.gender_label.setGeometry(20, 60, label_width, label_text_height)
        self.gender_label.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.gender_box = QComboBox(self)
        self.gender_box.setGeometry(150, 60, text_width, label_text_height)
        self.gender_box.addItem('Male')
        self.gender_box.addItem('Female')

        # Height
        self.height_label = QLabel('Height (in)', self)
        self.height_label.setGeometry(20, 100, label_width, label_text_height)
        self.height_label.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.height_text = QLineEdit(self)
        self.height_text.setGeometry(150, 100, text_width, label_text_height)

        # Birth date
        self.birth_label = QLabel('Birth Date', self)
        self.birth_label.setGeometry(20, 140, label_width, label_text_height)
        self.birth_label.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.birth_date = QDateEdit(self)
        self.birth_date.setGeometry(150, 140, text_width, label_text_height)

        # Shoe size
        self.shoe_label = QLabel('Shoe Size', self)
        self.shoe_label.setGeometry(20, 180, label_width, label_text_height)
        self.shoe_label.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.shoe_text = QLineEdit(self)
        self.shoe_text.setGeometry(150, 180, text_width, label_text_height)

        button = QPushButton('Create', self)
        button.setGeometry(150, 220, label_width, label_text_height)
        button.clicked.connect(self.close_window)

    def close_window(self, event):
        # Check if any of the text fields are empty
        if (self.id_text.text() == '') or (self.height_text.text() == '') or \
        (self.shoe_text.text() == ''):
            self.error_window = CreatePatientWindowError()
            self.error_window.show()
        else:
            self.new_patient.emit(self.id_text.text(),
            {
                self.gender_label.text() : self.gender_box.currentText(),
                self.height_label.text() : self.height_text.text(),
                self.birth_label.text() : self.birth_date.date().toString(),
                self.shoe_label.text() : self.shoe_text.text()
            })
            self.close()

class LoadPatientWindowError(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Load Patient'
        self.left = 10
        self.top = 10
        self.width = 250
        self.height = 150
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel('ERROR: Please select a patient.', self)
        label.adjustSize()
        label.move(50, 50)

        button = QPushButton('OK', self)
        button.move(75, 100)
        button.clicked.connect(self.close_window)

        self.show()

    def close_window(self):
        self.close()

class LoadPatientWindow(QMainWindow):

    selected_patient = pyqtSignal(str)
    patient_name = ''

    def __init__(self, patient_information):
        super().__init__()
        self.title = 'Load Patient'
        self.left = 10
        self.top = 10
        self.width = 280
        self.height = 250
        self.initUI(patient_information)

    def initUI(self, patient_information):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create scroll area to show the custom simulations
        self.centralWidget = QWidget()
        layout = QVBoxLayout(self.centralWidget)
        self.scrollArea = QScrollArea(self.centralWidget)
        layout.addWidget(self.scrollArea)
        self.scrollAreaWidgetContents = QListWidget()
        self.scrollAreaWidgetContents.itemSelectionChanged.connect(self.update_selection)

        # Add custom simulations to the table
        for patient in patient_information:
            self.scrollAreaWidgetContents.addItem(patient)
        self.scrollAreaWidgetContents.setGeometry(20, 20, self.width - 20, self.height - 70)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        layout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.setCentralWidget(self.centralWidget)

        button = QPushButton('OK', self)
        button.move(90, self.height - 50)
        button.clicked.connect(self.close_window)

        self.show()


    def update_selection(self):
        self.patient_name = self.scrollAreaWidgetContents.currentItem().text()

    def close_window(self):
        # Check if a simulation has been selected
        if self.patient_name == '':
            self.error_window = LoadPatientWindowError()
            self.error_window.show()
        else:
            self.selected_patient.emit(self.patient_name)
            self.close()

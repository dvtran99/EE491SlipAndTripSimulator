import sys
import Database
import PatientInformationWindows
import CustomSimulationWindows
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel
from PyQt5.QtCore import Qt

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'dummyUI'
        self.left = 10
        self.top = 10
        self.width = 900
        self.height = 280
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        new_patient = QPushButton('New Patient', self)
        new_patient.setGeometry(100, 70, 100, 25)
        new_patient.clicked.connect(self.new_patient_click)

        existing_patient = QPushButton('Existing Patient', self)
        existing_patient.setGeometry(100, 120, 100, 25)
        existing_patient.clicked.connect(self.existing_patient_click)

        create_simulation = QPushButton('Create Simulation', self)
        create_simulation.setGeometry(250, 70, 100, 25)
        create_simulation.clicked.connect(self.create_simulation_click)

        load_simulation = QPushButton('Load Simulation', self)
        load_simulation.setGeometry(250, 120, 100, 25)
        load_simulation.clicked.connect(self.load_simulation_click)

        self.debug_text = QLabel('Debug Window', self)
        self.debug_text.setGeometry(400, 70, 400, 140)
        self.debug_text.setStyleSheet('background-color: white')
        self.debug_text.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.debug_text.setIndent(4)

        button = QPushButton('Exit', self)
        button.setGeometry(100, 170, 100, 25)
        button.clicked.connect(self.close_window)

        self.show()

    def new_patient_click(self):
        self.new_patient_window = PatientInformationWindows.CreatePatientWindow()
        self.new_patient_window.new_patient.connect(self.new_patient_handler)
        self.new_patient_window.show()

    def new_patient_handler(self, subject_id, new_patient):
        self.debug_text.setText(subject_id + "\n" + str(new_patient))
        Database.patient_information[subject_id] = new_patient
        Database.write_to_database()

    def existing_patient_click(self):
        self.existing_patient_window = PatientInformationWindows.LoadPatientWindow(Database.patient_information)
        self.existing_patient_window.selected_patient.connect(self.existing_patient_handler)
        self.existing_patient_window.show()

    def existing_patient_handler(self, subject_id):
        self.debug_text.setText(subject_id + "\n" + str(Database.patient_information[subject_id]))

    def create_simulation_click(self):
        self.create_simulation_window = CustomSimulationWindows.CreateSimulationWindow()
        self.create_simulation_window.new_simulation.connect(self.create_simulation_handler)
        self.create_simulation_window.show()

    def create_simulation_handler(self, name, new_simulation):
        self.debug_text.setText(name + "\n" + str(new_simulation))
        Database.custom_simulation[name] = new_simulation
        Database.write_to_database()

    def load_simulation_click(self):
        self.load_simulation_window = CustomSimulationWindows.LoadSimulationWindow(Database.custom_simulation)
        self.load_simulation_window.selected_simulation.connect(self.load_simulation_handler)
        self.load_simulation_window.show()

    def load_simulation_handler(self, name):
        self.debug_text.setText(name + "\n" + str(Database.custom_simulation[name]))

    def close_window(self):
        self.close()

if __name__ == '__main__':
    Database.load_database()
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

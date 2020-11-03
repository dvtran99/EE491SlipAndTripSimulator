import sys
import dummyUI
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal

class CreateSimulationWindowError(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Create Simulation'
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

class CreateSimulationWindow(QMainWindow):

    new_simulation = pyqtSignal(str, dict)

    def __init__(self):
        super().__init__()
        self.title = 'Create Simulation'
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
        # Name
        self.name_label = QLabel('Name', self)
        self.name_label.setGeometry(20, 20, label_width, label_text_height)
        self.name_label.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.name_text = QLineEdit(self)
        self.name_text.setGeometry(150, 20, text_width, label_text_height)

        # Distance
        self.distance_label = QLabel('Distance (m)', self)
        self.distance_label.setGeometry(20, 60, label_width, label_text_height)
        self.distance_label.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.distance_text = QLineEdit(self)
        self.distance_text.setGeometry(150, 60, text_width, label_text_height)

        # Duration
        self.duration_label = QLabel('Duration (s)', self)
        self.duration_label.setGeometry(20, 100, label_width, label_text_height)
        self.duration_label.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.duration_text = QLineEdit(self)
        self.duration_text.setGeometry(150, 100, text_width, label_text_height)

        # Speed
        self.speed_label = QLabel('Speed (m/s)', self)
        self.speed_label.setGeometry(20, 140, label_width, label_text_height)
        self.speed_label.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.speed_text = QLineEdit(self)
        self.speed_text.setGeometry(150, 140, text_width, label_text_height)

        # Acceleration
        self.acceleration_label = QLabel('Acceleration (m/s^2)', self)
        self.acceleration_label.setGeometry(20, 180, label_width, label_text_height)
        self.acceleration_label.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.acceleration_text = QLineEdit(self)
        self.acceleration_text.setGeometry(150, 180, text_width, label_text_height)

        button = QPushButton('Create', self)
        button.setGeometry(150, 220, label_width, label_text_height)
        button.clicked.connect(self.close_window)

    def close_window(self, event):
        # Check if any of the text fields are empty
        if (self.name_text.text() == '') or (self.distance_text.text() == '') or \
        (self.duration_text.text() == '') or (self.speed_text.text() == '') or \
        (self.acceleration_text.text() == ''):
            self.error_window = CreateSimulationWindowError()
            self.error_window.show()
        else:
            # Send a signal to the main window of the data passed back
            self.new_simulation.emit(self.name_text.text(),
                {
                    self.distance_label.text() : self.distance_text.text(),
                    self.duration_label.text() : self.duration_text.text(),
                    self.speed_label.text() : self.speed_text.text(),
                    self.acceleration_label.text() : self.acceleration_text.text()
                })
            self.close()

class LoadSimulationWindowError(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Load Simulation'
        self.left = 10
        self.top = 10
        self.width = 250
        self.height = 150
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel('ERROR: Please select a simulation.', self)
        label.adjustSize()
        label.move(50, 50)

        button = QPushButton('OK', self)
        button.move(75, 100)
        button.clicked.connect(self.close_window)

        self.show()

    def close_window(self):
        self.close()

class LoadSimulationWindow(QMainWindow):

    selected_simulation = pyqtSignal(str)
    simulation_name = ''

    def __init__(self, custom_simulation):
        super().__init__()
        self.title = 'Load Simulation'
        self.left = 10
        self.top = 10
        self.width = 480
        self.height = 450
        self.initUI(custom_simulation)

    def initUI(self, custom_simulation):
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
        for simulation in custom_simulation:
            parameters = list(custom_simulation[simulation].keys())
            description = simulation
            for parameter in parameters:
                description += '\n    ' + parameter + ': ' + custom_simulation[simulation][parameter]
            self.scrollAreaWidgetContents.addItem(description)
        self.scrollAreaWidgetContents.setGeometry(20, 20, 460, 370)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        layout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.setCentralWidget(self.centralWidget)

        button = QPushButton('OK', self)
        button.move(190, 400)
        button.clicked.connect(self.close_window)

        self.show()


    def update_selection(self):
        self.simulation_name = self.scrollAreaWidgetContents.currentItem().text().split('\n')[0]

    def close_window(self):
        # Check if a simulation has been selected
        if self.simulation_name == '':
            self.error_window = LoadSimulationWindowError()
            self.error_window.show()
        else:
            self.selected_simulation.emit(self.simulation_name)
            self.close()

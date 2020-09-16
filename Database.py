import numpy as np
import csv
import shutil

# Read csv file and format into dictionary structure

# Custom Simulation dictionary structure:
#   Key: Name of simulation
#   Value: Dictionary that stores the distance, duration, speed, and acceleration
#   of the simulation
custom_simulation_path = 'Data/Custom Simulation.csv'
custom_simulation_copy = 'Backup/Custom Simulation.csv'
custom_simulation = {}
custom_simulation_headers = []

# Patient Information dictionary structure:
#   Key: Subject ID
#   Value: Dictionary that stores gender, height, birth date, and shoe size of
#   the patient
patient_information_path = 'Data/Patient Information.csv'
patient_information_copy = 'Backup/Patient Information.csv'
patient_information = {}
patient_information_headers = []

def load_database():
    # Load custom simulations
    with open(custom_simulation_path, encoding = 'utf-8-sig') as custom_simulation_file:
        csv_reader = csv.reader(custom_simulation_file, delimiter = ',')
        # Extract headers
        global custom_simulation_headers
        custom_simulation_headers = next(csv_reader)
        for row in csv_reader:
            # First column of .csv will always be the simulation name
            name = ''
            for header, datum in zip(custom_simulation_headers, row):
                if (header == 'Name'):
                    # Create subdictionary
                    name = datum
                    custom_simulation[name] = {}
                else:
                    # Populate subdictionary
                    custom_simulation[name][header] = datum

    # Load patient information
    with open(patient_information_path, encoding = 'utf-8-sig') as patient_information_file:
        csv_reader = csv.reader(patient_information_file, delimiter = ',')
        # Extract headers
        global patient_information_headers
        patient_information_headers = next(csv_reader)
        for row in csv_reader:
            # First column of .csv will always be the subject ID
            name = ''
            for header, datum in zip(patient_information_headers, row):
                if (header == 'Subject ID'):
                    # Create subdictionary
                    name = datum
                    patient_information[name] = {}
                else:
                    # Populate subdictionary
                    patient_information[name][header] = datum

def write_to_database():
    # Create backup file
    shutil.copyfile(custom_simulation_path, custom_simulation_copy)
    # Write to custom simulations
    with open(custom_simulation_path, mode = 'w', newline = '') as output_custom_simulation:
        csv_writer = csv.writer(output_custom_simulation, delimiter = ',')
        # Write headers
        csv_writer.writerow(custom_simulation_headers)
        for simulation in list(custom_simulation.keys()):
            # First column of .csv will always be the simulation name
            name = ''
            # Create a list for each row of the output .csv file
            row = []
            for header in custom_simulation_headers:
                if (header == 'Name'):
                    name = simulation
                    row.append(name)
                else:
                    row.append(custom_simulation[name][header])
            csv_writer.writerow(row)

    # Write to patient information
    with open(patient_information_path, mode = 'w', newline = '') as output_patient_information:
        csv_writer = csv.writer(output_patient_information, delimiter = ',')
        # Write headers
        csv_writer.writerow(patient_information_headers)
        for patient in list(patient_information.keys()):
            # First column of .csv will always be the simulation name
            subject_id = ''
            # Create a list for each row of the output .csv file
            row = []
            for header in patient_information_headers:
                if (header == 'Subject ID'):
                    subject_id = patient
                    row.append(subject_id)
                else:
                    row.append(patient_information[subject_id][header])
            csv_writer.writerow(row)

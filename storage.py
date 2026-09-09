import csv
import os 
FILE_PATH = './data/entrenamientos.csv'
"""
    training = {
        'register_date': date.today(),
        'date': input_date(),
        'exercise': input_name(),
        'variant': input_variant(),
        'series': input_series(),
        'notes': input('Alguna nota?: ')
    }
"""
fieldnames = ['register_date','date','exercise','variant','# Serie','reps','weight_kg','notes']

if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
    with open(FILE_PATH, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

def save_training(training):

    with open(FILE_PATH, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        for index, serie in enumerate(training['series'], start=1):
            row = {}
            row['register_date'] = training['register_date']
            row['date'] = training['date']
            row['exercise'] = training['exercise']
            row['variant'] = training['variant']
            row['# Serie'] = index
            row['reps'] = serie['reps']
            row['weight_kg'] = serie['weight_kg']
            row['notes'] = training['notes']
            writer.writerow(row)


def get_trainings():
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

        if not rows:
            print('No hay registros')

        return rows
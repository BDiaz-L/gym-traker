import csv

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
def save_training(training):

    with open(FILE_PATH, 'a', newline='') as file:
        fieldnames = ['register_date','date','exercise','variant','# Serie','reps','weight_kg','notes']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
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
            print('row:',row)
            writer.writerow(row)


def get_trainings():
    trainings = []
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            trainings.append(row)
        return trainings
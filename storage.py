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
        writer = csv.writer(file)
        for index, serie in enumerate(training['series'], start=1):
            row = []
            row.append(training['register_date'])
            row.append(training['date'])
            row.append(training['exercise'])
            row.append(training['variant'])
            row.append(index)
            row.append(serie['reps'])
            row.append(serie['weight_kg'])
            row.append(training['notes'])
            print('row:',row)
            writer.writerow(row)


def get_trainings():
    trainings = []
    with open(FILE_PATH, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            trainings.append(row)
        return trainings
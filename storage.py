import csv

FILE_PATH = './data/entrenamientos.csv'

def save_training(training):
    print('Aqui se salva el training')
    with open(FILE_PATH, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(training.values())

from datetime import date
import storage

def input_date():
    while True:
        day = input_int_number('Dia de entrenamiento: ')
        month = input_int_number('Mes: ')
        year = input_int_number('Año: ')
        try:
            training_date  = date(year,month,day)
            if training_date <= date.today():
                return training_date
            print('No puedes registrar fecha futura')
        except ValueError:
            print('Agrega una fecha valida')

    
def input_name():
    text = (
        'Elige tu entrenamiento:\n'
        '1) Press con mancuerna a baja inclinacion\n'
        '2) Sentadilla Goblet\n'
        '3) Dominadas con agarre neutro\n'
        '4) Peso muerto rumano con mancuerna\n'
        '5) Remos en polea\n'
        '6) Superserie de elevaciones laterales\n'
        '7) Dead Bug\n'
        '8) Superserie de brazo\n'
        '9) Pantorrilla\n'
        'Opcion: '
    )
    menu = {
        '1': 'Press con mancuerna a baja inclinacion',
        '2': 'Sentadilla Goblet',
        '3': 'Dominadas con agarre neutro',
        '4': 'Peso muerto rumano con mancuerna',
        '5': 'Remos en polea',
        '6': 'Superserie de elevaciones laterales',
        '7': 'Dead Bug',
        '8': 'Superserie de brazo',
        '9': 'Pantorrilla',
    }

    return choose_menu(text, menu)
    

def input_variant():
    text = (
        'Es variante [y/n]? '
    )
    menu = {
        'y': True,
        'n': False
    }

    return choose_menu(text,menu)

def input_series():
    menu_default = {
        'y': True,
        'n': False
    }
    default_option = choose_menu('Fueron 3 series por default [y/n]? ', menu_default)
    if default_option:
        num_series = 3
    else:
        num_series = input_int_number('cuantas series hiciste? ')

    series  = []

    for contador in range(1, num_series + 1):

        reps = input_int_number(f'Cuantas repeticiones hiciste en la serie {contador}? ')
        weight = input_float_number(f'Cuanto peso ? ')
        serie = {
            'reps': reps,
            'weight_kg': weight
        }
        series.append(serie)

    return series

def choose_menu(text, menu):
    while True:
        option = input(text).strip().lower()
        value = menu.get(option)
        if value is not None:
            return value
        print('No elegiste una opción válida.')

def input_int_number(text):
    while True:
        try:
            number = int(input(text))
            if number > 0:
                return number
            print('Ingresa un número mayor a cero.')
        except ValueError:
            print('Ingresa un numero valido')

def input_float_number(text):
    while True:
        try:
            number =  float(input(text))
            if number >= 0:
                return number
            print('Ingresa un número positivo.')
        except ValueError:
            print('Ingresa un numero valido')


def training_register():
    print('Aqui registramos entrenamiento')
    training = {
        'register_date': date.today(),
        'date': input_date(),
        'exercise': input_name(),
        'variant': input_variant(),
        'series': input_series(),
        'notes': input('Alguna nota?: ')
    }
    print(f'Entrenamiento registrado: {training}')


def dummy_training():
    print('Aqui registramos entrenamiento falso')
    training = {
        'register_date': date.today(),
        'date': date.today(),
        'exercise': 'Sentadilla Goblet',
        'variant': True,
        'series': [
            {'reps': 10, 'weight_kg': 20},
            {'reps': 8, 'weight_kg': 20},
            {'reps': 10, 'weight_kg': 20}
        ],
        'notes': 'Soy una nota prueba'
    }
    
    print(f'Entrenamiento registrado: {training}')
    storage.save_training(training)

def show_trainings():
    trainings = storage.get_trainings()
    for index,training in enumerate(trainings, start=1):
        print(
            f'Registro: {index}\n'
            f'Ejercicio: {training['exercise']}\n'
            f'Serie: {training['# Serie']}\n'
            f'Reps: {training['reps']}\n'
            f'Peso: {training['weight_kg']}\n'
            f'Dia: {training['date']}\n'
        )
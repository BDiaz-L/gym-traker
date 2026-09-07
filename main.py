
import tracker


def exit_program():
    print('Saliendo...')

options = {
    '1': tracker.training_register,
    '2': exit_program
}

welcome_text = 'Bienvenido, ingresa una de las opciones:\n 1) Registrar Entrenamiento\n 2) Salir\n'

option = input(welcome_text)
function = options.get(option)

if function:
    function()
else:
    print('No elegiste una opcion valida')

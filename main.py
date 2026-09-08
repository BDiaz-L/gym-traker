import tracker

def exit_program():
    print('Saliendo...') 

options = {
    '1': tracker.training_register,
    '2': tracker.show_trainings,
    'd': tracker.dummy_training
}

welcome_text = (
    'Bienvenido, ingresa una de las opciones:\n'
    ' 1) Registrar Entrenamiento\n'
    ' 2) Obtener Entrenamientos\n'
    ' q) Salir\n'
    ' d) Dummy training\n'
    'Opcion: '
)

while True:
    option = input(welcome_text)
    if option == 'q':
        exit_program()
        break;
    
    function = options.get(option)

    if function:
        function()
    else:
        print('No elegiste una opcion valida')

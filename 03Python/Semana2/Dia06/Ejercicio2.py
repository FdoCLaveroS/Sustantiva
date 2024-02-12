# Inicialización de la agenda como un diccionario vacío
agenda = {}

# Variable para controlar si el usuario desea salir del programa
salir = False
nombreCorrecto = False
numeroCorrecto = False

# Mensaje de bienvenida
print("**** Bienvenido a AGENDA ****\n")

def validar_input(texto):
    """
    Valida si el input es una cadena de texto sin números.
    :param texto: El input a validar.
    :return: True si es válido (solo letras), False si no lo es.
    """
    return texto.isalpha()

while (not salir):

    # Bucle principal que permite al usuario agregar contactos a la agenda
    while (not nombreCorrecto):

        nombre = input("Ingresa un nombre: ")
        verificandonombre = validar_input(nombre)

        if verificandonombre == True:
            print("nombre valido")
            nombreCorrecto = True
        else:
            print("ingrese un nombre sin numeros")

    while (not numeroCorrecto):
        try:
            telefono = int(input("Ingrese un telefono:\n"))
            numeroCorrecto = True
        except ValueError:
            print("ingrese un nombre sin numeros")

    # Verifica si el nombre ya existe en la agenda
    if nombre not in agenda:
        # Si el nombre no está en la agenda, lo agrega junto con su teléfono
        agenda[nombre] = telefono
        print('Contacto guardado exitosamente!!')
        nombreCorrecto = False
        numeroCorrecto = False
    else:
        # Si el nombre ya está en la agenda, muestra un mensaje indicando que ya existe
        print('El nombre ya se encuentra en la agenda!!')

    # Pregunta al usuario si desea salir del programa
    respuesta = input("Salir? (S/N) ")

    # Si la respuesta es 'S' o 's', establece salir como True para finalizar el bucle
    if respuesta.lower() == "s":
        salir = True

# Imprime la lista de contactos almacenada en la agenda
print("Mis contactos:\n", agenda)

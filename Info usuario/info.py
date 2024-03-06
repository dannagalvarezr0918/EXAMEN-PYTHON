import os


def almacenamiento_datos():
    titulo = """
    ++++++++++++++++++++++++++++++++++++++++
    +       ALMACENAMIENTO DE DATOS        +
    ++++++++++++++++++++++++++++++++++++++++
    """
    print(titulo)

    id = input('Ingrese el id: ')
    nombres = input('Ingrese el nombre: ')
    apellidos = input('Ingrese sus apellidos: ')
    ubicacion = input('Ingrese la ubicacion: ')
    
    ciudad = input('Ingrese la ciudad: ')
    longitud = input('Ingrese la longitud: ')
    latitud = input('Ingrese la latitud: ')
    email = input('Ingrese el email: ')
    edad = input('Ingrese la edad: ')
    ocupacion = input('Ingrese su ocupacion: ')

    informacion = {
        'id': id,
        'nombres': nombres,
        'apellidos': apellidos,
        'ubicación': ubicacion,
        'dirección': {
            'ciudad': ciudad,
            'longitud': longitud,
            'latitud': latitud
        },
        'email': email,
        'edad': edad,
        'ocupación': ocupacion
    }
    print(informacion)

if __name__ == '__main__':
    almacenamiento_datos()
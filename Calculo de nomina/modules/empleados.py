from modules.corefiles import readFile

def registro():

    inventario = readFile('inventario.json')

    id = input('Ingrese el id: ')
    nombre = input('Ingrese el nombre: ')
    cargo = input('(Almacenista, Jefe IT, Administrador, Mensajero, Genrente)\nIngrese el cargo: ')
    salario = input('Ingrese el salario: ')

    empleado = {
        'id': id,
        'nombre': nombre,
        'cargo': cargo,
        'salario':salario
    }

    inventario.get('empleado').update({id:empleado})
    readFile('inventario.json', inventario)




    

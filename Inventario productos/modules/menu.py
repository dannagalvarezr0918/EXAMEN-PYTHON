from modules.corefiles import clear_screen, pause_screen,readFile

productos = {}

def main_menu():
    titulo = """
    ++++++++++++++++++++++++++++++++++++
    +    INVENTARIADO DE PRODUCTOS     +
    ++++++++++++++++++++++++++++++++++++
    """
    print(titulo)

    inventario = readFile('inventario.json')

    id = input('Ingrese el id: ')
    nombre = input('Ingrese el nombre: ')
    valorUnitario = input('Ingrese el valor unitario: ')
    stockMin = int(input('Ingrese el stock minimo del producto: '))
    stockMax = int(input('Ingrese el stock maximo del producto: '))

    producto = {
        'id': id,
        'nombre': nombre,
        'valorUnitario': valorUnitario,
        'stockmin': stockMin,
        'stockmax': stockMax,
    }

    inventario.get(productos).update(producto)
    readFile('inventario.json', inventario)
    return
    

    


    






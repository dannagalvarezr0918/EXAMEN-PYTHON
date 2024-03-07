from modules.empleados import registro
from tabulate import tabulate
def mainMenu():
    titulo = """
    +++++++++++++++++++++++++++++
    +    CALCULO DE NOMINA      +
    +++++++++++++++++++++++++++++
    """
    print(titulo)

    menu = (['1','Registro de empleado'], ['2', 'Registro informacion'], ['3', 'Colilla de pago'])
    print(tabulate(menu, tablefmt='grid'))

    op = input('Ingrese la opcion a seleccionar: ')

    if op == '1':
        registro()
        mainMenu()

    if op == '2':
        pass
    if op == '3':
        pass
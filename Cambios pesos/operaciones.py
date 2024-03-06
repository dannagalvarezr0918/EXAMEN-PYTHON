import os
from tabulate import tabulate

def cambios():

    titulo = """ 
    +++++++++++++++++++++++++++
    +     CALCULA CAMBIO      +
    +++++++++++++++++++++++++++
    """
    print(titulo)

    menu = ('1.Cambio yuanes\n2.Cambio dolar\n3.Calculo euro')
    print(menu)

    op = input('Ingrese la opcion a seleccionar: ')

    if op == '1':
        cal = float(input('Ingrese los pesos a cambiar: '))
        
        calculo_yuanes = (26.30 * cal)
        print(calculo_yuanes)
    
    if op == '2':
        cal = float(input('Ingrese los pesos a cambiar: '))
        calculo_dolar = (3944 * cal)
        print(calculo_dolar)
    
    if op == '3':
        cal = float(input('Ingrese los pesos a cambiar: '))
        calculo_euro = 4279 * cal
        print(calculo_euro)

if __name__ == '__main__':
    cambios()

     
    
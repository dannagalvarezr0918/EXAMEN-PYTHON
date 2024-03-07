import os 
import sys
import json

BASE = 'data/'

def clear_screen():
    if sys.platform == 'linux' or sys.plataform == 'darwin':
        os.system('clear')
    else:
        os.system('cls')

def pause_screen():
    if sys.platform == 'linux' or sys.plataform == 'darwin':
        x = input('Pulse enter para continuar ...')
    else:
        os.system('pause')

def checkFile(archivo:str, data):
    if(not(os.path.isfile(BASE+archivo))):
        with open (BASE+archivo, 'w') as br:
            json.dump(data, br, indent=4)

def readFile(archivo: str):
    with open(BASE+archivo, 'r') as rf:
        inventario = json.load(rf)
    return inventario
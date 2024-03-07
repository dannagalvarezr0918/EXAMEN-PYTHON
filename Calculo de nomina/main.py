from modules.corefiles import checkFile

inventariado = {
    'empleados': {},
    'datosPago': {},
    'colilla': {}
    
}

def main():
    checkFile('inventario.json', inventariado)

if __name__ == '__main__':
    main()
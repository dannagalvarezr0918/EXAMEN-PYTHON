from modules.corefiles import checkFile
from modules.menu import productos

def main():
    checkFile('inventario.json', productos)

if __name__ == '__main__':
    main()
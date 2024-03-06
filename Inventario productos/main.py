from modules.corefiles import checkFile,readFile
from modules.menu import productos, main_menu

def main():
    checkFile('inventario.json', productos)
    main_menu()

if __name__ == '__main__':
    main()
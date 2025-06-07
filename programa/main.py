from menu import Menu
from gestor_usuario import Gestor_usuario
from validador import Validador

def mostrar_bienvenida():
    print("=" * 60)
    print("👗 BIENVENIDOS A MERCED 👗".center(60))
    print("Tienda de moda accesible y global".center(60))
    print("=" * 60)

def main():
    mostrar_bienvenida()
    menu = Menu(None, Gestor_usuario([]), Validador())

    menu.menu_principal()
























































if __name__ == "__main__":
    main()
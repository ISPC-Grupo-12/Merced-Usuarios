from menu import Menu
from gestor_usuario import Gestor_usuario
from validador import Validador
def main():
    print("Iniciando")
    menu = Menu(None, Gestor_usuario([]), Validador())

    menu.menu_principal()



























































if __name__ == "__main__":
    main()
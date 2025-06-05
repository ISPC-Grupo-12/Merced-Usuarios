class Menu:
    #contructor
    def __init__(self, usuario_actual = None, gestor = None, validador = None):
        self.usuario_actual = usuario_actual
        self.gestor = gestor
        self.validador = validador

    #métodos 

    def mostrar_menu(self, opciones):
        opciones.append("Salir")
        print("\nSeleccione una opción")
        for i in range(0, len(opciones)):
            print(f"{i+1}. {opciones[i]}")
        opcion = self.validador.validar_opcion(1, len(opciones))
        return opcion

    def menu_principal(self):
        opciones = ["Iniciar Sesión", "Registrarse"]
        while True:
            opcion = self.mostrar_menu(opciones[:]) #[:] para copiar.
            if opcion == 1:
                email = input("\nIngresar email: ") #Modificar luego, con validación.
                contraseña = input("Ingresar contraseña:")  #Modificar luego, con validación.
                self.usuario_actual = self.gestor.login_usuario(email, contraseña)
                while self.usuario_actual != None:
                    if self.usuario_actual.es_admin():
                        self.menu_admin()
                    else: 
                        self.menu_estandar()
            elif opcion == 2:
                nombre = input("\nIngrese su nombre: ")
                apellido = input("Ingrese su apellido: ")
                email = input("Ingrese su email: ")
                contraseña = input("Ingresar contraseña: ")
                dni = input("Ingresar número de documento: ")
                self.gestor.registrar_usuario(nombre, apellido, email, contraseña, dni)
            else: break


    def menu_admin(self):
        opciones = ["Ver lista de usuarios", "Cambiar rol a un usuario", "Eliminar usuario"] #Agregar "Buscar usuario por id"
        roles = ["Admin", "Estándar"]
        while True:
            opcion = self.mostrar_menu(opciones[:])
            if opcion == 1:
                self.gestor.listar_usuarios()
            elif opcion == 2:
                id = int(input("\nIngresar número de id: ")) #Modificar luego, con validación.
                opcion = self.mostrar_menu(roles[:])
                if opcion <= len(roles):
                    if (self.gestor.modificar_rol(id, roles[opcion- 1])):
                        print(f"Se modificó el rol a {roles[opcion- 1]} con éxito.")
                    else:
                        print(f"No se encontró ningún usuario con el ID: {id}")
            elif opcion == 3:
                id = int(input("\nIngrese número de id del usuario que desea eliminar: ")) #Modificar luego, con validación.
                if (self.usuario_actual.id != id):
                    if(self.mostrar_menu(["Confirmar"]) == 1):
                        if (self.gestor.eliminar_usuario(id)):
                            print(f"Se eliminó el usuario con ID: {id} con éxito.")
                        else:
                            print(f"No se encontró ningún usuario con el ID: {id}")
                else:
                    print(100*"=", "\nNo se puede realizar esta acción.")
            else:
                self.usuario_actual = None
                break

    def menu_estandar(self):
        opciones = ["Ver datos personales", "Eliminar usuario", "Solicitar Admin"]
        while True:
            opcion = self.mostrar_menu(opciones[:])
            if opcion == 1:
                id = self.usuario_actual.id
                print(100*"=","\nDatos del usuario: ")
                self.gestor.buscar_usuario(id)
            elif opcion == 2:
                id = self.usuario_actual.id
                if(self.mostrar_menu(["Confirmar"]) == 1):
                    self.gestor.eliminar_usuario(id)
                    self.usuario_actual = None
                    break
            elif opcion == 3:
                if (self.gestor.modificar_rol(self.usuario_actual.id, "Admin")):
                    print("Su cambio a sido realizado con éxito.")
                    break
            else:
                self.usuario_actual = None
                break
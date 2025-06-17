class Menu:
    #contructor
    def __init__(self, usuario_actual = None, gestor = None, validador = None):
        self.usuario_actual = usuario_actual
        self.gestor = gestor
        self.validador = validador

    #métodos 

    def mostrar_menu(self, opciones):
        opciones.append("Salir")
        print("\n" + "═" * 60)
        print("📋 SELECCIONE UNA OPCIÓN".center(60))
        print("═" * 60)
        for i in range(0, len(opciones)):
            print(f"{i+1}. {opciones[i]}")
        opcion = self.validador.validar_opcion(1, len(opciones))
        return opcion

    def menu_principal(self):
        opciones = ["Iniciar Sesión", "Registrarse"]
        while True:
            opcion = self.mostrar_menu(opciones[:]) #[:] para copiar.
            if opcion == 1:
                print("\n🔐 INICIO DE SESIÓN\n".center(50, "-"))
                email = input("\nIngresar email: ") 
                while not self.validador.validar_email_patron(email):  
                    email = input("\nIngresar un email correcto: ") 
                contraseña = input("Ingresar contraseña:")  
                while not self.validador.validar_contraseña(contraseña):  
                    contraseña = input("Ingresar una contraseña correcta: ") 
                self.usuario_actual = self.gestor.login_usuario(email, contraseña)
                while self.usuario_actual != None:
                    if self.usuario_actual.es_admin():
                        self.menu_admin()
                    else: 
                        self.menu_estandar()
            elif opcion == 2:
                print("\n📝 REGISTRO DE USUARIO\n".center(50, "-"))
                nombre = input("\nIngrese su nombre: ")
                while not self.validador.validar_str(nombre):
                    nombre = input("\nIngrese un nombre válido: ")
                apellido = input("Ingrese su apellido: ")
                while not self.validador.validar_str(apellido):
                    apellido = input("\nIngrese un apellido válido: ")
                dni = input("Ingresar número de documento: ")
                while not self.validador.validar_dni(dni):
                    dni = input("\nIngresar un número de documento válido: ")
                email = input("Ingrese su email: ")
                while not self.validador.validar_email_repetido(email) and self.validador.validar_email_patron(email):  
                    email = input("\nIngresar un email correcto: ") 
                contraseña = input("Ingresar una contraseña que incluya letras y numeros:")  
                while not self.validador.validar_contraseña(contraseña): 
                    contraseña = input("Ingresar una contraseña correcta: ") 
                self.gestor.registrar_usuario(nombre, apellido, email, contraseña, dni)
                print(f"✅ Registro exitoso")
                
            else:
                print("👋 Hasta luego!")
                break


    def menu_admin(self):
        opciones = ["Ver lista de usuarios", "Buscar usuario por Id", "Cambiar rol a un usuario", "Eliminar usuario"] 
        roles = ["Estandar", "Admin"]
        while True:
            opcion = self.mostrar_menu(opciones[:])
            if opcion == 1:
                self.gestor.listar_usuarios()
            elif opcion == 2:
                id = int(input("\nIngresar número de id del usuario: ")) 
                usuario = self.gestor.buscar_usuario(id)
                if usuario is not None:
                    print(f"Usuario con el id {id}: {usuario}")
                else:
                    print(f"❌ No se encontró ningún usuario con el ID: {id}")     
            elif opcion == 3:
                id = int(input("\nIngresar número de id: ")) 
                opcion = self.mostrar_menu(roles[:])
                if opcion <= len(roles):
                    if (self.gestor.modificar_rol(id, opcion - 1)):  #En vez de revisar un str, revisa el id del Rol
                        print(f"Se modificó el rol a {roles[opcion - 1]} con éxito.")
                        if (self.usuario_actual.id == id):
                            self.usuario_actual = None
                            break
                    else:
                        print(f"❌ No se encontró ningún usuario con el ID: {id}")
            elif opcion == 4:
                id = int(input("\nIngrese número de id del usuario que desea eliminar: ")) 
                if (self.usuario_actual.id != id):
                    if(self.mostrar_menu(["Confirmar"]) == 1):
                        if (self.gestor.eliminar_usuario(id)):
                            print(f"✅ Se eliminó el usuario con ID: {id} con éxito.")
                        else:
                            print(f"❌ No se encontró ningún usuario con el ID: {id}")
                else:
                    print(100*"=", "\nNo se puede realizar esta acción.")
            else:
                
                self.usuario_actual = None
                break

    def menu_estandar(self):
        opciones = ["Ver datos personales", "Solicitar Admin", "Modificar datos personales"]
        opciones_datos= ["Modificar el nombre", "Modificar el apellido", "Modificar la contraseña"]
        while True:
            opcion = self.mostrar_menu(opciones[:])
            if opcion == 1:
                id = self.usuario_actual.id
                print(100*"=","\nDatos del usuario: ")
                print(self.gestor.buscar_usuario(id))
            elif opcion == 2:
                if (self.gestor.modificar_rol(self.usuario_actual.id, 1)):  #En vez de asignar un str al rol, se le asigna el id del Rol
                    print("✅ Su cambio a sido realizado con éxito.")
                    break
            elif opcion == 3: #segun la eleccion del usuario se modificará uno de sus datos personales
                opcion_dato= self.mostrar_menu(opciones_datos[:])
                if opcion_dato == 4:
                    break
                nuevo_dato=input(f"Por favor, ingrese el nuevo dato para {opciones_datos[opcion_dato - 1]}: ")
                if opcion_dato==3:
                    while not self.validador.validar_contraseña(nuevo_dato):
                        nuevo_dato=str(input(f"Por favor, ingrese el nuevo dato para {opciones_datos[opcion_dato -1]}: "))
                if (self.gestor.modificar_datos(self.usuario_actual.id, opcion_dato, nuevo_dato )):
                    print("✅ Su cambio a sido realizado con éxito.")
                    continue
                else:
                    print("Ocurrio un error")
                    break
                    
            else:
                self.usuario_actual = None
                break
class Validador:


    def validar_opcion(self, min, max):
        while True:
            try:
                opcion = int(input("Opción:"))
                if min <= opcion <= max:
                    return opcion
                else:
                    print(f"Error. Ingrese un valor entre {min} y {max}.\n")
            except ValueError:
                print("Por favor, ingresá un número válido.\n")

    #Agregar validar_id

    #Agregar valdiar_email

    #Agregar validar_contraseña
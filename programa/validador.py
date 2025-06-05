import re  

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

    def validar_email(self, email):
        patron= r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(patron, email) is not None #hace una comparacion basada en el patron para que el email sea veridico
    
    def validar_contraseña(self,contraseña):
        if len(contraseña)<6:
            return False
        contiene_letra= any(caracter.isalpha() for caracter in contraseña)
        contiene_numeros= any(caracter.isdigit() for caracter in contraseña)
        return contiene_letra and contiene_numeros             
    
    

class Usuario:
    #contructor
    def __init__(self, id, nombre, apellido, email, contraseña, dni):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.rol = "Estándar"
        self.dni = dni
    #métodos 
    def es_admin(self):
        return self.rol == "Admin"
    
    def validar_login(self, email, contraseña):
        return self.email == email and self.contraseña == contraseña
    
    def ver_datos(self):
        return f"\nID: {self.id}\nNombre completo: {self.apellido}, {self.nombre}\nEmail: {self.email}\nRol: {self.rol}\nDni: {self.dni}"


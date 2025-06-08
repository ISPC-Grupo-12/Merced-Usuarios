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
    
    def __str__(self):
        return f"\nID: {self.id}\nNombre completo: {self.apellido}, {self.nombre}\nDni: {self.dni}\nEmail: {self.email}\nRol: {self.rol}"


from usuario import Usuario

class Gestor_usuario:
#contructor
    def __init__(self, usuarios):
        self.usuarios = usuarios

#métodos    
    def registrar_usuario(self, nombre, apellido, email, contraseña, dni):
        if len(self.usuarios) > 0:
            id = self.usuarios[len(self.usuarios) - 1].id + 1 #Esto será identity cuando tengamos una db.
        else: 
            id = 1
        nuevo_usuario = Usuario (id, nombre, apellido, email, contraseña, dni)
        self.usuarios.append(nuevo_usuario)

    def login_usuario(self, email, contraseña):
        for u in self.usuarios:
            if u.validar_login(email, contraseña):
                return u

    def buscar_usuario(self, id):
        for u in self.usuarios:
            if u.id == id:
                print(u.ver_datos())

    def listar_usuarios(self):
        for u in self.usuarios:
            print(u.ver_datos())

    def eliminar_usuario(self, id):
        for u in self.usuarios:
            if u.id == id:
                self.usuarios.remove(u)
                return True
        return False

    def guardar_cambios(self):
        pass
    #esto tendría que commitear los cambios a la base de datos para que se guarde?

    def modificar_rol(self, id, rol):
        for u in self.usuarios:
            if u.id == id:
                u.rol = rol
                return True
        return False


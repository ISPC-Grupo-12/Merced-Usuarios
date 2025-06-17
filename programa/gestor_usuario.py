from usuario import Usuario
from rol import Rol
class Gestor_usuario:
#contructor
    def __init__(self, usuarios):
        self.__usuarios = usuarios

    @property
    def usuarios(self):
        return self.__usuarios
    
    @usuarios.setter
    def usuarios(self, usuarios):
        self.__usuarios = usuarios

#métodos    
    def registrar_usuario(self, nombre, apellido, email, contraseña, dni):
        if len(self.__usuarios) > 0:
            id = self.__usuarios[len(self.__usuarios) - 1].id + 1 #Esto será identity cuando tengamos una db.
        else: 
            id = 1
        rol = Rol(0)
        nuevo_usuario = Usuario (id, nombre, apellido, email, contraseña, dni, rol)
        self.__usuarios.append(nuevo_usuario)

    def login_usuario(self, email, contraseña):
        for u in self.__usuarios:
            if u.email == email:
                if u.contraseña == contraseña:
                    print(f"✅ Bienvenido, {u.nombre}!\n")
                    return u
                else:
                    print("❌ Contraseña incorrecta. ")
                    return None
        print("❌ Credenciales inválidas.")
        return None

    def buscar_usuario(self, id):
        for u in self.__usuarios:
            if u.id == id:
                return u

    def listar_usuarios(self):
        for u in self.__usuarios:
            print(u)

    def eliminar_usuario(self, id):
        for u in self.__usuarios:
            if u.id == id:
                self.__usuarios.remove(u)
                return True
        return False

    def modificar_datos(self, id, dato_opcion, dato_valor):
        for u in self.__usuarios:
            if u.id == id:
                if dato_opcion==1:
                    u.nombre=dato_valor
                    return True
                elif dato_opcion==2:
                    u.apellido=dato_valor
                    return True
                elif dato_opcion==3:
                    u.contraseña=dato_valor
                    return True
        return False
                
            
    def modificar_rol(self, id, id_rol): #Agregamos el id_rol y lo colocamos en u.rol = Rol(id_rol) para que busque en el objeto cual es el rol asignado.
        for u in self.__usuarios:
            if u.id == id:
                u.rol = Rol(id_rol)
                return True
        return False


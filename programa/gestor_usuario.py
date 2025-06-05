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
        for u in self.usuarios:
            if u.id == id:
                print(u)

    def listar_usuarios(self):
        for u in self.usuarios:
            print(u.ver_datos())

    def eliminar_usuario(self, id):
        for u in self.usuarios:
            if u.id == id:
                self.usuarios.remove(u)
                return True
        return False

    def modificar_datos(self, id, dato_opcion, dato_valor):
        for u in self.usuarios:
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
                
            
    def modificar_rol(self, id, rol):
        for u in self.usuarios:
            if u.id == id:
                u.rol = rol
                return True
        return False


class Rol:
    def __init__(self, id):
        self.__id = id
        self.__descripcion = "Estandar" if id == 0 else "Admin"
    
    def __str__(self):
        return self.__descripcion #por si quisieramos hacer un print del rol que nos queda, no salga el número sino el str
    
    @property
    def id(self):
        return self.__id
    
    #Creo la clase Rol, con su constructor, y en la descripcion aclaro que va a ser estandar si el id del rol es = a cero, caso contrario es Adminn. Y hago su @property.

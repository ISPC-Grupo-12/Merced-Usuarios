class Rol:
    def __init__(self, tipo):
        self.__tipo=tipo
    
    @property
    def tipo(self):
        return self.__tipo
    
    def __str__(self):
        return self.__tipo
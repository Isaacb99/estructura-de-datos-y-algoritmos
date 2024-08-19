
class Celda:
    __item: int #puede ser otro tipo de dato
    __sig: None

    def __init__(self):
        self.__item = None
        self.__sig = None

    def obtenerItem(self):
        return self.__item
    
    def cargaItem(self, item):
        self.__item = item

    def cargaSig(self, sig):
        self.__sig = sig
    
    def obtenerSig(self):
        return self.__sig
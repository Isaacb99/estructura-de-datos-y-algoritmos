class Celda:
    __item: int
    __sig: None

    def __init__(self, item=None, sig=None):
        self.__item = item
        self.__sig = sig
    
    def obtenerItem(self):
        return self.__item

    def cargaItem(self, item):
        self.__item = item
    
    def cargarSig(self, sig):
        self.__sig = sig
    
    def obtenerSig(self):
        return self.__sig
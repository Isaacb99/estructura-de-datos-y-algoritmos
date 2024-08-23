class Celda:
    __tiempo_asociado: int
    __tiempo_espera: int
    __sig: None

    def __init__(self, t_a=None, t_e=None, sig=None):
        self.__tiempo_asociado = t_a
        self.__tiempo_espera = t_e
        self.__sig = sig
    
    def obtenerTiempoAsociado(self):
        return self.__tiempo_asociado
    
    def obtenerTiempoEspera(self):
        return self.__tiempo_espera

    def cargaTiempoAsociado(self, ta):
        self.__tiempo_asociado = ta

    def cargaTiempoEspera(self, te):
        self.__tiempo_espera = te
    
    def cargarSig(self, sig):
        self.__sig = sig
    
    def obtenerSig(self):
        return self.__sig
from Entidades.dispositivo import Dispositivo

class LavaLoucas(Dispositivo): 
    def __init__(self, potencia: float,
                 codigo_dispositivo: int, 
                 modelo: str, modo: str):
        super().__init__(potencia,
                        codigo_dispositivo,
                        modelo)
        if isinstance(modo, str):
            self.__modo = modo
    
    def escolher_modo(modo): 
        pass 

    @property
    def modo(self):
        return self.__modo 
    
    @modo.setter
    def modo(self, modo: str): 
        if isinstance(modo, str):
            self.__modo = modo 
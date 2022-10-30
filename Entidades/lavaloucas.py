from Entidades.dispositivo import Dispositivo

class LavaLoucas(Dispositivo): 
    def __init__(self, nome: str, potencia: float,
                 codigo: int, modelo: str):
        super().__init__(nome, potencia,
                         codigo, modelo)
        self.__modo = None
    
    @property
    def modo(self):
        return self.__modo 
    
    def escolher_modo(self, modo: str):
        if isinstance(modo, str):
            self.__modo = modo
    

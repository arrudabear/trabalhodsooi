from Entidades.dispositivo import Dispositivo

class LavadoraDeRoupa(Dispositivo):
    def __init__(self, nome: str, potencia: float,
                 codigo: int, modelo: str):
        super().__init__(nome, potencia,
                         codigo, modelo)
        self.__modo = None

    @property
    def modo(self) -> str:
        return self.__modo
        
    def escolher_modo(self, modo: int):
        if isinstance(modo, int): 
            if modo == 1: 
                self.__modo = "Delicado"
            elif modo == 2:
                self.__modo = "Normal"
            elif modo == 3:
                self.__modo = "Rápido"
    

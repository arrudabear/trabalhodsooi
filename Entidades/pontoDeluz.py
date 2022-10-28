from Entidades.dispositivo import Dispositivo

class PontoDeLuz(Dispositivo): 
    # Metodo mudar cor ?
    def __init__(self, nome: str, potencia: float,
                 codigo: int, modelo: str):
        super().__init__(nome, potencia,
                         codigo, modelo)
    
    def ligar(self): 
        self.__estado = True 
        return self.__estado 

    def desligar(self):
        self.__estado = False 
        return self.__estado
from Entidades.dispositivo import Dispositivo

class PontoDeLuz(Dispositivo): 
    # Metodo mudar cor ?
    def __init__(self, potencia: float,
                 codigo_dispositivo: int, 
                 modelo: str):
        super().__init__(potencia,
                        codigo_dispositivo,
                        modelo)
    
    def ligar(self): 
        self.__estado = True 
        return self.__estado 

    def desligar(self):
        self.__estado = False 
        return self.__estado
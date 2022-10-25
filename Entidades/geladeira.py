from dispositivo import Dispositivo

class Geladeira(Dispositivo):
    def __init__(self, potencia: float,
                 codigo_dispositivo: int, 
                 modelo: str, temperatura: float):
        super().__init__(potencia,
                        codigo_dispositivo,
                        modelo)
        if isinstance(temperatura, float):
            self.__temperatura = temperatura
    
    @property
    def temperatura(self) -> float:
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, temperatura: float):
        if isinstance(temperatura, float):
            self.__temperatura = temperatura
        
    def aumentar_temperatura(self, temperatura: float):
        if isinstance(temperatura, float):
            self.__temperatura += temperatura
    
    def diminuir_temperatura(self, temperatura: float):
        if isinstance(temperatura, float):
            self.__temperatura -= temperatura
    

from Entidades.dispositivo import Dispositivo

class ArCondicionado(Dispositivo):
    def __init__(self, nome: str, potencia: float,
                 codigo_dispositivo: int, 
                 modelo: str):
        super().__init__(nome, potencia,
                         codigo_dispositivo,
                         modelo)
        self.__temperatura = 0.0
    
    @property
    def temperatura(self) -> float:
        return self.__temperatura
    
    def escolher_temperatura(self, temperatura: float):
        if isinstance(temperatura, float):
            self.__temperatura = temperatura
        
    def aumentar_temperatura(self, temperatura: float):
        if isinstance(temperatura, float):
            self.__temperatura += temperatura
    
    def diminuir_temperatura(self, temperatura: float):
        if isinstance(temperatura, float):
            self.__temperatura -= temperatura

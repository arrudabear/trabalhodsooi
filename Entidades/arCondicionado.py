from Entidades.dispositivo import Dispositivo

class ArCondicionado(Dispositivo):
    def __init__(self, nome: str, codigo: int, 
                 potencia: float, modelo: str):
        super().__init__(nome, codigo,
                         potencia,
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

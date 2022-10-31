from Entidades.dispositivo import Dispositivo

class Geladeira(Dispositivo):
    def __init__(self, nome: str, potencia: float,
                 codigo: int, modelo: str):
        super().__init__(nome, potencia,
                         codigo, modelo)
        self.__temperatura = 0.0
    
    @property
    def temperatura(self) -> float:
        return self.__temperatura
    
    @temperatura.setter 
    def temperatura(self, temperatura: float):
        if isinstance(temperatura, float):
            self.__temperatura = temperatura

    def aumentar_temperatura(self):
        if self.__temepratura < 7: 
            self.__temperatura += 1 

    def diminuir_temperatura(self):
        if self.__temperatura > -5: 
            self.__temperatura -= 1 

    

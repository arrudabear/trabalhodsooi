from dispositivo import Dispositivo

class Forno(Dispositivo):
    def __init__(self, estado: bool,
                potencia: float,
                tempo_ligado: float,
                timer_ligar: float,
                timer_desligar: float,
                codigo_dispositivo: int,
                modelo: str,
                temperatura: float):
        super().__init__(estado, potencia,
                        tempo_ligado, tempo_ligado,
                        timer_ligar, timer_desligar,
                        codigo_dispositivo, modelo)
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
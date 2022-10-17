from dispositivo import Dispositivo

class LavadoraDeRoupa(Dispositivo):
    def __init__(self, estado: bool,
                potencia: float,
                tempo_ligado: float,
                timer_ligar: float,
                timer_desligar: float,
                codigo_dispositivo: int,
                modelo: str,
                modo: str):
        super().__init__(estado, potencia,
                        tempo_ligado, tempo_ligado,
                        timer_ligar, timer_desligar,
                        codigo_dispositivo, modelo)
        if isinstance(modo, str):
            self.__modo = modo
    
    @property
    def modo(self) -> str:
        return self.__modo
    
    @modo.setter
    def modo(self, modo: str):
        if isinstance(modo, str):
            self.__modo = modo
        
    def escolher_modo(self, modo: str):
        if isinstance(modo, str):
            self.__modo = modo
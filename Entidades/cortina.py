from dispositivo import Dispositivo

class Cortina(Dispositivo):
    def __init__(self, estado: bool,
                 potencia: float, 
                 tempo_ligado: float, 
                 timer_ligar: float, 
                 timer_desligar: float,
                 codigo_dispositivo: int, 
                 modelo: str,
                 volume: int,
                 frequencia: float):
        super().__init__(estado, potencia, tempo_ligado, 
                         timer_ligar, timer_desligar, 
                         codigo_dispositivo, modelo)
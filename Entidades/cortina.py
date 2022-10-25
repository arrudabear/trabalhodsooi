from dispositivo import Dispositivo

class Cortina(Dispositivo):
    def __init__(self, potencia: float,
                 codigo_dispositivo: int, 
                 modelo: str):
        super().__init__(potencia,
                        codigo_dispositivo,
                        modelo)
    

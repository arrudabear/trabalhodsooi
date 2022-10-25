from dispositivo import Dispositivo

class TV(Dispositivo):
    def __init__(self, potencia: float,
                 codigo_dispositivo: int, 
                 modelo: str, volume:float,
                 canal: float):
        super().__init__(potencia,
                        codigo_dispositivo,
                        modelo)
        if isinstance(volume, float):
            self.__volume = volume 
        if isinstance(canal, float):
            self.__canal = canal 
            
    @property
    def volume(self) -> int:
        return self.__volume
    
    @volume.setter
    def volume(self, volume: int):
        if isinstance(volume, int):
            self.__volume = volume
    
    @property
    def canal(self) -> int:
        return self.__canal
    
    @canal.setter
    def canal(self, canal: int):
        if isinstance(canal, int):
            self.__canal = canal
    
    def trocar_canal(self, canal: int):
        if isinstance(canal, int):
            self.__canal = canal
    
    def aumentar_volume(self, volume: int):
        if isinstance(volume, int):
            self.__volume += volume
    
    def diminuir_volume(self, volume: int):
        if isinstance(volume, int):
            self.__volume -= volume
    
    
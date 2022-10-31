from Entidades.dispositivo import Dispositivo

class TV(Dispositivo):
    def __init__(self, nome:str, potencia: float,
                 codigo: int, modelo: str):
        super().__init__(nome, potencia,
                         codigo, modelo)
        self.__volume = 0 
        self.__canal = 0
        self.__canal_max = 100
        self.__canal_min = 1
            
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
    
    def escolher_canal(self, canal: int):
        if isinstance(canal, int):
            self.__canal = canal
    
    def aumentar_volume(self):
        if self.__volume < 100: 
            self.__volume += 1
    
    def diminuir_volume(self):
        if self.__volume > 0:
            self.__volume -= 1 

    @property
    def canal_max(self): 
        self.__canal_max 
    
    @property 
    def canal_min(self):
        self.__canal_min 
    
    
    
from Entidades.dispositivo import Dispositivo

class Som(Dispositivo): 
    # adicionar frequencia no UML;
    # metodos aumentar e diminuir frequencia
    def __init__(self, nome:str, potencia: float,
                 codigo: int, modelo: str):
        super().__init__(nome, potencia,
                         codigo, modelo)
        self.__volume = 0 
        self.__musica = None

    @property
    def volume(self): 
        return self.__volume 
    
    @property
    def musica(self): 
        return self.__musica 
    
    def escolher_musica(self, musica: float): 
        if isinstance(musica, float): 
            self.__musica= musica
    
    def aumentar_volume(self): 
        self.__volume += 1 
    
    def diminuir_volume(self): 
        self.__volume -= 1

    @volume.setter
    def volume(self, volume: int): 
        if isinstance(volume, int):
            self.__volume = volume 




        
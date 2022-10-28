from Entidades.dispositivo import Dispositivo

class Som(Dispositivo): 
    # adicionar frequencia no UML;
    # metodos aumentar e diminuir frequencia
    def __init__(self, nome:str, potencia: float,
                 codigo: int, modelo: str):
        super().__init__(nome, potencia,
                         codigo, modelo)
        self.__volume = 0 
        self.__frequencia = 0.0

    @property
    def volume(self): 
        return self.__volume 
    
    @property
    def frequencia(self): 
        return self.__frequencia 
    
    def escolher_volume(self, volume: int): 
        if isinstance(volume, int): 
            self.__volume = volume 
    
    def escolher_frequencia(self, frequencia: float): 
        if isinstance(frequencia, float): 
            self.__frequencia = frequencia
    
    def aumentar_frequencia(self): 
        self.__frequencia += 0.01 
    
    def diminuir_frequencia(self): 
        self.__frequencia -= 0.01
    
    def aumentar_volume(self): 
        self.__volume += 1 
    
    def diminuir_volume(self): 
        self.__volume -= 1




        
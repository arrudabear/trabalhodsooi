from dispositivo import Dispositivo

class Som(Dispositivo): 
    # adicionar frequencia no UML;
    # metodos aumentar e diminuir frequencia
    def __init__(self, potencia: float,
                 codigo_dispositivo: int, 
                 modelo: str, volume:float,
                 frequencia: float):
        super().__init__(potencia,
                        codigo_dispositivo,
                        modelo)
        if isinstance(volume, float):
            self.__volume = volume 
        if isinstance(frequencia, float):
            self.__frequencia = frequencia

    @property
    def volume(self): 
        return self.__volume 
    
    @property
    def frequencia(self): 
        return self.__frequencia 
    
    @volume.setter
    def volume(self, volume: int): 
        if isinstance(volume, int): 
            self.__volume = volume 
    
    @frequencia.setter
    def frequencia(self, frequencia: float): 
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




        
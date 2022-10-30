from Entidades.dispositivo import Dispositivo

class Som(Dispositivo): 
    # adicionar frequencia no UML;
    # metodos aumentar e diminuir frequencia
    def __init__(self, nome:str, potencia: float,
                 codigo: int, modelo: str):
        super().__init__(nome, potencia,
                         codigo, modelo)
        self.__volume = 0 

    @property
    def volume(self): 
        return self.__volume 
    
    @property
    def musica(self): 
        return self.__musica 
    
    def controlar_musica(self, opcao: int): 
        if opcao == 1: 
            acao = "Tocou/Pausou"
        elif opcao == 2:
            acao = "Passou"
        elif opcao == 3:
            acao = "Voltou"

        return acao 
    
    def aumentar_volume(self): 
        if self.__volume < 100:
            self.__volume += 1 
    
    def diminuir_volume(self): 
        if self.__volume > 0:
            self.__volume -= 1

    @volume.setter
    def volume(self, volume: int): 
        if isinstance(volume, int):
            self.__volume = volume 




        
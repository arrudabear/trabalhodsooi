from abc import ABC, abstractmethod

class Dispositivo(ABC):
    # deletar tempo ligado no UML 
    # codigo str 
    
    @abstractmethod
    def __init__(self, nome: str, codigo: int, potencia: float, modelo: str): 
        if isinstance(nome, str):
            self.__nome = nome 
        if isinstance(codigo, int):
            self.__codigo = codigo 
        if isinstance(potencia, float):
            self.__potencia = potencia 
        if isinstance(modelo, str): 
            self.__modelo = modelo
        self.__estado = False 
        self.__tempo_ligado = 0
        self.__timer_ligar = 0 
        self.__timer_desligar = 0

    @property
    def nome(self):
        return self.__nome 
    
    @property
    def codigo(self):
        return self.__codigo 

    @property
    def potencia(self):
        return self.__potencia

    @property
    def modelo(self):
        return self.__modelo 

    @property 
    def estado(self): 
        return self.__estado 
    
    @property
    def tempo_ligado(self):
        return self.__tempo_ligado 

    @property
    def timer_ligar(self): 
        return self.__timer_ligar 
        
    @property
    def timer_desligar(self): 
        return self.__timer_desligar 

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @codigo.setter
    def codigo(self, codigo: int): 
        if isinstance(codigo, int): 
            self.__codigo = codigo 

    @potencia.setter
    def potencia(self, potencia: float): 
        if isinstance(potencia, float): 
            self.__potencia = potencia
        
    @modelo.setter
    def modelo(self, modelo: int):
        if isinstance(modelo, int):
            self.__modelo = modelo 

    @estado.setter
    def estado(self, estado: bool): 
        if isinstance(estado, bool): 
            self.__estado = estado
    
    @tempo_ligado.setter
    def tempo_ligado(self, tempo_ligado: float): 
        if isinstance(tempo_ligado, float): 
            self.__tempo_ligado = tempo_ligado 
        
    @timer_ligar.setter
    def timer_ligar(self, timer_ligar: float): 
        if isinstance(timer_ligar, float): 
                self.__timer_ligar = timer_ligar 
        
    @timer_desligar.setter
    def timer_desligar(self, timer_desligar: float): 
        if isinstance(timer_desligar, float): 
            self.__timer_desligar = timer_desligar

    def ligar(self): 
        self.__estado = True 
            

    def desligar(self):
        self.__estado = False 
    

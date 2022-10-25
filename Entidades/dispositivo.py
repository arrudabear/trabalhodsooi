from abc import ABC, abstractmethod


class Dispositivo:
    #deletar tempo_ligado no UML 

    @abstractmethod
    def __init__(self, potencia: float,
                 codigo_dispositivo: int, 
                 modelo: str):
        if isinstance(potencia, float): 
            self.__potencia = potencia  
        if isinstance(codigo_dispositivo, int): 
            self.__codigo_dispositivo = codigo_dispositivo
        if isinstance(modelo, str): 
            self.__modelo = modelo
        self.__estado = False 
        self.__tempo_ligado = 0
        self.__timer_ligar = 0
        self.__timer_desligar = 0
        
        @property 
        def estado(self): 
            return self.__estado 

        @property
        def potencia(self): 
            return self.__potencia 
        
        @property
        def tempo_ligado(self):
            return self.__tempo_ligado 

        @property
        def timer_ligar(self): 
            return self.__timer_ligar 
        
        @property
        def timer_desligar(self): 
            return self.__timer_desligar 
        
        @property
        def codigo_dispositivo(self):
            return self.__codigo_dispositivo
        
        @property
        def modelo(self):
            return self.__modelo 
        
        @estado.setter
        def estado(self, estado: bool): 
            if isinstance(estado, bool): 
                self.__estado = estado 
        
        @potencia.setter
        def potencia(self, potencia: float): 
            if isinstance(potencia, float): 
                self.__potencia = potencia 
            
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
        
        @codigo_dispositivo.setter
        def codigo_dispositivo(self, codigo_dispositivo):
            if isinstance(codigo_dispositivo, int): 
                self.__codigo_dispositivo = codigo_dispositivo
        
        @modelo.setter
        def modelo(self, modelo: str):
            if isinstance(modelo, str):
                self.__modelo = modelo 
    
        def ligar(self): 
            self.__estado = True 
            

        def desligar(self):
            self.__estado = False 
            


                    
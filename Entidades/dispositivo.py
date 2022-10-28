

class Dispositivo:
    # deletar tempo ligado no UML 

    def __init__(self, nome: str, potencia: float, codigo: int, modelo: str):
        if isinstance(nome, str):
            self.__nome = nome 
        if isinstance(potencia, float):
            self.__potencia = potencia 
        if isinstance(codigo, int): 
            self.__codigo = codigo
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
    def potencia(self):
        return self.__potencia

    @property
    def codigo(self):
        return self.__codigo
    
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

    @potencia.setter
    def potencia(self, potencia: float): 
        if isinstance(potencia, float): 
            self.__potencia = potencia
    
    @codigo.setter
    def codigo_dispositivo(self, codigo):
        if isinstance(codigo, int): 
            self.__codigo = codigo
        
    @modelo.setter
    def modelo(self, modelo: str):
        if isinstance(modelo, str):
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
    

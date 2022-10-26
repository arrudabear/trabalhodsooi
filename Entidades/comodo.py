
class Comodo: 

    def __init__(self, nome_comodo: str): 
        if isinstance(nome_comodo, str): 
            self.__nome_comodo = nome_comodo 
        self.__dispositivos = []
    
    @property
    def nome_comodo(self):
        return self.__nome_comodo 

    @property
    def dispositivos(self): 
        return self.__dispositivos
    
    @nome_comodo.setter
    def nome_comodo(self, nome_comodo: str): 
        if isinstance(nome_comodo, str): 
            return self.__nome_comodo





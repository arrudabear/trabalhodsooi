
class Usuario():
    def __init__(self, nome: str, codigo_usuario: int):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(codigo_usuario, int):
            self.__codigo_usuario = codigo_usuario
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
    
    @property
    def codigo_usuario(self) -> int:
        return self.__codigo_usuario
    
    @codigo_usuario.setter
    def codigo_usuario(self, codigo_usuario: int):
        if isinstance(codigo_usuario, int):
            self.__codigo_usuario = codigo_usuario
    

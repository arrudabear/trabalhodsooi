from usuario import Usuario
from dispositivo import Dispositivo

class Evento():
    def __init__(self, usuario: Usuario, dispositivo: Dispositivo, data: str, horario: str):
        if isinstance(usuario, Usuario):
            self.__usuario = usuario
        if isinstance(dispositivo, Dispositivo):
            self.__dispositivo = dispositivo
        if isinstance(data, str):
            self.__data = data
        if isinstance(horario, str):
            self.__horario = horario
        
    @property
    def usuario(self) -> Usuario:
        return self.__usuario
    
    @usuario.setter
    def usuario(self, usuario: Usuario):
        if isinstance(usuario, Usuario):
            self.__usuario = usuario
    
    @property
    def dispositivo(self) -> Dispositivo:
        return self.__dispositivo
    
    @dispositivo.setter
    def dispositivo(self, dispositivo: Dispositivo):
        if isinstance(dispositivo, Dispositivo):
            self.__dispositivo = dispositivo
    
    @property
    def data(self) -> str:
        return self.__data
    
    @data.setter
    def data(self, data: str):
        if isinstance(data, str):
            self.__data = data

    @property
    def horario(self) -> str:
        return self.__horario

    @horario.setter
    def horario(self, horario: str):
        if isinstance(horario, str):
            self.__horario = horario
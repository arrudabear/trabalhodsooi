from datetime import datetime
from Entidades.usuario import Usuario
from Entidades.dispositivo import Dispositivo

class Evento():
    def __init__(self, usuario: Usuario, dispositivo: Dispositivo, acao, datahora):
        if isinstance(usuario, Usuario):
            self.__usuario = usuario
        if isinstance(dispositivo, Dispositivo):
            self.__dispositivo = dispositivo
        self.__acao = acao
        self.__datahora = datahora
        
        
    @property
    def usuario(self) -> Usuario:
        return self.__usuario
    
    @property
    def dispositivo(self) -> Dispositivo:
        return self.__dispositivo
    
    @property
    def datahora(self):
        return self.__datahora
    
    @property
    def acao(self):
        return self.__acao
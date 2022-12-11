from datetime import datetime
import uuid
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
        self.__id = uuid.uuid1()
        
        
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
    
    @property
    def id(self):
        return self.__id
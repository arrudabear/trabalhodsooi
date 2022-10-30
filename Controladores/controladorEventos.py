#from Controladores.controladorSistema import ControladorSistema
import datetime
from typing import Type
from Entidades.evento import Evento
from Entidades.usuario import Usuario
from Entidades.dispositivo import Dispositivo
from Limites.telaEvento import TelaEvento

class ControladorEventos():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_eventos = TelaEvento()
        self.__eventos = []
    
    @property
    def eventos(self) -> list:
        return self.__eventos
    
    def registrar_evento(self, usuario, dispositivo):
        datahora = datetime.datetime.now()
        try:
            if isinstance(usuario, Usuario) and isinstance(dispositivo, Dispositivo):
                evento = Evento(usuario, dispositivo, datahora)
                self.__eventos.append(evento)
            else:
                raise TypeError
        except TypeError:
            self.__tela_eventos.mostrar_mensagem("Falha ao registrar o evento.")
    
    def lista_eventos(self):
        return self.__eventos
    
    def find_evento(self, data: str, horario:str):
        for evento in self.__eventos:
            if evento.data == data and evento.horario == horario:
                return evento
    
    
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
    
    def registrar_evento(self, usuario, dispositivo, acao):
        datahora = datetime.datetime.now()
        try:
            if isinstance(usuario, Usuario) and isinstance(dispositivo, Dispositivo):
                evento = Evento(usuario, dispositivo, acao, datahora)
                self.__eventos.append(evento)
            else:
                raise TypeError
        except TypeError:
            self.__tela_eventos.mostrar_mensagem("Falha ao registrar o evento.")
    
    def lista_eventos(self):
        num = 0
        self.__tela_eventos.mostrar_mensagem("--- Registro de Eventos ---")
        for evento in self.__eventos:
            num += 1
            self.__tela_eventos.mostrar_mensagem("-"*15)
            self.__tela_eventos.mostrar_mensagem(f"Evento - {num}")
            self.__tela_eventos.mostrar_mensagem(f"Data e Hora: {evento.datahora}")
            self.__tela_eventos.mostrar_mensagem(f"Usuário: {evento.usuario.nome}")
            self.__tela_eventos.mostrar_mensagem(f"Dispositivo: {evento.dispositivo.nome}")
            self.__tela_eventos.mostrar_mensagem(f"Código do dispositivo: {evento.dispositivo.codigo}")
            self.__tela_eventos.mostrar_mensagem(f"Ação registrada: {evento.acao}")

    
    def evento_usuario(self, usuario):
        num = 0
        self.__tela_eventos.mostrar_mensagem(f"Eventos do Usuário: {usuario.nome}")
        try:
            if usuario is not None: 
                self.__tela_eventos.mostrar_mensagem(f"Eventos do Usuário: {usuario.nome}")
                for evento in self.__eventos:
                    if evento.usuario == usuario:
                        num += 1
                        self.__tela_eventos.mostrar_mensagem("-"*15)
                        self.__tela_eventos.mostrar_mensagem(f"Evento - {num}")
                        self.__tela_eventos.mostrar_mensagem(f"Data e Hora: {evento.datahora}")
                        self.__tela_eventos.mostrar_mensagem(f"Usuário: {evento.usuario.nome}")
                        self.__tela_eventos.mostrar_mensagem(f"Dispositivo: {evento.dispositivo.nome}")
                        self.__tela_eventos.mostrar_mensagem(f"Código do dispositivo: {evento.dispositivo.codigo}")
                        self.__tela_eventos.mostrar_mensagem(f"Ação registrada: {evento.acao}")
            else:
                raise KeyError
        except KeyError: 
            self.__tela_eventos.mostrar_mensagem("Usuário não existente!!")

    def evento_dispositivo(self, dispositivo):
        num = 0
        try: 
            if dispositivo is not None: 
                self.__tela_eventos.mostrar_mensagem(f"Eventos do Dispositivo: {dispositivo.nome}")
                for evento in self.__eventos:
                    if evento.dispositivo == dispositivo:
                        num += 1
                        self.__tela_eventos.mostrar_mensagem("-"*15)
                        self.__tela_eventos.mostrar_mensagem(f"Evento - {num}")
                        self.__tela_eventos.mostrar_mensagem(f"Data e Hora: {evento.datahora}")
                        self.__tela_eventos.mostrar_mensagem(f"Usuário: {evento.usuario.nome}")
                        self.__tela_eventos.mostrar_mensagem(f"Dispositivo: {evento.dispositivo.nome}")
                        self.__tela_eventos.mostrar_mensagem(f"Código do dispositivo: {evento.dispositivo.codigo}")
                        self.__tela_eventos.mostrar_mensagem(f"Ação registrada: {evento.acao}")
            else: 
                raise KeyError
        except KeyError: 
            self.__tela_eventos.mostrar_mensagem("Dispositivo não existente!!")
        
    
    
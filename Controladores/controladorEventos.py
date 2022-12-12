#from Controladores.controladorSistema import ControladorSistema
import datetime
from typing import Type
from Entidades.evento import Evento
from Entidades.usuario import Usuario
from Entidades.dispositivo import Dispositivo
from Limites.telaEvento import TelaEvento
from DAOs.eventos_dao import EventosDAO

class ControladorEventos():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__evento_DAO = EventosDAO()
        self.__tela_eventos = TelaEvento()
        self.__eventos = self.__evento_DAO.get_all()
    
    @property
    def eventos(self) -> list:
        return self.__eventos
    
    def registrar_evento(self, usuario, dispositivo, acao):
        datahora = datetime.datetime.now()
        try:
            if isinstance(usuario, Usuario) and isinstance(dispositivo, Dispositivo):
                evento = Evento(usuario, dispositivo, acao, datahora)
                self.__evento_DAO.add(evento)
                self.__eventos = self.__evento_DAO.get_all()
            else:
                raise TypeError
        except TypeError:
            self.__tela_eventos.mostrar_mensagem("Falha ao registrar o evento.")
    
    def lista_eventos(self):
        self.__eventos = self.__evento_DAO.get_all()
        dados_eventos = []
        for evento in self.__eventos:
            dados_eventos.append({'id' : evento.id})
            dados_eventos.append({'data' : evento.datahora})
            dados_eventos.append({'usuario' : evento.usuario.nome})
            dados_eventos.append({'dispositivo_nome' : evento.dispositivo.nome})
            dados_eventos.append({'dispositivo_codigo' : evento.dispositivo.codigo})
            dados_eventos.append({'acao' : evento.acao})

        self.__tela_eventos.mostrar_evento(dados_eventos)

        '''self.__tela_eventos.mostrar_mensagem("--- Registro de Eventos ---")
        for evento in self.__eventos:
            self.__tela_eventos.mostrar_mensagem("-"*15)
            self.__tela_eventos.mostrar_mensagem(f"Evento - {evento.id}")
            self.__tela_eventos.mostrar_mensagem(f"Data e Hora: {evento.datahora}")
            self.__tela_eventos.mostrar_mensagem(f"Usuário: {evento.usuario.nome}")
            self.__tela_eventos.mostrar_mensagem(f"Dispositivo: {evento.dispositivo.nome}")
            self.__tela_eventos.mostrar_mensagem(f"Código do dispositivo: {evento.dispositivo.codigo}")
            self.__tela_eventos.mostrar_mensagem(f"Ação registrada: {evento.acao}")'''

    
    def evento_usuario(self, usuario):
        self.__eventos = self.__evento_DAO.get_all()
        lista_eventos = []
        try:
            if usuario is not None: 
                self.__tela_eventos.mostrar_mensagem(f"Eventos do Usuário: {usuario.nome}")
                for evento in self.__eventos:
                    if evento.usuario == usuario:
                        lista_eventos.append(evento)

                        '''self.__tela_eventos.mostrar_mensagem("-"*15)
                        self.__tela_eventos.mostrar_mensagem(f"Evento - {num}")
                        self.__tela_eventos.mostrar_mensagem(f"Data e Hora: {evento.datahora}")
                        self.__tela_eventos.mostrar_mensagem(f"Usuário: {evento.usuario.nome}")
                        self.__tela_eventos.mostrar_mensagem(f"Dispositivo: {evento.dispositivo.nome}")
                        self.__tela_eventos.mostrar_mensagem(f"Código do dispositivo: {evento.dispositivo.codigo}")
                        self.__tela_eventos.mostrar_mensagem(f"Ação registrada: {evento.acao}")'''
                self.__tela_eventos.mostrar_evento(lista_eventos)
            else:
                raise KeyError
        except KeyError: 
            self.__tela_eventos.mostrar_mensagem("Usuário não existente!!")

    def evento_dispositivo(self, dispositivo):
        self.__eventos = self.__evento_DAO.get_all()
        lista_eventos = []
        try: 
            if dispositivo is not None: 
                self.__tela_eventos.mostrar_mensagem(f"Eventos do Dispositivo: {dispositivo.nome}")
                for evento in self.__eventos:
                    if evento.dispositivo == dispositivo:
                        lista_eventos.append(evento)
                        '''self.__tela_eventos.mostrar_mensagem("-"*15)
                        self.__tela_eventos.mostrar_mensagem(f"Evento - {num}")
                        self.__tela_eventos.mostrar_mensagem(f"Data e Hora: {evento.datahora}")
                        self.__tela_eventos.mostrar_mensagem(f"Usuário: {evento.usuario.nome}")
                        self.__tela_eventos.mostrar_mensagem(f"Dispositivo: {evento.dispositivo.nome}")
                        self.__tela_eventos.mostrar_mensagem(f"Código do dispositivo: {evento.dispositivo.codigo}")
                        self.__tela_eventos.mostrar_mensagem(f"Ação registrada: {evento.acao}")'''
                self.__tela_eventos.mostrar_evento(lista_eventos)
            else: 
                raise KeyError
        except KeyError: 
            self.__tela_eventos.mostrar_mensagem("Dispositivo não existente!!")
        
    
    
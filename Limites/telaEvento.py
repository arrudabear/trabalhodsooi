import PySimpleGUI as sg 
from Limites.tela import Tela

class TelaEvento(Tela):
    def __init__(self):
        self.__window = None
    
    def mostrar_evento(self, lista_eventos):
        string_eventos = ""
        for evento in lista_eventos:
            string_eventos = string_eventos + "Evento - " + evento.id + '\n'
            string_eventos = string_eventos + "Data e Hora: " + evento.datahora + '\n'
            string_eventos = string_eventos + "Usuário: " + evento.usuario.nome + '\n'
            string_eventos = string_eventos + "Dispositivo: " + evento.dispositivo.nome + '\n'
            string_eventos = string_eventos + "Código do dispositivo: " + evento.dispositivo.codigo + '\n'
            string_eventos = string_eventos + "Ação registrada: " + evento.acao + '\n'
            string_eventos = string_eventos + ("-"*15) + '\n'
        
        sg.Popup("--- Registro de Eventos ---", string_eventos)
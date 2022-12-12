import PySimpleGUI as sg 
from Limites.tela import Tela

class TelaEvento(Tela):
    def __init__(self):
        self.__window = None
    
    def mostrar_evento(self, lista_eventos):
        string_eventos = ""
        for evento in lista_eventos:
            string_data = str(evento.datahora)
            string_codigo = str(evento.dispositivo.codigo)
            string_id = str(evento.id)
            string_eventos = string_eventos + "Evento - " + string_id + '\n'
            string_eventos = string_eventos + "Data e Hora: " + string_data + '\n'
            string_eventos = string_eventos + "Usuário: " + evento.usuario.nome + '\n'
            string_eventos = string_eventos + "Dispositivo: " + evento.dispositivo.nome + '\n'
            string_eventos = string_eventos + "Código do dispositivo: " + string_codigo + '\n'
            string_eventos = string_eventos + "Ação registrada: " + evento.acao + '\n'
            string_eventos = string_eventos + ("-"*15) + '\n\n'
        
        sg.Popup("--- Registro de Eventos ---", string_eventos)
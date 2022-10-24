from controladorSistema import ControladorSistema
from Entidades.evento import Evento

class ControladorEventos():
    def __init__(self, controlador_sistema: ControladorSistema):
        self.__controlador_sistema = controlador_sistema
        self.__eventos = []
    
    @property
    def eventos(self) -> list:
        return self.__eventos
    
    def incluir_evento(self, evento: Evento):
        if isinstance(evento, Evento):
            self.__eventos.append(Evento)
    
    def lista_eventos(self):
        return self.__eventos
    
    def find_evento(self, data: str, horario:str):
        for evento in self.__eventos:
            if evento.data == data and evento.horario == horario:
                return evento
    
    
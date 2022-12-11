from DAOs.dao import DAO
from Entidades.evento import Evento

class EventosDAO(DAO):
    def __init__(self):
        super().__init__('eventos.pkl')
    
    def add(self, evento: Evento):
        if ((evento is not None) and isinstance(evento, Evento) and isinstance(evento.id, int)):
            super().add(evento.id, evento)

    def update(self, evento: Evento):
        if ((evento is not None) and isinstance(evento, Evento) and isinstance(evento.id, int)):
            super().update(evento.id, evento)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
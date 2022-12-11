from DAOs.dao import DAO
from Entidades.dispositivo import Dispositivo

class DispositivoDAO(DAO):
    def __init__(self):
        super().__init__('dispositivos.pkl')
    
    def add(self, dispositivo: Dispositivo):
        if ((dispositivo is not None) and isinstance(dispositivo, Dispositivo) and isinstance(dispositivo.codigo, int)):
            super().add(dispositivo.codigo, dispositivo)

    def update(self, dispositivo: Dispositivo):
        if ((dispositivo is not None) and isinstance(dispositivo, Dispositivo) and isinstance(dispositivo.codigo, int)):
            super().update(dispositivo.codigo, dispositivo)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
from DAOs.dao import DAO
from Entidades.comodo import Comodo

class ComodoDAO(DAO):
    def __init__(self):
        super().__init__('comodos.pkl')
    
    def add(self, comodo: Comodo):
        if ((comodo is not None) and isinstance(comodo, Comodo) and isinstance(comodo.nome_comodo, str)):
            super().add(comodo.nome_comodo, comodo)

    def update(self, comodo: Comodo):
        if ((comodo is not None) and isinstance(comodo, Comodo) and isinstance(comodo.nome_comodo, str)):
            super().update(comodo.nome_comodo, comodo)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)
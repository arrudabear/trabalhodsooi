from DAOs.dao import DAO
from Entidades.usuario import Usuario

class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__('usuarios.pkl')
    
    def add(self, usuario: Usuario):
        if ((usuario is not None) and isinstance(usuario, Usuario) and isinstance(usuario.codigo, int)):
            super().add(usuario.codigo, usuario)

    def update(self, usuario: Usuario):
        if ((usuario is not None) and isinstance(usuario, Usuario) and isinstance(usuario.codigo, int)):
            super().update(usuario.codigo, usuario)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
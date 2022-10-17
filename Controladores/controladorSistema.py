from controladorEventos import ControladorEventos
from controladorUsuarios import ControladorUsuario

class ControladorSistema():
    def __init__(self):
        self.__controlador_usuarios = ControladorUsuario(self)
        self.__controlador_eventos = ControladorEventos(self)
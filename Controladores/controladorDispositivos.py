from Controladores.controladorSistema import ControladorSistema


class ControladorDispositivos():
    def __init__(self, controlador_sistema: ControladorSistema):
        if isinstance(controlador_sistema, ControladorSistema):
            self.__controlador_sistema = controlador_sistema
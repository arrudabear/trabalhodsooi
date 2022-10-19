from controladorEventos import ControladorEventos
from controladorUsuarios import ControladorUsuario
from controladorDispositivos import ControladorDispositivos
#from controladorComodos import ControladorComodos
from Limites.telaSistema import TelaSistema

class ControladorSistema():
    def __init__(self):
        self.__controlador_usuarios = ControladorUsuario(self)
        self.__controlador_eventos = ControladorEventos(self)
        self.__controlador_dispositivos = ControladorDispositivos(self)
        #self.__controlador_comodos = ControladorComodos(self)
        self.__tela_sistema = TelaSistema(self)
    
    @property
    def controlador_usuarios(self) -> ControladorUsuario:
        return self.__controlador_usuarios
    
    @property
    def controlador_eventos(self) -> ControladorEventos:
        return self.__controlador_eventos
    
    @property
    def controlador_dispositivos(self) -> ControladorDispositivos:
        return self.__controlador_dispositivos
    
    def inicializa_sistema(self):
        self.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = 

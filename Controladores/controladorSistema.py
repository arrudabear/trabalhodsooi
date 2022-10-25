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
        lista_opcoes = {1: self.entra_usuario, 2: self.cadastra_usuario, 0: self.encerrar_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
    
    def entra_usuario(self):
        usuario_atual = self.__controlador_usuarios.entrar_usuario
        #entrar com o usuario é no sistema eventos ou no sistema usuario??

    def cadastra_usuario(self):
        self.__controlador_usuarios.cadastra_usuario
    

    

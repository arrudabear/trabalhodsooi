from Controladores.controladorEventos import ControladorEventos
from Controladores.controladorUsuarios import ControladorUsuario
from Controladores.controladorDispositivos import ControladorDispositivos
from Controladores.controladorComodos import ControladorComodos
from Limites.telaSistema import TelaSistema

class ControladorSistema():
    def __init__(self):
        self.__controlador_usuarios = ControladorUsuario(self)
        self.__controlador_eventos = ControladorEventos(self)
        self.__controlador_dispositivos = ControladorDispositivos(self)
        self.__controlador_comodos = ControladorComodos(self)
        self.__tela_sistema = TelaSistema()
        self.__usuario_atual = None
    
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
        while True:

            if self.__usuario_atual == None:
                lista_opcoes = {1: self.entrar_usuario, 2: self.cadastra_usuario, 0: self.encerrar_sistema}

                while True:
                    opcao_escolhida = self.__tela_sistema.login
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida()
        
            else:
                lista_opcoes = {1: self.comodos, 2: self.todos_dispositivos, 3: self.relatorios, 4: self.usuarios, 0: self.encerrar_sistema}

                while True:
                    opcao_escolhida = self.__tela_sistema.opcoes_usuario(self.__usuario_atual.nome)
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida()
    
    def entrar_usuario(self):
        self.__usuario_atual = self.__controlador_usuarios.entrar_usuario


    def cadastra_usuario(self):
        self.__controlador_usuarios.cadastra_usuario

    def comodos(self):
        self.__controlador_comodos.lista_comodos
        comodo = self.__controlador_comodos.__tela_comodos.pega_comodo
        self.__controlador_comodos.dispositivos_comodo(comodo)
        #self.dispositivos_comodo(comodo)
    


    
    def todos_dispositivos(self):
        self.__controlador_dispositivos.listar_dispositivos
        pass

    def relatorios(self):
        lista_opcoes = {}
        opcao_escolhida = self.__tela_sistema.relatorios
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        funcao_escolhida()

    def usuarios(self):
        pass


    
    def encerrar_sistema(self):
        exit(0)
    

    

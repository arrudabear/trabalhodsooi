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
    
    @property
    def controlador_comodos(self) -> ControladorComodos:
        return self.__controlador_comodos
    
    @property
    def usuario_atual(self):
        return self.__usuario_atual
    
    def inicializa_sistema(self):
        self.abre_tela()
    
    def abre_tela(self):
        while True:
            if self.__usuario_atual == None:
                lista_opcoes = {1: self.entrar_usuario, 2: self.cadastra_usuario, 0: self.encerrar_sistema}


                opcao_escolhida = self.__tela_sistema.login()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()

            else:
                self.tela_logado()
    
    def tela_logado(self):
        lista_opcoes = {1: self.comodos, 2: self.todos_dispositivos, 3: self.relatorios, 4: self.usuarios, 0: self.voltar}

        while True:
            opcao_escolhida = self.__tela_sistema.opcoes_usuario(self.__usuario_atual.nome)
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def entrar_usuario(self):
        print('entrando')
        self.__usuario_atual = self.__controlador_usuarios.entrar_usuario()

    def cadastra_usuario(self):
        self.__controlador_usuarios.cadastra_usuario() 

    def comodos(self):
        self.__controlador_comodos.abre_tela()
    
    
    def todos_dispositivos(self): 
        self.__controlador_dispositivos.abre_tela()

    def relatorios(self):
        lista_opcoes = {1: self.relatorio_eventos, 2: self.relatorio_usuario, 3: self.relatorio_dispositivo, 0: self.void_func}
        opcao_escolhida = self.__tela_sistema.relatorios()
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        funcao_escolhida()

    def usuarios(self):
        self.__controlador_usuarios.lista_usuarios() 
    
    def relatorio_eventos(self):
        self.__controlador_eventos.lista_eventos()
    
    def relatorio_usuario(self):
        self.__controlador_usuarios.lista_usuarios()
        usuario =  self.__controlador_usuarios.pega_usuario()
        self.__controlador_eventos.evento_usuario(usuario)

    def relatorio_dispositivo(self):
        self.__controlador_dispositivos.lista_dispositivos()
        dados_dispositivo = self.__controlador_dispositivos.escolhe_dispositivo()
        dispositivo = self.__controlador_dispositivos.find_dispositivo(dados_dispositivo["codigo"], dados_dispositivo["nome"])
        self.__controlador_eventos.evento_dispositivo(dispositivo)

    
    def void_func(self):
        pass

    def voltar(self):
        self.__usuario_atual = None 
        self.abre_tela()

    def encerrar_sistema(self):
        exit(0)
    

    

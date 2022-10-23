from controladorSistema import ControladorSistema
from Entidades.usuario import Usuario
from Limites.telaUsuario import TelaUsuario
from random import randint

class ControladorUsuario():
    def __init__(self, controlador_sistema: ControladorSistema):
        self.__cotrolador_sistema = controlador_sistema
        self.__usuarios = []
        self.__lista_codigos = []
        self.__tela = TelaUsuario()
    
    @property
    def usuarios(self):
        return self.__usuarios

    def incluir_usuario(self, usuario: Usuario):
        if isinstance(usuario, Usuario):
            self.__usuarios.append(usuario)
    
    def excluir_usuario(self, usuario: Usuario):
        if isinstance(usuario, Usuario):
            self.__usuarios.remove(usuario)
    
    def lista_usuarios(self):
        return self.__usuarios
    
    def altera_usuario(self, usuario: Usuario, novo_nome, novo_codigo):
        for user in self.__usuarios:
            if user == usuario:
                user.nome = novo_nome
                user.codigo = novo_codigo
    
    def find_usuario(self, codigo: int):
        for usuario in self.__usuarios:
            if usuario.codigo_usuario == codigo:
                return usuario
    
    def cadastra_usuario(self):
        nome_usuario = self.__tela.tela_cadastra_usuario
        while codigo not in self.__lista_codigos:
            codigo = randint(1000,2000)
            if codigo not in self.__lista_codigos:
                self.__lista_codigos.append(codigo)
                codigo_usuario = codigo



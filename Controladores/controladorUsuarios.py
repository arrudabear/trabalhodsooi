from controladorSistema import ControladorSistema
from Entidades.usuario import Usuario

class ControladorUsuario():
    def __init__(self, controlador_sistema: ControladorSistema):
        self.__cotrolador_sistema = controlador_sistema
        self.__usuarios = []
    
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

#from Controladores.controladorSistema import ControladorSistema
from Entidades.usuario import Usuario
from Limites.telaUsuario import TelaUsuario
from random import randint

class ControladorUsuario():
    def __init__(self, controlador_sistema):
        self.__cotrolador_sistema = controlador_sistema
        self.__usuarios = []
        self.__lista_codigos = []
        self.__tela = TelaUsuario()
    
    @property
    def usuarios(self):
        return self.__usuarios

    def find_usuario(self, nome: str, codigo: int): 
        for usuario in self.__usuarios: 
            if (usuario.nome == nome) and (usuario.codigo == codigo):
                return usuario 
        return None 

    def incluir_usuario(self):
        dados_usuario = self.__tela.pega_dados_usuario() 
        usuario = self.find_usuario(dados_usuario["nome"], int(dados_usuario["codigo"]))
        try:
            if usuario == None:
                usuario = Usuario(dados_usuario["nome"], int(dados_usuario["codigo"]))
                self.__usuarios.append(usuario)
                self.__tela.mostrar_mensagem("Usuario Cadastrado")
            else:
                raise KeyError
        except KeyError:
            self.__tela.mostrar_mensagem("Usuario ja cadastrado")

    def excluir_usuario(self, usuario: Usuario):
        if isinstance(usuario, Usuario):
            self.__usuarios.remove(usuario)
    
    def lista_usuarios(self):
        for usuario in self.__usuarios: 
            self.__tela.mostra_usuario({"nome": usuario.nome, "codigo": usuario.codigo})
        return self.__usuarios
    
    def altera_usuario(self, usuario: Usuario, novo_nome, novo_codigo):
        for user in self.__usuarios:
            if user == usuario:
                user.nome = novo_nome
    
    def find_usuario(self, codigo: int):
        for usuario in self.__usuarios:
            if usuario.codigo_usuario == codigo:
                return usuario
#------------------------------------------------------------------------------------------------------------------------------
    def cadastra_usuario(self):
        print('cadastrando 2') #prints pra ver onde ta indo a função
        nome_usuario, codigo_usuario = self.__tela.tela_cadastra_usuario()
        #while codigo not in self.__lista_codigos:
        #    codigo = randint(100,999)
        #    if codigo not in self.__lista_codigos:
        #self.__lista_codigos.append(codigo)
        #codigo_usuario = codigo #consetar!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        usuario = Usuario(nome_usuario, codigo_usuario)
        self.__usuarios.append(usuario)
        print("-"*20)
        print(usuario.codigo, usuario.nome)
    
    def entrar_usuario(self):
        nome_usuario, codigo_usuario = self.__tela.tela_entrar_usuario()
        try:
            for usuario in self.__usuarios:
                print('entrou no for')
                print(usuario.nome, usuario.codigo)
                print(nome_usuario, codigo_usuario)
                if (nome_usuario == usuario.nome):# and (codigo_usuario == usuario.codigo):
                    print('confirmou condição')
                    usuario_atual = usuario
                    return usuario_atual
                else:
                    raise KeyError
        except KeyError:
            self.__tela.mostrar_mensagem("Usuário não Cadastrado")
    



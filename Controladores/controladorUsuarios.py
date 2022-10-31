#from Controladores.controladorSistema import ControladorSistema
from logging import exception
from Entidades.usuario import Usuario
from Limites.telaUsuario import TelaUsuario

class ControladorUsuario():
    def __init__(self, controlador_sistema):
        self.__cotrolador_sistema = controlador_sistema
        self.__usuarios = []
        self.__tela = TelaUsuario()
    
    @property
    def usuarios(self):
        return self.__usuarios

    def find_usuario(self, nome: str, codigo: int): 
        for usuario in self.__usuarios: 
            if (usuario.nome == nome) and (usuario.codigo == codigo):
                return usuario 
        return None 

    def pega_usuario(self):
        dados_usuario = self.__tela.pega_dados_usuario()
        usuario = self.find_usuario(dados_usuario["nome"], int(dados_usuario["codigo"]))
        return usuario
        
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

    def excluir_usuario(self):
        self.lista_usuarios() 
        usuario_escolhido = self.__tela.escolher_usuario() 
        usuario = self.find_usuario(int(usuario_escolhido["codigo"]), usuario_escolhido["nome"])
        try: 
            if (usuario is not None):
                self.__disposistivos.remove(usuario)
                self.__tela.mostrar_mensagem("USUARIO EXCLUIDO")
                self.lista_usuarios() 
            else: 
                raise KeyError
        except KeyError: 
             self.__tela_dispositivos.mostrar_mensagem("USUARIO NÃO EXISTENTE!!")

    def lista_usuarios(self):
        for usuario in self.__usuarios: 
            self.__tela.mostra_usuario({"nome": usuario.nome, "codigo": usuario.codigo})
        return self.__usuarios
    
    def altera_usuario(self):
        self.lista_usuarios() 
        usuario_escolhido = self.__tela.escolher_usuario() 
        usuario = self.find_usuario(int(usuario_escolhido["codigo"]), usuario_escolhido["nome"])
        try: 
            if (usuario is not None): 
                self.__usuarios.remove(usuario) 
                self.incluir_usuario() 
                self.__tela.mostrar_mensagem("USUARIO ALTERADO!!")
                self.lista_usuarios() 
            else: 
                raise KeyError
        except KeyError: 
            self.__tela.mostrar_mensagem("USUARIO NÃO EXISTENTE!!")

#------------------------------------------------------------------------------------------------------------------------------
    def cadastra_usuario(self):
        cadastrando = True
        while cadastrando == True:
            nome_usuario, codigo_usuario = self.__tela.tela_cadastra_usuario()
            try:
                for usuario in self.__usuarios:
                    if usuario.codigo == codigo_usuario:
                        raise KeyError
                usuario = Usuario(nome_usuario, codigo_usuario)
                self.__usuarios.append(usuario)
                self.__tela.mostrar_mensagem("Usuário Cadastrado.")
                print("-"*20)
                print(usuario.codigo, usuario.nome)
                cadastrando = False
                
            except KeyError:
                self.__tela.mostrar_mensagem("Código em uso, por favor digite outro.")
        
    def entrar_usuario(self):
        nome_usuario, codigo_usuario = self.__tela.tela_entrar_usuario()
        try:
            for usuario in self.__usuarios:
                print(usuario.nome, usuario.codigo)
                print(nome_usuario, codigo_usuario)
                if (nome_usuario == usuario.nome) and (codigo_usuario == usuario.codigo):
                    usuario_atual = usuario
                    return usuario_atual
            else:
                raise KeyError 
        except KeyError:
            self.__tela.mostrar_mensagem("Usuário não Cadastrado")
    



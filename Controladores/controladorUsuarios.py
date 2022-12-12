#from Controladores.controladorSistema import ControladorSistema
from logging import exception
from Entidades.usuario import Usuario
from Limites.telaUsuario import TelaUsuario
from DAOs.usuarios_dao import UsuarioDAO

class ControladorUsuario():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__usuario_DAO = UsuarioDAO()
        self.__usuarios = self.__usuario_DAO.get_all()
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
                self.__usuario_DAO.add(usuario)
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
                #self.__disposistivos.remove(usuario)
                self.__usuario_DAO.remove(usuario_escolhido["codigo"])
                self.__tela.mostrar_mensagem("USUARIO EXCLUIDO")
                self.lista_usuarios() 
            else: 
                raise KeyError
        except KeyError: 
             self.__tela_dispositivos.mostrar_mensagem("USUARIO NÃO EXISTENTE!!")

    def lista_usuarios(self):
        self.__usuarios = self.__usuario_DAO.get_all()
        for usuario in self.__usuarios: 
            self.__tela.mostra_usuario({"nome": usuario.nome, "codigo": usuario.codigo})
        return self.__usuarios
    
    def altera_usuario(self):
        self.lista_usuarios() 
        usuario_escolhido = self.__tela.escolher_usuario() 
        usuario = self.find_usuario(int(usuario_escolhido["codigo"]), usuario_escolhido["nome"])
        try: 
            if (usuario is not None): 
                '''self.__usuarios.remove(usuario) 
                self.incluir_usuario() 
                self.lista_usuarios() '''
                dados = self.__tela.pega_dados_usuario()
                user_update = Usuario(dados["nome"], dados["codigo"])
                self.__usuario_DAO.update(user_update)
                self.__tela.mostrar_mensagem("USUARIO ALTERADO!!")
            else: 
                raise KeyError
        except KeyError: 
            self.__tela.mostrar_mensagem("USUARIO NÃO EXISTENTE!!")

#------------------------------------------------------------------------------------------------------------------------------
    def cadastra_usuario(self):
        cadastrando = True
        while cadastrando == True:
            try:
                dados_usuario = self.__tela.tela_cadastra_usuario()
                if dados_usuario == None:
                    break
                else: 
                    codigo = self.__tela.pegar_valor_int(dados_usuario["codigo_usuario"])
                    if dados_usuario["codigo_usuario"] == '' or type(codigo) != int:
                        raise KeyError
                    else: 
                        for usuario in self.__usuarios:
                            if usuario.codigo == int(dados_usuario['codigo_usuario']):
                                raise KeyError
                        usuario = Usuario(dados_usuario['nome_usuario'], int(dados_usuario['codigo_usuario']))
                        self.__usuario_DAO.add(usuario)
                        self.__tela.mostrar_mensagem("Usuário Cadastrado.")
                        print("-"*20)
                        print(usuario.codigo, usuario.nome)
                        cadastrando = False
                    
            except KeyError:
                self.__tela.mostrar_mensagem("Código em uso ou inválido.")
                return None 

    def entrar_usuario(self):
        dados_usuario = self.__tela.tela_entrar_usuario()
        if dados_usuario == None:
            pass 
        else: 
            try:
                for usuario in self.__usuarios:
                    # print(usuario.nome, usuario.codigo)
                    # print(nome_usuario, codigo_usuario)
                    if (dados_usuario['nome_usuario'] == usuario.nome) and (int(dados_usuario['codigo_usuario']) == usuario.codigo):
                        usuario_atual = usuario
                        return usuario_atual
                else:
                    raise KeyError 
            except KeyError:
                self.__tela.mostrar_mensagem("Usuário não Cadastrado")
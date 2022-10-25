#from tela import Tela

class TelaUsuario('''Tela'''):


    def tela_cadastra_usuario(self):
        print("--- Cadastro de Usuario ---")
        nome_usuario = input("Nome do Usuário: ").title()
        return nome_usuario
    
    def tela_entrar_usuario(self):
        print("--- Entrar com Usuário ---")
        nome_usuario = input("Nome do Usuário").title()
        codigo_usuario = int(input("Codigo do Usuário"))
        return nome_usuario, codigo_usuario
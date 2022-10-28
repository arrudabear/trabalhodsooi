from Limites.tela import Tela

class TelaUsuario(Tela):


    def tela_cadastra_usuario(self):
        print("--- Cadastro de Usuario ---")
        nome_usuario = input("Nome do Usuário: ").title()
        return nome_usuario
    
    def tela_entrar_usuario(self):
        print("--- Entrar com Usuário ---")
        nome_usuario = input("Nome do Usuário: ").title()
        codigo_usuario = input("Codigo do Usuário: ")
        try:
            codigo_usuario = int(codigo_usuario)
            if type(codigo_usuario) != int:
                raise ValueError
        except ValueError:
            print("Digite apenas números.")
        return nome_usuario, codigo_usuario
    
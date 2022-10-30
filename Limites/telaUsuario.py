from Limites.tela import Tela

class TelaUsuario(Tela):


    def tela_cadastra_usuario(self):
        print("--- Cadastro de Usuario ---")
        nome_usuario = input("Nome do Usuário: ").title()
        codigo_usuario = self.pegar_valor_int("Codigo do Usuário: ")
        return nome_usuario, codigo_usuario 
    
    def tela_entrar_usuario(self):
        print("--- Entrar com Usuário ---")
        while True:
            nome_usuario = input("Nome do Usuário: ").title()
            codigo_usuario = self.pegar_valor_int("Codigo do Usuário: ")
            return nome_usuario, codigo_usuario
    
    
    def pega_dados_usuario(self): 
        print("------------")
        nome = input("Nome do usuario: ").title()
        codigo = input("Codigo do usuario")

        return {"nome": nome, "codigo": codigo}

    def mostra_usuario(self, dados_usuario):
        print("--------")
        print("Nome", dados_usuario["nome"])
        print("Codigo", dados_usuario["codigo"])
    
    def escolher_usuario(self):
        print("------")
        nome = input("Digite o nome do usuario que deseja acessar: ")
        codigo = input("Digite o codigo do usuario que deseja acessar: ")

        return {"nome": nome, "codigo": codigo}
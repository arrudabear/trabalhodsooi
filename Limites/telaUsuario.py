import PySimpleGUI as sg
from Limites.tela import Tela

class TelaUsuario(Tela):
    def __init__(self): 
        self.__window = None 

    # def tela_cadastra_usuario(self):
    #     print("--- Cadastro de Usuario ---")
    #     nome_usuario = input("Nome do Usuário: ").title()
    #     codigo_usuario = self.pegar_valor_int("Codigo do Usuário: ")
    #     return nome_usuario, codigo_usuario 
    
    def tela_cadastra_usuario(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Cadastro de Usuário ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome_usuario')],
            [sg.Text('Código', size=(15, 1)), sg.InputText('', key='codigo_usuario')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Sistema Casa Inteligente').Layout(layout)

        button, values = self.open()
        nome_usuario = values['nome_usuario']
        codigo_usuario = values['codigo_usuario']
        if button in (None, 'Voltar'):
            self.close() 
        else:
            self.pegar_valor_int(codigo_usuario)
            self.close()
            return {"nome_usuario": nome_usuario, "codigo_usuario": codigo_usuario}
    

    # def tela_entrar_usuario(self):
    #     print("--- Entrar com Usuário ---")
    #     while True:
    #         nome_usuario = input("Nome do Usuário: ").title()
    #         codigo_usuario = self.pegar_valor_int("Codigo do Usuário: ")
    #         return nome_usuario, codigo_usuario

    def tela_entrar_usuario(self):
        while True:
            sg.ChangeLookAndFeel('DarkTeal4')
            layout = [
                [sg.Text('-------- Entrar com Usuário ----------', font=("Helvica", 25))],
                [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome_usuario')],
                [sg.Text('Código', size=(15, 1)), sg.InputText('', key='codigo_usuario')],
                [sg.Button('Confirmar'), sg.Cancel('Voltar')]
            ]
            self.__window = sg.Window('Sistema Casa Inteligente').Layout(layout)

            button, values = self.open()
            nome_usuario = values['nome_usuario']
            codigo_usuario = values['codigo_usuario']
            if button in (None, 'Voltar'):
                self.close()
                break 
            else:
                self.pegar_valor_int(codigo_usuario)
                self.close()
                return {"nome_usuario": nome_usuario, "codigo_usuario": codigo_usuario}
        
    def pega_dados_usuario(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
                [sg.Text('-------- Digite os dados do usuário escolhido ----------', font=("Helvica", 25))],
                [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome_usuario')],
                [sg.Text('Código', size=(15, 1)), sg.InputText('', key='codigo_usuario')],
                [sg.Button('Confirmar'), sg.Cancel('Voltar')]
                ]
        self.__window = sg.Window('Sistema Casa Inteligente').Layout(layout)

        button, values = self.open()
        nome_usuario = values['nome_usuario']
        codigo_usuario = values['codigo_usuario']
        self.close()
        return {"nome": nome_usuario, "codigo": codigo_usuario}
        '''print("------------")
        nome = input("Nome do usuario: ").title()
        codigo = input("Codigo do usuario: ")

        return {"nome": nome, "codigo": codigo}'''

    def mostra_usuario(self, lista_usuarios):
        string_usuarios = ''
        for usuario in lista_usuarios:
            string_usuarios = string_usuarios + "Nome: " + usuario.nome + '\n'
            string_usuarios = string_usuarios + "Código: " + str(usuario.codigo) + '\n'
            string_usuarios = string_usuarios + ('-'*10) + '\n'
        sg.Popup("--- Usuario Cadastrados ---", string_usuarios)
        '''print("--------")
        print("Nome", dados_usuario["nome"])
        print("Codigo", dados_usuario["codigo"])'''
    
    def escolher_usuario(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
                [sg.Text('-------- Digite os dados do usuário escolhido ----------', font=("Helvica", 25))],
                [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome_usuario')],
                [sg.Text('Código', size=(15, 1)), sg.InputText('', key='codigo_usuario')],
                [sg.Button('Confirmar'), sg.Cancel('Voltar')]
                ]
        self.__window = sg.Window('Sistema Casa Inteligente').Layout(layout)

        button, values = self.open()
        nome_usuario = values['nome_usuario']
        codigo_usuario = values['codigo_usuario']
        self.close()
        return {"nome": nome_usuario, "codigo": codigo_usuario}
        '''print("------")
        nome = input("Digite o nome do usuario que deseja acessar: ")
        codigo = input("Digite o codigo do usuario que deseja acessar: ")

        return {"nome": nome, "codigo": codigo}'''

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
import PySimpleGUI as sg 
from Limites.tela import Tela 

class TelaComodos(Tela): 
    def __init__(self):
        self.__window = None 
        self.init_components() 
    # metodo mostrar opcoes em todas as telas; 
    # metodo pegar dados em todas as telas;
    # metodo seleciona em todas as telas
    # metodo mostra em todoas as telas
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

    # def tela_opcoes(self):
    #     print("-------- MENU CÔMODOS ----------")
    #     print("Escolha uma opcao")
    #     print("1 - Incluir Comodo")
    #     print("2 - Excluir Comodo")
    #     print("3 - Listar Comodo")
    #     print("4 - Alterar Comodo")
    #     print("5 - Adicionar Dispositivo Comodo")
    #     print("6 - Mostrar Dispositivos")
    #     print("0 - Voltar")

    #     opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3,4,5,6])
    #     return opcao

    def tela_opcoes(self):
        self.init_components() 
        button, values = self.__window.Read() 
        opcao = 0 
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao


  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    # def pega_dados_comodo(self):
    #   print("-------- DADOS CÔMODO ----------")
    #   nome_comodo = input("Nome do cômodo: ")

    #   return {"nome_comodo": nome_comodo} 
    
    def pega_dados_comodo(self): 
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS CÔMODO ----------', font=("Helvica", 25))],
            [sg.Text('Nome do cômodo:', size=(15, 1)), sg.InputText('', key='nome_comodo')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Sistema Casa Inteligente').Layout(layout)

        button, values = self.open()
        nome_comodo = values['nome_comodo']

        self.close()
        return {"nome_comodo": nome_comodo}

    # def escolhe_comodo(self): 
    #   nome_comodo = input("Digite o nome do cômodo  que deseja acessar: ")
      
    #   return nome_comodo 
    
    def escolhe_comodo(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- ESCOLHER CÔMODO ----------', font=("Helvica", 25))],
            [sg.Text('Nome do cômodo:', size=(15, 1)), sg.InputText('', key='nome_comodo')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Sistema Casa Inteligente').Layout(layout)

        button, values = self.open()
        nome_comodo = values['nome_comodo']

        self.close()
        return nome_comodo
    
    # def mostra_comodo(self, dados_comodo):
    #   print("Nome do cômodo: ", dados_comodo["nome_comodo"])

    def mostra_comodo(self, dados_comodo): 
        string_comodos = ''
        for dado in dados_comodo:
            string_comodos = string_comodos + "Nome Cômodo: " + (dado['nome_comodo']) + '\n\n'
            
        sg.Popup('-------- LISTA DE CÔMODOS ----------', string_comodos)

    def mostrar_mensagem(self, msg):
        sg.Popup(msg)
    #    return super().mostrar_mensagem(msg)
    
    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Menu Comodos', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Incluir Cômodo',"RD1", key='1')],
            [sg.Radio('Excluir Cômodo',"RD1", key='2')],
            [sg.Radio('Listar Cômodo',"RD1", key='3')],
            [sg.Radio('Alterar Cômodo',"RD1", key='4')],
            [sg.Radio('Adicionar Dispositivo Cômodo',"RD1", key='5')],
            [sg.Radio('Mostrar Dispositivos',"RD1", key='6')],
            [sg.Radio('Voltar',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Casa Inteligente').Layout(layout)
    
    def close(self):
        self.__window.Close()
    
    def open(self):
        button, values = self.__window.Read()
        return button, values


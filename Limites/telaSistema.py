import PySimpleGUI as sg 
from Limites.tela import Tela

class TelaSistema(Tela):
    def __init__(self): 
        self.__window = None 

    # def login(self):
    #     print("--- SISTEMA SMART-HOUSE ---")
    #     print("Escolha sua opção:")
    #     print("1 - Entrar com um usuário")
    #     print("2 - Criar usuário novo")
    #     print("0 - Finalizar sistema")
    #     opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2])
    #     return opcao

    def login(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo ao sistema da casa inteligente!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Entrar com um usuário',"RD1", key='1')],
            [sg.Radio('Criar usuário novo',"RD1", key='2')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Sair')]
        ]
        self.__window = sg.Window('Sistema Casa Inteligente').Layout(layout)
        button, values = self.__window.Read() 
        opcao = 0  
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao
    
    # def opcoes_usuario(self, usuario):
    #     print("BEM VINDO ", usuario)
    #     print("Escolha sua opção:")
    #     print("1 - Menu comodos")
    #     print("2 - Menu dispositivos")
    #     print("3 - Gerar Relatório")
    #     print("4 - Usuários da Casa")
    #     print("0 - Voltar")
    #     opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3,4])
    #     return opcao

    def opcoes_usuario(self): 
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('BEM VINDO', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Menu Comodos',"RD1", key='1')],
            [sg.Radio('Menu Dispositivos',"RD1", key='2')],
            [sg.Radio('Gerar Relatório ',"RD1", key='3')],
            [sg.Radio('Usuários Casa',"RD1", key='4')],
            [sg.Radio('Voltar',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Casa Inteligente').Layout(layout)
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
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def relatorios(self):
        print("--- RELATÓRIOS ---")
        print("Escolha sua opção:")
        print("1 - Relatório de Eventos")
        print("2 - Relatório de Eventos por Usuário")
        print("3 - Relatório de Eventos por Dispositivo")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3])
        return opcao

    def relatorios(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("--- RELATÓRIOS ---", font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Relatório de Eventos',"RD1", key='1')],
            [sg.Radio('Relatório de Eventos por Usuário',"RD1", key='2')],
            [sg.Radio('Relatório de Eventor por Dispositivo',"RD1", key='3')],
            [sg.Radio('Voltar',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Casa Inteligente').Layout(layout)
        button, values = self.__window.Read() 
        opcao = 0 
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()
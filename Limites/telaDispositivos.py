import PySimpleGUI as sg 
from Limites.tela import Tela 

class TelaDispositivos(Tela):
    def __init__(self):
        self.__window = None 
        self.init_components()

    #metodo mostrar opcoes em todas as telas; 
    #metodo pegar dados em todas as telas;
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Menu Dispositivos', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Incluir Dispositivo',"RD1", key='1')],
            [sg.Radio('Excluir Dispositivo',"RD1", key='2')],
            [sg.Radio('Listar Dispositivo',"RD1", key='3')],
            [sg.Radio('Alterar Dispositivo',"RD1", key='4')],
            [sg.Radio('Calcular Gasto',"RD1", key='5')],
            [sg.Radio('Controlar Dispositivo',"RD1", key='6')],
            [sg.Radio('Voltar',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Sistema Casa Inteligente').Layout(layout)

    def mostrar_mensagem(self, msg):
        sg.Popup(msg)
    
    def close(self):
        self.__window.Close()
    
    def open(self):
        button, values = self.__window.Read()
        return button, values

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
    
    '''def tela_opcoes(self):
        print("-------- MENU DISPOSITIVOS ----------")
        print("Escolha uma opcao")
        print("1 - Incluir Dispositivo")
        print("2 - Excluir Dispositivo")
        print("3 - Listar Dispositvos")
        print("4 - Alterar Dispositivo")
        print("5 - Calcular Gasto")
        print("6 - Controlar dispositivo")
        print("0 - Voltar")

        opcao = opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3,4,5,6])
        return opcao'''
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

    def pega_dados_dispositivo(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Dados Dispositivo', font=("Helvica",25))],
            [sg.Text('Digite os dados do dispositivo', font=("Helvica",15))],
            [sg.Text('Nome do Dispositivo:', size=(15, 1)), sg.InputText('', key='nome_disp')],
            [sg.Text('Codigo do Dispositivo:', size=(15, 1)), sg.InputText('', key='codigo_disp')],
            [sg.Text('Potência do Dispositivo:', size=(15, 1)), sg.InputText('', key='potencia_disp')],
            [sg.Text('Modelo do Dispositivo:', size=(15, 1)), sg.InputText('', key='modelo_disp')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Sistema Casa Inteligente').Layout(layout)

        button, values = self.open()
        nome_disp = values['nome_disp']
        codigo_disp = values['codig_disp']
        potencia_disp = values['potencia_disp']
        modelo_disp = values['modelo_disp']

        self.close()
        return {"nome": nome_disp, "codigo": codigo_disp, "potencia": potencia_disp, "modelo": modelo_disp}

        '''
        print("-------- DADOS DISPOSITIVO ----------")
        nome = input("Nome do dipositivo: ")
        codigo = self.pegar_valor_int("Codigo: ")
        potencia = self.pegar_valor_float("Potência: ")
        modelo = input("Modelo: ")

        return {"nome": nome,"codigo": codigo, "potencia": potencia, "modelo": modelo}
        '''
    
    def mostra_dispositivo(self, dados_dispositivo):
        msg = "Nome: " + dados_dispositivo["nome"] + "\nCodigo: "+ dados_dispositivo["codigo"]
        sg.Popup("Dados Dispositivo", msg )

        '''
        print("Nome do dispositivo: ", dados_dispositivo["nome"])
        print("Codigo: ", dados_dispositivo["codigo"])
        '''

    def escolhe_dispositivo(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Escolha o Dispositivo', font=("Helvica",25))],
            [sg.Text('Digite os dados do dispositivo que deseja acessar', font=("Helvica",15))],
            [sg.Text('Nome do Dispositivo:', size=(15, 1)), sg.InputText('', key='nome_disp')],
            [sg.Text('Codigo do Dispositivo:', size=(15, 1)), sg.InputText('', key='codigo_disp')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Sistema Casa Inteligente').Layout(layout)

        button, values = self.open()
        nome_disp = values['nome_disp']
        codigo_disp = values['codig_disp']

        self.close()
        return {"nome": nome_disp, "codigo": codigo_disp}

        '''
        print("--- Escolha o Dispositivo ---")
        nome = input("Digite o nome do dispositivo que deseja acessar: ")
        codigo = self.pegar_valor_int("Digite o código do dispositivo que deseja acessar: ")

        return {"nome": nome, "codigo": codigo}
        ''' 
#------------------------------------------------------------------------------------------------------------------    
    def controle_arcondicionado(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Controle Ar Condicionado', font=("Helvica",25))],
            [sg.Text('Escolha a ação', font=("Helvica",15))],
            [sg.Radio('Ligar/Desligar',"RD1", key='1')],
            [sg.Radio('Temperatura',"RD1", key='2')],
            [sg.Radio('Timer',"RD1", key='3')],
            [sg.Radio('Informações do Dispositivo',"RD1", key='4')],
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
        '''
        print("--- Controle Ar Condicionado ---")
        print("1 - Ligar/Desligar")
        print("2 - Temperatura")
        print("3 - Timer")
        print("4 - Informações do Dispositivo")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3,4])
        return opcao
        '''
    
    def controle_geladeira(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Controle Geladeira', font=("Helvica",25))],
            [sg.Text('Escolha a ação', font=("Helvica",15))],
            [sg.Radio('Ligar/Desligar',"RD1", key='1')],
            [sg.Radio('Temperatura',"RD1", key='2')],
            [sg.Radio('Timer',"RD1", key='3')],
            [sg.Radio('Informações do Dispositivo',"RD1", key='4')],
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

        '''
        print("--- Controle Geladeira ---")
        print("1 - Ligar/Desligar")
        print("2 - Temperatura")
        print("3 - Timer")
        print("4 - Informações do Dispositivo")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3,4])
        return opcao
        '''

    def controle_forno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Controle Forno', font=("Helvica",25))],
            [sg.Text('Escolha a ação', font=("Helvica",15))],
            [sg.Radio('Ligar/Desligar',"RD1", key='1')],
            [sg.Radio('Temperatura',"RD1", key='2')],
            [sg.Radio('Timer',"RD1", key='3')],
            [sg.Radio('Informações do Dispositivo',"RD1", key='4')],
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
        '''
        print("--- Controle Forno ---")
        print("1 - Ligar/Desligar")
        print("2 - Temperatura")
        print("3 - Timer")
        print("4 - Informações do Dispositivo")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3,4])
        return opcao
        '''

    def controle_tv(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Controle TV', font=("Helvica",25))],
            [sg.Text('Escolha a ação', font=("Helvica",15))],
            [sg.Radio('Ligar/Desligar',"RD1", key='1')],
            [sg.Radio('Canal',"RD1", key='2')],
            [sg.Radio('Volume',"RD1", key='3')],
            [sg.Radio('Timer',"RD1", key='4')],
            [sg.Radio('Informações do Dispositivo',"RD1", key='5')],
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
        if values['5']:
            opcao = 5
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao
        '''
        print("--- Contorle TV ---")
        print("1 - Ligar/Desligar")
        print("2 - Canal")
        print("3 - Volume")
        print("4 - Timer")
        print("5 - Informações do Dispositivo")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3,4,5])
        return opcao
        '''

    def controle_som(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Controle Som', font=("Helvica",25))],
            [sg.Text('Escolha a ação', font=("Helvica",15))],
            [sg.Radio('Ligar/Desligar',"RD1", key='1')],
            [sg.Radio('Trocar Musica',"RD1", key='2')],
            [sg.Radio('Volume',"RD1", key='3')],
            [sg.Radio('Timer',"RD1", key='4')],
            [sg.Radio('Informações do Dispositivo',"RD1", key='5')],
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
        if values['5']:
            opcao = 5
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao
        '''
        print("--- Controle Som ---")
        print("1 - Ligar/Desligar")
        print("2 - Trocar Música")
        print("3 - Volume")
        print("4 - Timer")
        print("5 - Informações do Dispositivo")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3,4,5])
        return opcao
        '''

    def controle_lavadoras(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Controle Lavadora de Roupas', font=("Helvica",25))],
            [sg.Text('Escolha a ação', font=("Helvica",15))],
            [sg.Radio('Ligar/Desligar',"RD1", key='1')],
            [sg.Radio('Modo',"RD1", key='2')],
            [sg.Radio('Timer',"RD1", key='3')],
            [sg.Radio('Informações do Dispositivo',"RD1", key='4')],
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
        '''
        print("--- Controle Lavadora de Roupa ---")
        print("1 - Ligar/Desligar")
        print("2 - Modo")
        print("3 - Timer")
        print("4 - Informações do Dispositivo")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3,4])
        return opcao
        '''

    def controle_lavaloucas(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Controle Lavadora de Louças', font=("Helvica",25))],
            [sg.Text('Escolha a ação', font=("Helvica",15))],
            [sg.Radio('Ligar/Desligar',"RD1", key='1')],
            [sg.Radio('Modo',"RD1", key='2')],
            [sg.Radio('Timer',"RD1", key='3')],
            [sg.Radio('Informações do Dispositivo',"RD1", key='4')],
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
        '''
        print("--- Controle Lava Louças ---")
        print("1 - Ligar/Desligar")
        print("2 - Modo")
        print("3 - Timer")
        print("4 - Informações do Dispositivo")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3,4])
        return opcao
        '''
    
    def controle_cafeteira(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Controle Cafeteira', font=("Helvica",25))],
            [sg.Text('Escolha a ação', font=("Helvica",15))],
            [sg.Radio('Ligar/Desligar',"RD1", key='1')],
            [sg.Radio('Timer',"RD1", key='2')],
            [sg.Radio('Informações do Dispositivo',"RD1", key='3')],
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
        '''
        print("--- Controle Cafeteira ---")
        print("1 - Ligar/Desligar")
        print("2 - Timer")
        print("3 - Informações do Dispositivo")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3])
        return opcao
        '''

    def controle_cortina(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Controle Cortina', font=("Helvica",25))],
            [sg.Text('Escolha a ação', font=("Helvica",15))],
            [sg.Radio('Ligar/Desligar',"RD1", key='1')],
            [sg.Radio('Timer',"RD1", key='2')],
            [sg.Radio('Informações do Dispositivo',"RD1", key='3')],
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
        '''
        print("--- Controle Cortina ---")
        print("1 - Abrir/Fechar")
        print("2 - Timer")
        print("3 - Informações do Dispositivo")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3])
        return opcao
        '''

    def controle_luz(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Controle Ponto de Luz', font=("Helvica",25))],
            [sg.Text('Escolha a ação', font=("Helvica",15))],
            [sg.Radio('Ligar/Desligar',"RD1", key='1')],
            [sg.Radio('Timer',"RD1", key='2')],
            [sg.Radio('Informações do Dispositivo',"RD1", key='3')],
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
        '''
        print("--- Controle Luz ---")
        print("1 - Ligar/Desligar")
        print("2 - Timer")
        print("3 - Informações do Dispositivo")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3])
        return opcao
        '''

    def escolher_tipo_dispositivo(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Menu Dispositivos', font=("Helvica",25))],
            [sg.Text('Escolha o tipo do dispositivo', font=("Helvica",15))],
            [sg.Radio('Ar Condicionado',"RD1", key='1')],
            [sg.Radio('Cafeteira',"RD1", key='2')],
            [sg.Radio('Cortina',"RD1", key='3')],
            [sg.Radio('Forno',"RD1", key='4')],
            [sg.Radio('Geladeira',"RD1", key='5')],
            [sg.Radio('Lavadora de Roupas',"RD1", key='6')],
            [sg.Radio('Ponto de Luz',"RD1", key='7')],
            [sg.Radio('Som',"RD1", key='8')],
            [sg.Radio('TV',"RD1", key='9')],
            [sg.Radio('Lava Louças',"RD1", key='10')],
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
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['7']:
            opcao = 7
        if values['8']:
            opcao = 8
        if values['9']:
            opcao = 9
        if values['10']:
            opcao = 10
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

        '''
        print("1 - Ar Condicionado")
        print("2 - Cafeteira")
        print("3 - Cortina")
        print("4 - Forno")
        print("5 - Geladeira")
        print("6 - Lavadoura de Roupa")
        print("7 - Ponto de luz")
        print("8 - Som")
        print("9 - TV")
        print("10 - Lava louças")
        print("0 - Voltar")
    
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3,4,5,6,7,8,9,10])
        return opcao 
        '''



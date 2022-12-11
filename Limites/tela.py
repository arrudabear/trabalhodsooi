import PySimpleGUI as sg 
from abc import ABC

class Tela(ABC):
    def __init__(self):
        self.__window = None 

    def mostrar_mensagem(self, msg):
        sg.Popup(msg)
    
    def close(self):
        self.__window.Close()
    
    def open(self):
        button, values = self.__window.Read()
        return button, values

    def le_num_inteiro(self, mensagem = "", ints_validos = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError
                return valor_int
            except ValueError:
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)

    
    def mostrar_mensagem(self, msg):
        sg.Popup(msg)
        # print(msg)

    def seleciona_opcao(self, msg, opcoes):
      opcao = self.le_num_inteiro(msg, opcoes)
      return opcao
    
    # def seleciona_opcao(self):
    #     sg.ChangeLookAndFeel('DarkTeal4')
    #     layout = [
    #         [sg.Text('Menu Comodos', font=("Helvica",25))],
    #         [sg.Text('Escolha sua opção', font=("Helvica",15))],
    #         [sg.Radio('Sim',"RD1", key='1')],]

    #     self.__window = sg.Window('Sistema Casa Inteligente').Layout(layout)
    #     self.init_components() 
    #     button, values = self.__window.Read() 
    #     opcao = 0 
    #     if values['1']:
    #         opcao = 1
    #     if values['2']:
    #         opcao = 2
    #     self.close()
    #     return opcao

    def pegar_valor_int(self, mensagem):
        valor_lido = mensagem
        try:
            valor_int = int(valor_lido)
            if type(valor_int) == int:
                return valor_int
            else:   
                raise ValueError
        except ValueError:
            self.mostrar_mensagem("Digite apenas números.")

    def pegar_valor_float(self, mensagem):
        valor_lido = mensagem  
        try:
            valor_float = float(valor_lido)
            if type(valor_float) == float:
                return valor_float
            else:   
                raise ValueError
        except ValueError:
            self.mostrar_mensagem("Digite apenas números.")


    def tela_int(self, mensagem):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text(mensagem, font=("Helvica",15))],
            [sg.Text('Digite um valor inteiro:', size=(15, 1)), sg.InputText('', key='valor_int')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Sistema Casa Inteligente').Layout(layout)

        button, values = self.open()
        valor = values['valor_int']
        try:
            valor_int = int(valor)
            if isinstance(valor_int, int):
                self.close()
                return valor_int
            else:
                raise ValueError
        except ValueError:
            self.mostrar_mensagem("Digite apenas números inteiros")
    


    
   

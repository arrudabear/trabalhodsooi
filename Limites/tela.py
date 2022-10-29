from abc import ABC

class Tela():
    
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
        print(msg)

    def seleciona_opcao(self, msg, opcoes):
      opcao = self.le_num_inteiro(msg, opcoes)
      return opcao
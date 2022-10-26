from tela import Tela 

class TelaDispositivos(Tela): 
    #metodo mostrar opcoes em todas as telas; 
    #metodo pegar dados em todas as telas;
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- DISPOSITIVOS ----------")
        print("Escolha uma opcao")
        print("1 - Incluir Dispositivo")
        print("2 - Alterar Dispositivo")
        print("3 - Listar Dispositvos")
        print("4 - Excluir Dispositivo")
        print("5 - Calcular Gasto")
        print("0 - Lista dispositivos")

        opcao = int(input("Escolha a opcao: "))
        return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_dispositivo(self):
        print("-------- DADOS DISPOSITIVO ----------")
        codigo_dispositivo = input("Código dispositivo: ")
        potencia = input("Potência: ")
        modelo = input("Modelo: ")

        return {"codigo_dispositivo": codigo_dispositivo, "potencia": potencia, "modelo": modelo}
    
    def mostra_dispositivo(self, nome, codigo, modelo):
        print("Nome do Dispositivo: ", nome)
        print("Código: ", codigo)
        print("Modelo: ", modelo)

    def escolhe_dispositivo(self):
        print("--- Escolha o Dispositivo ---")
        codigo = input("Digite o código do dispositivo que deseja acessar: ")
        try:
            codigo = int(codigo)
            return codigo
        except:
            raise execption # fazer aqui tratamento da exceção da entrada nao ser int
    
    def controle_temp(self, nome, codigo):
        print("CONTROLE: ", nome)
        print("Código: ", codigo)
        print("1 - Ligar/Desligar")
        print("2 - Temperatura")
        print("3 - Timer")
        print("4 - Informações do Dispositivo")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3,4])
        return opcao
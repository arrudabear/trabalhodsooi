from Limites.tela import Tela 

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
        print("0 - Voltar")

        opcao = opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3,4,5])
        return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_dispositivo(self):
        print("-------- DADOS DISPOSITIVO ----------")
        nome = input("Nome do dipositivo: ")
        potencia = input("Potência: ")
        codigo = input("Código dispositivo: ")
        modelo = input("Modelo: ")

        return {"nome": nome, "potencia": potencia, "codigo": codigo, "modelo": modelo}
    
    def mostra_dispositivo(self, dados_dispositivo):
        print("Nome do dispositivo: ", dados_dispositivo["nome"])
        print("Código: ", dados_dispositivo["codigo"])
        print("Modelo: ", dados_dispositivo["modelo"])

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
    
    def escolher_tipo_dispositivo(self): 
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



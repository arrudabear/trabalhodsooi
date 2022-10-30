from Limites.tela import Tela 

class TelaDispositivos(Tela): 
    #metodo mostrar opcoes em todas as telas; 
    #metodo pegar dados em todas as telas;
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
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
        return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_dispositivo(self):
        print("-------- DADOS DISPOSITIVO ----------")
        nome = input("Nome do dipositivo: ")
        codigo = input("Codigo: ")
        potencia = input("Potência: ")
        modelo = input("Modelo: ")

        return {"nome": nome,"codigo": codigo, "potencia": potencia, "modelo": modelo}
    
    def mostra_dispositivo(self, dados_dispositivo):
        print("Nome do dispositivo: ", dados_dispositivo["nome"])
        print("Codigo: ", dados_dispositivo["codigo"])

    def escolhe_dispositivo(self):
        print("--- Escolha o Dispositivo ---")
        nome = input("Digite o nome do dispositivo que deseja acessar: ")
        codigo = input("Digite o código do dispositivo que deseja acessar: ")

        return {"nome": nome, "codigo": codigo}

#------------------------------------------------------------------------------------------------------------------    
    def controle_arcondicionado(self):
        pass
    
    def controle_geladeira(self):
        print('geladeira')

    def controle_forno(self):
        #print("CONTROLE: ", dados_dispositivo["nome"])
        #print("Código: ", dados_dispositivo["codigo"])
        print("1 - Ligar/Desligar")
        print("2 - Temperatura")
        print("3 - Timer")
        print("4 - Informações do Dispositivo")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3,4,8])
        return opcao
    
    def controle_tv(self):
        print('TV')

    def controle_som(self):
        print('som')

    def controle_lavadoras(self):
        print('Controle lavadora')
    
    def controle_lavaloucas(self):
        print('lava louças')
    
    def controle_cafeteira(self):
        pass

    def controle_cortina(self):
        pass

    def controle_luz(self):
        print('controle luz')
    
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



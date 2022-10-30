from Limites.tela import Tela 

class TelaComodos(Tela): 
    # metodo mostrar opcoes em todas as telas; 
    # metodo pegar dados em todas as telas;
    # metodo seleciona em todas as telas
    # metodo mostra em todoas as telas
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- MENU CÔMODOS ----------")
        print("Escolha uma opcao")
        print("1 - Incluir Comodo")
        print("2 - Excluir Comodo")
        print("3 - Listar Comodo")
        print("4 - Alterar Comodo")
        print("5 - Calcular Gasto no Comodo")
        print("6 - Mostrar Dispositivos")
        print("0 - Voltar")

        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3,4,5,6])
        return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_comodo(self):
      print("-------- DADOS CÔMODO ----------")
      nome_comodo = input("Nome do cômodo: ")

      return {"nome_comodo": nome_comodo} 

    def escolhe_comodo(self): 
      nome_comodo = input("Digite o nome do cômodo  que deseja acessar: ")
      return nome_comodo 
    
    def mostra_comodo(self, dados_comodo):
      print("Nome do cômodo: ", dados_comodo["nome_comodo"])
    



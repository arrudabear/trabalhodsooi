from calendar import c
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

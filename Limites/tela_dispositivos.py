class TelaDispositivos(): 
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
      estado = input("Estado: ")
      potencia = input("Potência: ")
      tempo_ligado = input("Tempo ligado: ")
      timer_ligar = input("Timer para ligar: ")
      timer_desligar = input("Timer para desligar: ")
      codigo_dispositivo = input("Código dispositivo: ")
      modelo = input("Modelo: ")

      return {"estado": estado, "potencia": potencia, "tempo_ligado": tempo_ligado, 
              "timer_ligar": timer_ligar, "timer_desligar": timer_desligar,
              "codigo_dispositivo": codigo_dispositivo, "modelo": modelo}

    def mensagem(self, msg): 
      print(msg) 

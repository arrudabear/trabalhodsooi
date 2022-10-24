from tela import Tela

class TelaSistema(Tela):
        
    def login(self):
        print("--- SISTEMA SMART-HOUSE ---")
        print("Escolha sua opção:")
        print("1 - Entrar com um usuário")
        print("2 - Criar usuário novo")
        print("0 - Finalizar sistema")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2])
        return opcao
    
    def opcoes_usuario(self, usuario):
        print("BEM VINDO ", usuario)
        print("Escolha sua opção:")
        print("1 - Controlar Dispositivos")
        print("2 - Controlar Cômodos")
        print("3 - Gerar Relatório")
        print("0 - Finalizar sistema")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3])
        return opcao

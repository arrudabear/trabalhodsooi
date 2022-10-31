from Limites.tela import Tela

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
        print("1 - Menu comodos")
        print("2 - Menu dispositivos")
        print("3 - Gerar Relatório")
        print("4 - Usuários da Casa")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3,4])
        return opcao

    def relatorios(self):
        print("--- RELATÓRIOS ---")
        print("Escolha sua opção:")
        print("1 - Relatório de Eventos")
        print("2 - Relatório de Eventos por Usuário")
        print("3 - Relatório de Eventos por Dispositivo")
        print("0 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0,1,2,3])
        return opcao
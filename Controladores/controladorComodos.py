
#from Controladores.controladorSistema import ControladorSistema
from Limites.telaComodos import TelaComodos
from Entidades.comodo import Comodo

class ControladorComodos(): 
    #colocar contolador sistema no UML 
    def __init__(self, controlador_sistema):
        self.__comodos = [] 
        self.__controlador_sistema = controlador_sistema
        self.__tela_comodos = TelaComodos() 
    
    def find_comodo(self, nome_comodo: str): 
        for comodo in self.__comodos:
            if (comodo.nome_comodo == nome_comodo): 
                return comodo
        return None 

    def incluir_comodo(self): 
        print('incluindo comodo')
        dados_comodo = self.__tela_comodos.pega_dados_comodo() 
        comodo = self.find_comodo(dados_comodo["nome_comodo"])
        try:
            if comodo == None:
                comodo = Comodo(dados_comodo["nome_comodo"])
                self.__comodos.append(comodo)
                self.__tela_comodos.mostrar_mensagem("Cômodo adicionado na lista!")
            else:
                raise KeyError
        except KeyError:
            self.__tela_comodos.mostrar_mensagem("Cômodo já existente na lista!") 
    
    def lista_comodos(self):
        if self.__comodos == []:
            self.__tela_comodos.mostrar_mensagem("Ainda não há cômodos cadastrados")
            self.__tela_comodos.mostrar_mensagem("Deseja criar um novo cômodo? [SIM: 1 / NÃO: 0]")
            opcao = self.__tela_comodos.seleciona_opcao("Escolha a opção: ", [0,1])
            if opcao == 1:
                self.incluir_comodo()
                self.lista_comodos()
            else:
                self.abre_tela() 
            
        else:
            self.__tela_comodos.mostrar_mensagem("-------- CÔMODOS CADASTRADOS ----------")
            for comodo in self.__comodos: 
                self.__tela_comodos.mostra_comodo({"nome_comodo": comodo.nome_comodo})
                self.__tela_comodos.mostrar_mensagem("-----------------------------------")


    def excluir_comodo(self): 
        self.lista_comodos()
        nome_comodo = self.__tela_comodos.escolhe_comodo() 
        comodo = self.find_comodo(nome_comodo) 
        try: 
            if(comodo is not None):
                self.__comodos.remove(comodo)
                self.__tela_comodos.mostrar_mensagem("CÔMODO EXCLUIDO!!")
                self.lista_comodos() 
            else:
                raise KeyError
        except KeyError:
            self.__tela_comodos.mostrar_mensagem("CÔMODO NÃO EXISTENTE!!")
        

    def altera_comodo(self): 
        self.lista_comodos()
        nome_comodo = self.__tela_comodos.escolhe_comodo()
        comodo = self.find_comodo(nome_comodo) 
        try:
            if (comodo is not None): 
                novo_nome_comodo = self.__tela_comodos.pega_dados_comodo()
                novo_comodo = Comodo(novo_nome_comodo["nome_comodo"])
                self.__comodos.remove(comodo)
                self.__comodos.append(novo_comodo)
                self.__tela_comodos.mostrar_mensagem("CÔMODO ALTERADO!!")
                self.lista_comodos()
            else:
                raise KeyError
        except KeyError:
            self.__tela_comodos.mostrar_mensagem("CÔMODO NÃO EXISTENTE!!")

    def abre_tela(self):
        opcoes = {1: self.incluir_comodo, 2: self.excluir_comodo, 3: self.lista_comodos, 4: self.altera_comodo, 5: self.pegar_comodo, 6: self.dispositivos_comodo, 0: self.voltar}

        continua = True
        while continua: 
            opcoes[self.__tela_comodos.tela_opcoes()]() 
    
    def dispositivos_comodo(self, comodo): 
        if comodo.dispositivos == []:
            self.__tela_comodos.mostrar_mensagem("Ainda não há dispositivos cadastrados neste comodo.")
            self.__tela_comodos.mostrar_mensagem("Deseja adicionar um novo dispositivos à esse comodo? [SIM: 1/NÃO: 0]")
            opcao = self.__tela_comodos.seleciona_opcao("Escolha sua opção: ", [0,1])
            if opcao == 1:
                self.adicionar_dispositivo_comodo(comodo)
            else:
                self.lista_comodos()
        else:
            #self.__tela_comodos.mostrar_mensagem("Dispositivos no Comodo: ", comodo.nome_comodo)
            for dispositivo in comodo.dispositivos:
                self.__controlador_sistema.__controlador_dispositivos.mostra_dispositivo(dispositivo)
            #disp = self.__controlador_sistema.__controlador_dispositivos.pega_dispositivo
            #self.__controlador_sistema.__controlador_dispositivos.controla_dispositivo(disp)

    def adicionar_dispositivo_comodo(self, comodo):  
        self.__controlador_sistema.controlador_dispositivos.lista_dispositivos() 
        disp = self.__controlador_sistema.controlador_dispositivos.escolhe_dispositivo()
        disp = self.__controlador_sistema.controlador_dispositivos.find_dispositivo(disp["codigo"], disp["nome"])
        comodo.adicionar_dispositivo(disp)
        self.dispositivos_comodo(comodo) 
        
    def pegar_comodo(self): 
        comodo = self.__tela_comodos.escolhe_comodo() 
        comodo = Comodo(comodo)
        self.adicionar_dispositivo_comodo(comodo)


    def voltar(self): 
        self.__controlador_sistema.abre_tela() 
    #def voltar(self):
        #self.__controlador_sistema.abre_tela()

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
        self.__tela_comodos.mostrar_mensagem("-------- CÔMODOS CADASTRADOS ----------")
        for comodo in self.__comodos: 
            self.__tela_comodos.mostra_comodo({"nome_comodo": comodo.nome_comodo})

    def excluir_comodo(self): 
        self.lista_comodos()
        nome_comodo = self.__tela_comodos.pega_comodo()
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
        nome_comodo = self.__tela_comodos.pega_comodo()
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
        opcoes = {1: self.incluir_comodo, 2: self.excluir_comodo, 3: self.lista_comodos, 4: self.altera_comodo}

        continua = True
        while continua: 
            opcoes[self.__tela_comodos.tela_opcoes()]() 
    
    def dispositivos_comodo(self, comodo: Comodo):
        self.__tela_comodos.mostrar_mensagem("Dispositivos no Comodo: ", comodo.nome_comodo)
        for dispositivo in comodo.dispositivos:
            self.__controlador_sistema.__controlador_dispositivos.mostra_dispositivo(dispositivo)
        disp = self.__controlador_sistema.__controlador_dispositivos.pega_dispositivo
        self.__controlador_sistema.__controlador_dispositivos.controla_dispositivo(disp)


    

    #def adicionar_dispositivo_comodo(self): 
        #self.__controlador_sistema.controlador_


    #def voltar(self):
        #self.__controlador_sistema.abre_tela()

#from Controladores.controladorSistema import ControladorSistema
from Limites.telaComodos import TelaComodos
from Entidades.comodo import Comodo
from DAOs.comodos_dao import ComodoDAO

class ControladorComodos(): 
    #colocar contolador sistema no UML 
    def __init__(self, controlador_sistema):
        self.__comodo_DAO = ComodoDAO() 
        self.__comodos = self.__comodo_DAO.get_all() 
        self.__controlador_sistema = controlador_sistema
        self.__tela_comodos = TelaComodos()  
    
    def find_comodo(self, nome_comodo: str): 
        for comodo in self.__comodos:
            if (comodo.nome_comodo == nome_comodo): 
                return comodo
        return None 

    def incluir_comodo(self): 
        dados_comodo = self.__tela_comodos.pega_dados_comodo() 
        if dados_comodo == None: 
            pass
        else:
            comodo = self.find_comodo(dados_comodo["nome_comodo"])
            try:
                if comodo == None:
                    comodo = Comodo(dados_comodo["nome_comodo"])
                    self.__comodo_DAO.add(comodo)
                    self.__tela_comodos.mostrar_mensagem("Cômodo adicionado na lista!")
                else:
                    raise KeyError
            except KeyError:
                self.__tela_comodos.mostrar_mensagem("Cômodo já existente na lista!") 
    
    def lista_comodos(self):
        self.__comodos = self.__comodo_DAO.get_all()
        dados_comodo = [] 
        # self.__tela_comodos.mostrar_mensagem("-------- CÔMODOS CADASTRADOS ----------")
        for comodo in self.__comodos: 
            dados_comodo.append({'nome_comodo': comodo.nome_comodo})
            # self.__tela_comodos.mostra_comodo({comodo.nome_comodo})
            # self.__tela_comodos.mostrar_mensagem("-----------------------------------")
        self.__tela_comodos.mostra_comodo(dados_comodo) 

    def excluir_comodo(self): 
        self.lista_comodos()
        nome_comodo = self.__tela_comodos.escolhe_comodo()
        if nome_comodo == None: 
            pass
        else: 
            comodo = self.find_comodo(nome_comodo['nome_comodo']) 
            try: 
                if(comodo is not None):
                    self.__comodo_DAO.remove(nome_comodo['nome_comodo'])
                    self.__tela_comodos.mostrar_mensagem("CÔMODO EXCLUIDO!!")
                    self.lista_comodos() 
                else:
                    raise KeyError
            except KeyError:
                self.__tela_comodos.mostrar_mensagem("CÔMODO NÃO EXISTENTE!!")
        

    def altera_comodo(self): 
        self.lista_comodos()
        nome_comodo = self.__tela_comodos.escolhe_comodo()
        if nome_comodo == None: 
            pass
        else: 
            comodo = self.find_comodo(nome_comodo['nome_comodo']) 
            try:
                if (comodo is not None): 
                    novo_nome_comodo = self.__tela_comodos.pega_dados_comodo()
                    novo_comodo = Comodo(novo_nome_comodo["nome_comodo"])
                    self.__comodo_DAO.remove(nome_comodo['nome_comodo'])
                    self.__comodo_DAO.add(novo_comodo)
                    self.__tela_comodos.mostrar_mensagem("CÔMODO ALTERADO!!")
                    self.lista_comodos()
                else:
                    raise KeyError
            except KeyError:
                self.__tela_comodos.mostrar_mensagem("CÔMODO NÃO EXISTENTE!!")

    def abre_tela(self):
        opcoes = {1: self.incluir_comodo, 2: self.excluir_comodo, 3: self.lista_comodos, 4: self.altera_comodo, 5: self.adicionar_dispositivo_comodo, 6: self.dispositivos_comodo, 0: self.voltar}

        continua = True
        while continua: 
            opcoes[self.__tela_comodos.tela_opcoes()]() 
    
    def dispositivos_comodo(self): 
        self.lista_comodos()
        nome_comodo = self.__tela_comodos.escolhe_comodo()
        if nome_comodo == None:
            pass 
        else: 
            dados_dispositivo = []
            comodo = self.find_comodo(nome_comodo['nome_comodo']) 
                #self.__tela_comodos.mostrar_mensagem("Dispositivos no Comodo: ", comodo.nome_comodo)
            for dispositivo in comodo.dispositivos:
                dados_dispositivo.append({'nome_disp': dispositivo.nome, 'codigo_disp': dispositivo.codigo})
                #disp = self.__controlador_sistema.__controlador_dispositivos.pega_dispositivo
                #self.__controlador_sistema.__controlador_dispositivos.controla_dispositivo(disp)
            self.__controlador_sistema.controlador_dispositivos.mostra_dispositivo(dados_dispositivo)

    def adicionar_dispositivo_comodo(self):
        self.lista_comodos()
        nome_comodo = self.__tela_comodos.escolhe_comodo()
        if nome_comodo == None:
            pass
        else: 
            comodo = self.find_comodo(nome_comodo['nome_comodo'])
            self.__controlador_sistema.controlador_dispositivos.lista_dispositivos() 
            disp = self.__controlador_sistema.controlador_dispositivos.escolhe_dispositivo()
            disp = self.__controlador_sistema.controlador_dispositivos.find_dispositivo(int(disp["codigo"]), disp["nome"])
            comodo.adicionar_dispositivo(disp)
            self.__tela_comodos.mostrar_mensagem("Dispositivo Adicionado no cômodo!!")
        
    # def pegar_comodo(self): 
    #     comodo = self.__tela_comodos.escolhe_comodo() 
    #     comodo = Comodo(comodo)
    #     self.adicionar_dispositivo_comodo(comodo)

    def voltar(self): 
        self.__controlador_sistema.abre_tela() 
    #def voltar(self):
        #self.__controlador_sistema.abre_tela()
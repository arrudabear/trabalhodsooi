
from Limites.telaDispositivos import TelaDispositivos
from Entidades.dispositivo import Dispositivo

class ControladorDispositivos(): 
    #colocar contolador sistema no UML 
    def __init__(self):
        self.__dispositivos = [] 
        #self.__controlador_sistema = controlador_sistema
        self.__tela_dispositivos = TelaDispositivos() 
    
    def find_dispositivo(self, codigo_dispositivo: int, modelo: str): 
        for dispositivo in self.__dispositivos:
            if (dispositivo.codigo_dispositivo == codigo_dispositivo) and (dispositivo.modelo == modelo): 
                return dispositivo
        return None 

    def incluir_dispositivo(self): 
        dados_dispositivo = self.__tela_dispositivos.pega_dados_dispositivo()
        dispositivo = self.find_dispositivo(dados_dispositivo["codigo_dispositivo"], dados_dispositivo["modelo"])
        try:
            if dispositivo == None:
                dispositivo = Dispositivo(dados_dispositivo["codigo_dispositivo"], dados_dispositivo["potencia"],
                                          dados_dispositivo["modelo"])

                self.__dispositivos.append(dispositivo)
                self.__tela_dispositivos.mostrar_mensagem("Dispositivo adicionado na lista!")
            else:
                raise KeyError
        except KeyError:
            self.__tela_dispositivos.mostrar_mensagem("Dispositivo já existente na lista!") 
    
    def abre_tela(self):
        opcoes = {1: self.incluir_dispositivo}

        continua = True
        while continua: 
            opcoes[self.__tela_dispositivos.tela_opcoes()]()
    
    def mostra_dispositivo(self, dispositivo: Dispositivo):
        self.__tela_dispositivos(dispositivo.nome, dispositivo.codigo_dispositivo, dispositivo.modelo)
    
    def pega_dispositivo(self):
        dispositivo = self.__tela_dispositivos.escolhe_dispositivo
        self.controla_dispositivo(dispositivo)
    
    def controla_dispositivo(self, dispositivo: Dispositivo):
        self.__tela_dispositivos.mostrar_mensagem("--- Controle do Dispositivo ---")
        self.__tela_dispositivos.mostra_dispositivo(dispositivo.nome, dispositivo.codigo_dispositivo, dispositivo.modelo)
        self.__tela_dispositivos.controle
    
    '''def dipositivos_comodo(self, comodo):
        for dispositivo in self.__dipositivos:
            if dispositivo.comodo == comodo:'''




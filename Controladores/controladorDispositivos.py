
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



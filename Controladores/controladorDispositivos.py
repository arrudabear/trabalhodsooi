<<<<<<< HEAD

from Limites.tela_dispositivos import TelaDispositivos
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
                dispositivo = Dispositivo(dados_dispositivo["estado"], dados_dispositivo["potencia"],
                                          dados_dispositivo["tempo_ligado"], dados_dispositivo["timer_ligar"],
                                          dados_dispositivo["timer_desligar"], dados_dispositivo["codigo_dispositivo"],
                                          dados_dispositivo["modelo"])
                self.__dispositivos.append(dispositivo)
                self.__tela_dispositivos.mensagem("Dispositivo adicionado na lista!")
            else:
                raise KeyError
        except KeyError:
            self.__tela_dispositivos.mensagem("Dispositivo já existente na lista!") 
    
    def abre_tela(self):
        opcoes = {1: self.incluir_dispositivo}

        continua = True
        while continua: 
            opcoes[self.__tela_dispositivos.tela_opcoes()]() 


=======
from Controladores.controladorSistema import ControladorSistema


class ControladorDispositivos():
    def __init__(self, controlador_sistema: ControladorSistema):
        if isinstance(controlador_sistema, ControladorSistema):
            self.__controlador_sistema = controlador_sistema
>>>>>>> 1eceaf3590c8b004e8e5d00996dd08ed04285b00

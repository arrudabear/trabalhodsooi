
from Limites.telaDispositivos import TelaDispositivos
from Entidades.dispositivo import Dispositivo
from Entidades.arCondicionado import ArCondicionado
from Entidades.geladeira import Geladeira
from Entidades.forno import Forno
from Entidades.cafeteira import Cafeteira
from Entidades.cortina import Cortina
from Entidades.lavadouraDeRoupa import LavadoraDeRoupa
from Entidades.lavaloucas import LavaLoucas
from Entidades.pontoDeluz import PontoDeLuz
from Entidades.som import Som
from Entidades.tv import TV

class ControladorDispositivos(): 
    #colocar contolador sistema no UML 
    def __init__(self):
        self.__dispositivos = [] 
        #self.__controlador_sistema = controlador_sistema
        self.__tela_dispositivos = TelaDispositivos() 
    
    def find_dispositivo(self, codigo: int, modelo: str): 
        for dispositivo in self.__dispositivos:
            if (dispositivo.codigo_dispositivo == codigo) and (dispositivo.modelo == modelo): 
                return dispositivo
        return None 

    def incluir_dispositivo(self): 
        dados_dispositivo = self.__tela_dispositivos.pega_dados_dispositivo()
        dispositivo = self.find_dispositivo(dados_dispositivo["codigo"], dados_dispositivo["modelo"])
        #tipo_dispositivo = self.__tela_dispositivos.escolher_tipo_dispositivo() 
        try:
            if dispositivo == None:
                dispositivo = Dispositivo(dados_dispositivo["nome"], dados_dispositivo["codigo"], dados_dispositivo["potencia"],
                                          dados_dispositivo["modelo"])
            
                self.__dispositivos.append(dispositivo)
                self.__tela_dispositivos.mostrar_mensagem("Dispositivo adicionado na lista!")
            else:
                raise KeyError
        except KeyError:
            self.__tela_dispositivos.mostrar_mensagem("Dispositivo já existente na lista!") 

    def lista_dispositivos(self): 
        self.__tela_dispositivos.mostrar_mensagem("-------- DISPOSITIVOS CADASTRADOS ----------")
        for dispositivo in self.__dispositivos:
            self.__tela_dispositivos.mostra_dispositivo({"nome": dispositivo.nome, "codigo_dispositivo": dispositivo.codigo_dispositivo, "modelo": dispositivo.modelo})

    def abre_tela(self):
        opcoes = {1: self.incluir_dispositivo, 3: self.lista_dispositivos}

        continua = True
        while continua: 
            opcoes[self.__tela_dispositivos.tela_opcoes()]()
    
    
    def controla_dispositivo(self, dispositivo: Dispositivo):
        self.__tela_dispositivos.mostrar_mensagem("--- Controle do Dispositivo ---")
        self.__tela_dispositivos.mostra_dispositivo(dispositivo.nome, dispositivo.codigo_dispositivo, dispositivo.modelo)
        if type(dispositivo) == ArCondicionado or type(dispositivo) == Geladeira or type(dispositivo) == Forno:
            self.__tela_dispositivos.controle_temp(dispositivo.nome, dispositivo.codigo_dispositivo)
        else:
            self.__tela_dispositivos.controle
    
    def liga_desliga(self, dispositivo):
        pass

    def controlar_temperatura(self, dispositivo):
        pass
    
    def controlar_timer(self, dispositivo):
        pass

    def info_disp(self, dispositivo):
        pass

    '''def dipositivos_comodo(self, comodo):
        for dispositivo in self.__dipositivos:
            if dispositivo.comodo == comodo:'''




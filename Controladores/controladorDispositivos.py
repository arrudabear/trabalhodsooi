
from dis import dis
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
    def __init__(self, controlador_sistema):
        self.__dispositivos = [] 
        self.__controlador_sistema = controlador_sistema
        self.__tela_dispositivos = TelaDispositivos() 
    
    def find_dispositivo(self, codigo: int, nome: str): 
        for dispositivo in self.__dispositivos:
            if (dispositivo.codigo == codigo) and (dispositivo.nome == nome): 
                return dispositivo
        return None 

    def incluir_dispositivo(self): 
        dados_dispositivo = self.__tela_dispositivos.pega_dados_dispositivo()
        dispositivo = self.find_dispositivo(int(dados_dispositivo["codigo"]), dados_dispositivo["nome"])
        tipo_dispositivo = self.__tela_dispositivos.escolher_tipo_dispositivo() 
        try:
            if dispositivo == None:
                if tipo_dispositivo == 1:
                    dispositivo = ArCondicionado(dados_dispositivo["nome"], int(dados_dispositivo["codigo"]), float(dados_dispositivo["potencia"]),
                                                 dados_dispositivo["modelo"])
                elif tipo_dispositivo == 2: 
                    dispositivo = Cafeteira(dados_dispositivo["nome"], int(dados_dispositivo["codigo"]), float(dados_dispositivo["potencia"]),
                                            dados_dispositivo["modelo"])
                elif tipo_dispositivo == 3:
                    dispositivo = Cortina(dados_dispositivo["nome"], int(dados_dispositivo["codigo"]), float(dados_dispositivo["potencia"]),
                                          dados_dispositivo["modelo"])
                elif tipo_dispositivo == 4:
                    dispositivo = Forno(dados_dispositivo["nome"], int(dados_dispositivo["codigo"]), float(dados_dispositivo["potencia"]),
                                        dados_dispositivo["modelo"])
                elif tipo_dispositivo == 5:
                    dispositivo = Geladeira(dados_dispositivo["nome"], int(dados_dispositivo["codigo"]), float(dados_dispositivo["potencia"]),
                                            dados_dispositivo["modelo"])
                elif tipo_dispositivo == 6: 
                    dispositivo = LavadoraDeRoupa(dados_dispositivo["nome"], int(dados_dispositivo["codigo"]), float(dados_dispositivo["potencia"]),
                                            dados_dispositivo["modelo"])
                elif tipo_dispositivo == 7: 
                    dispositivo = PontoDeLuz(dados_dispositivo["nome"], int(dados_dispositivo["codigo"]), float(dados_dispositivo["potencia"]),
                                            dados_dispositivo["modelo"])
                elif tipo_dispositivo == 8: 
                    dispositivo = Som(dados_dispositivo["nome"], int(dados_dispositivo["codigo"]), float(dados_dispositivo["potencia"]),
                                      dados_dispositivo["modelo"])
                elif tipo_dispositivo == 9: 
                    dispositivo = TV(dados_dispositivo["nome"], int(dados_dispositivo["codigo"]), float(dados_dispositivo["potencia"]),
                                     dados_dispositivo["modelo"])
                elif tipo_dispositivo == 10: 
                    dispositivo = LavaLoucas(dados_dispositivo["nome"], int(dados_dispositivo["codigo"]), float(dados_dispositivo["potencia"]),
                                             dados_dispositivo["modelo"])

                self.__dispositivos.append(dispositivo)
                self.__tela_dispositivos.mostrar_mensagem("DISPOSIITIVO ADICIONADO NA LISTA!")
            else:
                raise KeyError
        except KeyError:
            self.__tela_dispositivos.mostrar_mensagem("Dispositivo já existente na lista!") 

    def lista_dispositivos(self): 
        if self.__dispositivos == []:
            self.__tela_dispositivos.mostrar_mensagem("Ainda não há dispositivos cadastrados")
            self.__tela_dispositivos.mostrar_mensagem("Deseja criar um novo dispositivo? [SIM: 1 / NÃO: 0]")
            opcao = self.__tela_dispositivos.seleciona_opcao("Escolha a opção: ", [0,1])
            if opcao == 1: 
                self.incluir_dispositivo() 
                self.lista_dispositivos()
            else: 
                self.lista_dispositivos()
                self.abre_tela()

        else:
            self.__tela_dispositivos.mostrar_mensagem("------ DISPOSITIVOS CADASTRADOS ------")
            for dispositivo in self.__dispositivos:
                self.__tela_dispositivos.mostra_dispositivo({"nome": dispositivo.nome, "codigo": dispositivo.codigo})
        

    def excluir_dispositivo(self):
        self.lista_dispositivos()
        dispositivo_escolhido = self.__tela_dispositivos.escolhe_dispositivo()  
        dispositivo = self.find_dispositivo(int(dispositivo_escolhido["codigo"]), dispositivo_escolhido["nome"])
        try: 
            if (dispositivo is not None): 
                self.__dispositivos.remove(dispositivo)
                self.__tela_dispositivos.mostrar_mensagem("DISPOSITIVO EXCLUIDO!!")
                self.lista_dispositivos()
            else:
                raise KeyError
        except KeyError: 
            self.__tela_dispositivos.mostrar_mensagem("DISPOSITIVO NÃO EXISTENTE!!")

    def altera_dispositivo(self):
        self.lista_dispositivos()
        dispositivo_escolhido = self.__tela_dispositivos.escolhe_dispositivo()  
        dispositivo = self.find_dispositivo(int(dispositivo_escolhido["codigo"]), dispositivo_escolhido["nome"])
        try:
            if (dispositivo is not None):
                self.__dispositivos.remove(dispositivo)
                self.incluir_dispositivo() 
                self.__tela_dispositivos.mostrar_mensagem("DISPOSITIVO ALTERADO!!")
                self.lista_dispositivos() 
            else:
                raise KeyError 
        except KeyError: 
            self.__tela_comodos.mostrar_mensagem("DISPOSITIVOS NÃO EXISTENTE!!")

    def abre_tela(self):
        opcoes = {1: self.incluir_dispositivo, 2: self.excluir_dispositivo, 3: self.lista_dispositivos, 4: self.altera_dispositivo, 6: self.controla_dispositivo}

        while True:
            opcoes[self.__tela_dispositivos.tela_opcoes()]()
    
    def calcular_gasto(self): 
        self.lista_dispositivos() 
        dispositivo_escolhido = self.__tela_dispositivos.escolhe_dispositivo() 
        dispositivo = self.find_dispositivo(int(dispositivo_escolhido["codigo"]), dispositivo_escolhido["nome"])
    
    def controla_dispositivo(self):
        self.lista_dispositivos() 
        dados_dispositivo = self.__tela_dispositivos.escolhe_dispositivo() 
        dispositivo = self.find_dispositivo(int(dados_dispositivo["codigo"]), dados_dispositivo["nome"])
        self.__tela_dispositivos.mostrar_mensagem("--- Controle do Dispositivo ---")
        if type(dispositivo) == ArCondicionado:
            self.__tela_dispositivos.controle_arcondicionado()
        elif type(dispositivo) == Geladeira:
            self.__tela_dispositivos.controle_geladeira()
        elif type(dispositivo) == Forno:
            self.__tela_dispositivos.controle_forno()
        elif type(dispositivo) == TV:
            self.__tela_dispositivos.controle_tv()
        elif type(dispositivo) == Som:
            self.__tela_dispositivos.controle_som()
        elif type(dispositivo) == LavadoraDeRoupa:
            self.__tela_dispositivos.controle_lavadoras()
        elif type(dispositivo) == LavaLoucas:
            self.__tela_dispositivos.controle_lavaloucas()
        elif type(dispositivo) == Cafeteira:
            self.__tela_dispositivos.controle_cafeteira()
        elif type(dispositivo) == Cortina:
            self.__tela_dispositivos.controle_cortina()
        elif type(dispositivo) == PontoDeLuz:
            self.__tela_dispositivos.controle_luz()
        self.abre_tela_opcoes_controle() 
#-----------------------------------------------------------------------------------------------------------------
    def abre_tela_opcoes_controle(self):
        opcoes = {1: self.liga_desliga}

        while True:
            opcoes[self.__tela_dispositivos.controle_forno()]()

    def liga_desliga(self):
        dados_dispositivo = self.__tela_dispositivos.escolhe_dispositivo()
        dispositivo = self.find_dispositivo(dados_dispositivo["codigo"], dados_dispositivo["nome"])
        Forno(dispositivo).ligar
        print("ligar_desligar")

    def controlar_temperatura(self, dispositivo):
        pass
    
    def controlar_timer(self, dispositivo):
        pass

    def info_disp(self, dispositivo):
        pass

    def escolhe_dispositivo(self):
        disp = self.__tela_dispositivos.escolhe_dispositivo()
        return disp

    '''def dipositivos_comodo(self, comodo):
        for dispositivo in self.__dipositivos:
            if dispositivo.comodo == comodo:'''




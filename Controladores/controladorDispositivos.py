
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
                self.__tela_dispositivos.mostrar_mensagem("-----------------------------------")
        

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
            self.__tela_dispositivos.mostrar_mensagem("DISPOSITIVOS NÃO EXISTENTE!!")

    def abre_tela(self):
        opcoes = {1: self.incluir_dispositivo, 2: self.excluir_dispositivo, 3: self.lista_dispositivos, 4: self.altera_dispositivo, 6: self.controla_dispositivo}

        while True:
            opcoes[self.__tela_dispositivos.tela_opcoes()]()
    
    def calcular_gasto(self): 
        self.lista_dispositivos() 
        dispositivo_escolhido = self.__tela_dispositivos.escolhe_dispositivo() 
        dispositivo = self.find_dispositivo(int(dispositivo_escolhido["codigo"]), dispositivo_escolhido["nome"])
        print(dispositivo.potencia)
    
    def controla_dispositivo(self):
        self.lista_dispositivos() 
        dados_dispositivo = self.__tela_dispositivos.escolhe_dispositivo() 
        dispositivo = self.find_dispositivo(int(dados_dispositivo["codigo"]), dados_dispositivo["nome"])
        try:
            if (dispositivo is not None):
                self.__tela_dispositivos.mostrar_mensagem("--- Controle do Dispositivo ---")
                if type(dispositivo) == ArCondicionado:
                    lista_opcoes = {1: self.liga_desliga, 2: self.controlar_temperatura, 3: self.controlar_timer, 4: self.info_disp, 0: self.void_func}
                    opcao_escolhida = self.__tela_dispositivos.controle_arcondicionado()
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida(dispositivo)

                elif type(dispositivo) == Geladeira:
                    lista_opcoes = {1: self.liga_desliga, 2: self.controlar_temperatura, 3: self.controlar_timer, 4: self.info_disp, 0: self.void_func}
                    opcao_escolhida = self.__tela_dispositivos.controle_geladeira()
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida(dispositivo)
                    
                elif type(dispositivo) == Forno:
                    lista_opcoes = {1: self.liga_desliga, 2: self.controlar_temperatura, 3: self.controlar_timer, 4: self.info_disp, 0: self.void_func}
                    opcao_escolhida = self.__tela_dispositivos.controle_forno()
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida(dispositivo)

                elif type(dispositivo) == TV:
                    lista_opcoes = {1: self.liga_desliga, 2: self.controlar_canal,3: self.controlar_volume, 4: self.controlar_timer, 5: self.info_disp, 0: self.void_func}
                    opcao_escolhida = self.__tela_dispositivos.controle_tv()
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida(dispositivo)

                elif type(dispositivo) == Som:
                    lista_opcoes = {1: self.liga_desliga, 2: self.controlar_musica, 3: self.controlar_volume, 4: self.controlar_timer, 5: self.info_disp, 0: self.void_func}
                    opcao_escolhida = self.__tela_dispositivos.controle_som()
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida(dispositivo)

                elif type(dispositivo) == LavadoraDeRoupa:
                    lista_opcoes = {1: self.liga_desliga, 2: self.controlar_modo, 3: self.controlar_timer, 4: self.info_disp, 0: self.void_func}
                    opcao_escolhida = self.__tela_dispositivos.controle_lavadoras()
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida(dispositivo)

                elif type(dispositivo) == LavaLoucas:
                    lista_opcoes = {1: self.liga_desliga, 2: self.controlar_modo, 3: self.controlar_timer, 4: self.info_disp, 0: self.void_func}
                    opcao_escolhida = self.__tela_dispositivos.controle_lavaloucas()
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida(dispositivo)

                elif type(dispositivo) == Cafeteira:
                    lista_opcoes = {1: self.liga_desliga, 2: self.controlar_timer, 3: self.info_disp, 0: self.void_func}
                    opcao_escolhida = self.__tela_dispositivos.controle_cafeteira()
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida(dispositivo)

                elif type(dispositivo) == Cortina:
                    lista_opcoes = {1: self.liga_desliga, 2: self.controlar_timer, 3: self.info_disp, 0: self.void_func}
                    opcao_escolhida = self.__tela_dispositivos.controle_cortina()
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida(dispositivo)

                elif type(dispositivo) == PontoDeLuz:
                    lista_opcoes = {1: self.liga_desliga, 2: self.controlar_timer, 3: self.info_disp, 0: self.void_func}
                    opcao_escolhida = self.__tela_dispositivos.controle_luz()
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida(dispositivo)
            else:
                raise KeyError
        except KeyError: 
            self.__tela_dispositivos.mostrar_mensagem("DISPOSITIVOS NÃO EXISTENTE!!")

        #self.abre_tela_opcoes_controle() 
#-----------------------------------------------------------------------------------------------------------------
    def abre_tela_opcoes_controle(self):
        opcoes = {1: self.liga_desliga, 2: self.controlar_temperatura, 3: self.controlar_timer, 4: self.info_disp}

        while True:
            opcoes[self.__tela_dispositivos.controle_forno()]()

    def liga_desliga(self, dispositivo):
        self.__tela_dispositivos.mostrar_mensagem("[LIGAR: 1 / DESLIGAR: 0]")
        opcao = self.__tela_dispositivos.seleciona_opcao("Escolha a opção: ", [0,1])
        if opcao == 1: 
            dispositivo.ligar()
            usuario = self.__controlador_sistema.usuario_atual
            self.__controlador_sistema.controlador_eventos.registrar_evento(usuario, dispositivo)
            print(dispositivo.estado)
            print("ligado")
        else: 
            dispositivo.desligar() 
            print(dispositivo.estado)
            print("desligado")

    def controlar_temperatura(self, dispositivo):
        print(dispositivo.estado)
        self.__tela_dispositivos.mostrar_mensagem("[AUMENTAR TEMPERATURA: 1 / DIMINUIR TEMPERATURA: 2]")
        opcao = self.__tela_dispositivos.seleciona_opcao("Escolha a opção: ", [1,2]) 
        if opcao == 1: 
            dispositivo.aumentar_temperatura() 
            self.__tela_dispositivos.mostrar_mensagem(f"Temperatura: {dispositivo.temperatura}")
        else: 
            dispositivo.diminuir_temperatura() 
            self.__tela_dispositivos.mostrar_mensagem(f"Temperatura: {dispositivo.temperatura}")

    def controlar_timer(self, dispositivo):
        print(dispositivo.estado)
        self.__tela_dispositivos.mostrar_mensagem("[ESCOLHER TEMPO TIMER LIGAR: 1 / ESCOLHER TEMPO TIMER DESLIGAR: 0]")
        opcao = self.__tela_dispositivos.seleciona_opcao("Escolha a opção: ", [1,0])
        self.__tela_dispositivos.mostrar_mensagem("Escolha o valor do timer: ")
        if opcao == 1: 
            tempo = self.__tela_dispositivos.pegar_valor_float() 
            dispositivo.escolher_timer_ligar(float(tempo))
            self.__tela_dispositivos.mostrar_mensagem(f"Timer ligar: {dispositivo.temperatura}")
        else: 
            tempo = self.__tela_dispositivos.pegar_valor_float() 
            dispositivo.timer_desligar(float(tempo)) 
            self.__tela_dispositivos.mostrar_mensagem(f"Timer ligar: {dispositivo.temperatura}")

    def escolher_modo(self, dispositivo): 
        self.__tela_dispositivos.mostrar_mensagem("--- MODOS ---\n1 - DELICADO\n2 - NORMAL\n3 - RÁPIDO")
        opcao = self.__tela_dispositivos.seleciona_opcao("Escolha a opção: ", [1,2,3])
        dispositivo.escolher_modo() 

    def info_disp(self, dispositivo):
        self.__tela_dispositivos.mostrar_mensagem("INFORMAÇÔES DISPOSITIIVO")
        self.__tela_dispositivos.mostrar_mensagem(f"Nome: {dispositivo.nome}")
        self.__tela_dispositivos.mostrar_mensagem(f"Código: {dispositivo.codigo}")
        self.__tela_dispositivos.mostrar_mensagem(f"Modelo: {dispositivo.modelo}")
        self.__tela_dispositivos.mostrar_mensagem(f"Potência: {dispositivo.potencia}")
        self.__tela_dispositivos.mostrar_mensagem(f"Temperatura: {dispositivo.temperatura}")
        self.__tela_dispositivos.mostrar_mensagem(f"Estado: {dispositivo.estado}")
    
    def controlar_canal(self, dispositivo):
        controlando_canal = True
        while controlando_canal == True:
            self.__tela_dispositivos.mostrar_mensagem("Digite o canal de sua escolha: ")
            canal = self.__tela_dispositivos.pegar_valor_int()
            try:
                if canal >= dispositivo.canal_max or canal <= dispositivo.canal_min:
                    dispositivo.escolher_canal(canal)
                    self.__tela_dispositivos.mostrar_mensagem("Canal trocado com sucesso!")
                    controlando_canal = False
                else:
                    raise ValueError
            except ValueError:
                self.__tela_dispositivos.mostrar_mensagem(f"Digite apenas canais dentro do intervalo:\nMínimo: {dispositivo.canal_min}\nMáximo: {dispositivo.canal_max}")


    def controlar_volume(self, dispositivo):
        self.__tela_dispositivos.mostrar_mensagem("[AUMENTAR VOLUME: 1 / DIMINUIR VOLUME: 2]")
        opcao = self.__tela_dispositivos.seleciona_opcao("Escolha a opção: ", [1,2]) 
        if opcao == 1: 
            dispositivo.aumentar_volume() 
            self.__tela_dispositivos.mostrar_mensagem(f"Volume: {dispositivo.volume}")
        else: 
            dispositivo.diminuir_volume() 
            self.__tela_dispositivos.mostrar_mensagem(f"Volume: {dispositivo.volume}")

    def controlar_musica(self, dispositivo):
        self.__tela_dispositivos.mostrar_mensagem("--- CONTROLE PLAYER DE MÚSICA ---")
        self.__tela_dispositivos.mostrar_mensagem("[TOCAR/PAUSAR: 1 / PRÓXIMA MÚSICA: 2 / VOLTAR MÚSICA: 3]")
        opcao = self.__tela_dispositivos.seleciona_opcao("Escolha a opção: ", [1,2,3])
        acao = dispositivo.controlar_musica(opcao)
        self.__tela_dispositivos.mostrar_mensagem(f"O player {acao} a música.")

    def void_func(self, dispositivo):
        pass
                

    def escolhe_dispositivo(self):
        disp = self.__tela_dispositivos.escolhe_dispositivo()
        return disp

    def tipo_dispositivo(self, dispositivo): 
        if type(dispositivo) == ArCondicionado:
            dispositivo = ArCondicionado(dispositivo.nome, dispositivo.codigo, dispositivo.potencia, dispositivo.modelo)
        elif type(dispositivo) == Geladeira:
            dispositivo = Geladeira(dispositivo.nome, dispositivo.codigo, dispositivo.potencia, dispositivo.modelo)
        elif type(dispositivo) == Forno:
            dispositivo = Forno(dispositivo.nome, dispositivo.codigo, dispositivo.potencia, dispositivo.modelo)
        elif type(dispositivo) == TV:
            dispositivo = TV(dispositivo.nome, dispositivo.codigo, dispositivo.potencia, dispositivo.modelo)
        elif type(dispositivo) == Som:
            dispositivo = Som(dispositivo.nome, dispositivo.codigo, dispositivo.potencia, dispositivo.modelo)
        elif type(dispositivo) == LavadoraDeRoupa:
            dispositivo = LavadoraDeRoupa(dispositivo.nome, dispositivo.codigo, dispositivo.potencia, dispositivo.modelo)
        elif type(dispositivo) == LavaLoucas:
            dispositivo = LavaLoucas(dispositivo.nome, dispositivo.codigo, dispositivo.potencia, dispositivo.modelo)
        elif type(dispositivo) == Cafeteira:
            dispositivo = Cafeteira(dispositivo.nome, dispositivo.codigo, dispositivo.potencia, dispositivo.modelo)
        elif type(dispositivo) == Cortina:
            dispositivo = Cortina(dispositivo.nome, dispositivo.codigo, dispositivo.potencia, dispositivo.modelo)
        elif type(dispositivo) == PontoDeLuz:
            dispositivo = PontoDeLuz(dispositivo.nome, dispositivo.codigo, dispositivo.potencia, dispositivo.modelo)

        return dispositivo

    '''def dipositivos_comodo(self, comodo):
        for dispositivo in self.__dipositivos:
            if dispositivo.comodo == comodo:'''




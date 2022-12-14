
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
from DAOs.dispositivos_dao import DispositivoDAO

class ControladorDispositivos(): 
    #colocar contolador sistema no UML 
    def __init__(self, controlador_sistema):
        self.__dispositivo_DAO = DispositivoDAO()
        self.__dispositivos = self.__dispositivo_DAO.get_all() 
        self.__controlador_sistema = controlador_sistema
        self.__tela_dispositivos = TelaDispositivos() 
    
    def find_dispositivo(self, codigo: int, nome: str): 
        self.__dispositivo = self.__dispositivo_DAO.get_all() 
        for dispositivo in self.__dispositivos:
            if (dispositivo.codigo == codigo) or (dispositivo.nome == nome): 
                return dispositivo

        return None 
        
    def incluir_dispositivo(self): 
        dados_dispositivo = self.__tela_dispositivos.pega_dados_dispositivo()
        if dados_dispositivo == None:
            pass
        else:
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

                    self.__dispositivo_DAO.add(dispositivo)
                    self.__tela_dispositivos.mostrar_mensagem("DISPOSIITIVO ADICIONADO NA LISTA!")
                else:
                    raise KeyError
            except KeyError:
                self.__tela_dispositivos.mostrar_mensagem("Dispositivo j?? existente na lista!") 

    def lista_dispositivos(self): 
        self.__dispositivos = self.__dispositivo_DAO.get_all() 
        dados_dispositivo = []
        # self.__tela_dispositivos.mostrar_mensagem("------ DISPOSITIVOS CADASTRADOS ------")
        for dispositivo in self.__dispositivos:
            dados_dispositivo.append({'nome_disp': dispositivo.nome, 'codigo_disp': dispositivo.codigo})
            # self.__tela_dispositivos.mostra_dispositivo({"nome": dispositivo.nome, "codigo": dispositivo.codigo})
            # self.__tela_dispositivos.mostrar_mensagem("-----------------------------------")
        self.__tela_dispositivos.mostra_dispositivo(dados_dispositivo)

    def excluir_dispositivo(self):
        self.lista_dispositivos()
        dispositivo_escolhido = self.__tela_dispositivos.escolhe_dispositivo()  
        if dispositivo_escolhido == None:
            pass 
        else: 
            try: 
                dispositivo = self.find_dispositivo(int(dispositivo_escolhido["codigo"]), dispositivo_escolhido["nome"])
                if (dispositivo is not None): 
                    self.__dispositivo_DAO.remove(dispositivo_escolhido["codigo"])
                    self.__tela_dispositivos.mostrar_mensagem("DISPOSITIVO EXCLUIDO!!")
                    self.lista_dispositivos()
                else:
                    raise KeyError
            except KeyError: 
                self.__tela_dispositivos.mostrar_mensagem("DISPOSITIVO N??O EXISTENTE OU C??DIGO INV??LIDO!!")

    def altera_dispositivo(self):
        self.lista_dispositivos()
        dispositivo_escolhido = self.__tela_dispositivos.escolhe_dispositivo()  
        if dispositivo_escolhido == None:
            pass
        else:
            try:
                dispositivo = self.find_dispositivo(int(dispositivo_escolhido["codigo"]), dispositivo_escolhido["nome"])
                if (dispositivo is not None):
                    self.__dispositivo_DAO.remove(dispositivo_escolhido["codigo"])
                    self.incluir_dispositivo() 
                    self.__tela_dispositivos.mostrar_mensagem("DISPOSITIVO ALTERADO!!")
                    self.lista_dispositivos() 
                else:
                    raise KeyError 
            except KeyError: 
                self.__tela_dispositivos.mostrar_mensagem("DISPOSITIVO N??O EXISTENTE OU C??DIGO INV??LIDO!!")

    def abre_tela(self):
        opcoes = {1: self.incluir_dispositivo, 2: self.excluir_dispositivo, 3: self.lista_dispositivos, 4: self.altera_dispositivo, 5: self.calcular_gasto, 6: self.controla_dispositivo, 0: self.voltar}

        while True:
            opcoes[self.__tela_dispositivos.tela_opcoes()]()
    
    def calcular_gasto(self): 
        self.lista_dispositivos() 
        dispositivo_escolhido = self.__tela_dispositivos.escolhe_dispositivo() 
        dispositivo = self.find_dispositivo(int(dispositivo_escolhido["codigo"]), dispositivo_escolhido["nome"])
        tempo_ligado = self.__tela_dispositivos.pegar_valor_int("Digite o tempo, em horas, que o dispositivo ficou ligado: ")
        gasto_energia = dispositivo.potencia * tempo_ligado
        self.__tela_dispositivos.mostrar_mensagem(f"O dispositivo gastou: {gasto_energia} W/h")
    
    def controla_dispositivo(self):
        self.lista_dispositivos() 
        dados_dispositivo = self.__tela_dispositivos.escolhe_dispositivo()
        if dados_dispositivo == None:
            pass 
        else: 
            try:
                dispositivo = self.find_dispositivo(int(dados_dispositivo["codigo"]), dados_dispositivo["nome"])
                if (dispositivo is not None):
                    # self.__tela_dispositivos.mostrar_mensagem("--- Controle do Dispositivo ---")
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
                        lista_opcoes = {1: self.liga_desliga, 2: self.escolher_modo, 3: self.controlar_timer, 4: self.info_disp, 0: self.void_func}
                        opcao_escolhida = self.__tela_dispositivos.controle_lavadoras()
                        funcao_escolhida = lista_opcoes[opcao_escolhida]
                        funcao_escolhida(dispositivo)

                    elif type(dispositivo) == LavaLoucas:
                        lista_opcoes = {1: self.liga_desliga, 2: self.escolher_modo, 3: self.controlar_timer, 4: self.info_disp, 0: self.void_func}
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
                self.__tela_dispositivos.mostrar_mensagem("DISPOSITIVO N??O EXISTENTE OU C??DIGO INV??LIDO!!")

        #self.abre_tela_opcoes_controle() 
#-----------------------------------------------------------------------------------------------------------------
    # def abre_tela_opcoes_controle(self):
    #     opcoes = {1: self.liga_desliga, 2: self.controlar_temperatura, 3: self.controlar_timer, 4: self.info_disp}

    #     while True:
    #         opcoes[self.__tela_dispositivos.controle_forno()]()

    def liga_desliga(self, dispositivo):
        usuario = self.__controlador_sistema.usuario_atual
        # self.__tela_dispositivos.mostrar_mensagem("[LIGAR: 1 / DESLIGAR: 0]")
        # opcao = self.__tela_dispositivos.seleciona_opcao("Escolha a op????o: ", [0,1])
        opcao = self.__tela_dispositivos.controle_ligar_desligar() 
        if opcao == 1: 
            dispositivo.ligar()
            self.__controlador_sistema.controlador_eventos.registrar_evento(usuario, dispositivo, "Ligar")
            self.__tela_dispositivos.mostrar_mensagem("Ligado")

        elif opcao == 2: 
            dispositivo.desligar() 
            self.__controlador_sistema.controlador_eventos.registrar_evento(usuario, dispositivo, "Desligar")
            self.__tela_dispositivos.mostrar_mensagem("Desligado")

    def controlar_temperatura(self, dispositivo):
        usuario = self.__controlador_sistema.usuario_atual
        # self.__tela_dispositivos.mostrar_mensagem("[AUMENTAR TEMPERATURA: 1 / DIMINUIR TEMPERATURA: 2]")
        # opcao = self.__tela_dispositivos.seleciona_opcao("Escolha a op????o: ", [1,2]) 
        opcao = self.__tela_dispositivos.controle_temperatura() 
        if opcao == 1: 
            dispositivo.aumentar_temperatura()
            self.__controlador_sistema.controlador_eventos.registrar_evento(usuario, dispositivo, "Aumentou Temperatura")
            self.__tela_dispositivos.mostrar_mensagem(f"Temperatura: {dispositivo.temperatura}")
        elif opcao == 2:
            dispositivo.diminuir_temperatura() 
            self.__controlador_sistema.controlador_eventos.registrar_evento(usuario, dispositivo, "Diminuiu Temperatura")
            self.__tela_dispositivos.mostrar_mensagem(f"Temperatura: {dispositivo.temperatura}")

    def controlar_timer(self, dispositivo):
        usuario = self.__controlador_sistema.usuario_atual
        # self.__tela_dispositivos.mostrar_mensagem("[ESCOLHER TEMPO TIMER LIGAR: 1 / ESCOLHER TEMPO TIMER DESLIGAR: 0]")
        # opcao = self.__tela_dispositivos.seleciona_opcao("Escolha a op????o: ", [1,0])
        opcao = self.__tela_dispositivos.controle_timer() 
        self.__tela_dispositivos.mostrar_mensagem("Escolha o valor do timer: ")
        if opcao == 1: 
            tempo = self.__tela_dispositivos.valor_float()
            if tempo == None:
                pass
            else: 
                dispositivo.escolher_timer_ligar(float(tempo))
                self.__tela_dispositivos.mostrar_mensagem(f"Timer ligar: {dispositivo.timer_ligar}")
                self.__controlador_sistema.controlador_eventos.registrar_evento(usuario, dispositivo, "Definiu Timer para Ligar")
        elif opcao == 2:
            tempo = self.__tela_dispositivos.valor_float() 
            if tempo == None: 
                pass
            else: 
                dispositivo.escolher_timer_desligar(float(tempo)) 
                self.__tela_dispositivos.mostrar_mensagem(f"Timer Desligar: {dispositivo.timer_desligar}")
                self.__controlador_sistema.controlador_eventos.registrar_evento(usuario, dispositivo, "Definiu Timer para Desligar")

    def escolher_modo(self, dispositivo):
        usuario = self.__controlador_sistema.usuario_atual
        # self.__tela_dispositivos.mostrar_mensagem("--- MODOS ---\n1 - DELICADO\n2 - NORMAL\n3 - R??PIDO")
        # opcao = self.__tela_dispositivos.seleciona_opcao("Escolha a op????o: ", [1,2,3])
        opcao = self.__tela_dispositivos.controle_modo() 
        dispositivo.escolher_modo(opcao)
        self.__tela_dispositivos.mostrar_mensagem(f"Modo: {dispositivo.modo}")
        self.__controlador_sistema.controlador_eventos.registrar_evento(usuario, dispositivo, "Definiu Timer Modo para o Dispositivo")


    # def info_disp(self, dispositivo):
    #     self.__tela_dispositivos.mostrar_mensagem("INFORMA????ES DISPOSITIIVO")
    #     self.__tela_dispositivos.mostrar_mensagem(f"Nome: {dispositivo.nome}")
    #     self.__tela_dispositivos.mostrar_mensagem(f"C??digo: {dispositivo.codigo}")
    #     self.__tela_dispositivos.mostrar_mensagem(f"Modelo: {dispositivo.modelo}")
    #     self.__tela_dispositivos.mostrar_mensagem(f"Pot??ncia: {dispositivo.potencia} Watts")
    #     if type(dispositivo) == Forno or type(dispositivo) == ArCondicionado or type(dispositivo) == Geladeira:
    #         self.__tela_dispositivos.mostrar_mensagem(f"Temperatura: {dispositivo.temperatura}")
    #     if type(dispositivo) == TV:
    #         self.__tela_dispositivos.mostrar_mensagem(f"Canal: {dispositivo.canal}")
    #     if type(dispositivo) == TV or type(dispositivo) == Som:
    #         self.__tela_dispositivos.mostrar_mensagem(f"Volume: {dispositivo.volume}")
    #     if dispositivo.estado == True:
    #         self.__tela_dispositivos.mostrar_mensagem("Estado: Ligado")
    #     elif dispositivo.estado == False:
    #         self.__tela_dispositivos.mostrar_mensagem("Estado: Desligado")
    #     if type(dispositivo) == LavadoraDeRoupa or type(dispositivo) == LavaLoucas: 
    #         self.__tela_dispositivos.mostrar_mensagem(f"Modo: {dispositivo.modo}")
    
    def info_disp(self, dispositivo): 
        dados_dispositivo = {}
        dados_dispositivo['nome'] = dispositivo.nome
        dados_dispositivo['codigo'] = dispositivo.codigo 
        dados_dispositivo['modelo'] = dispositivo.modelo
        dados_dispositivo['potencia'] = dispositivo.potencia
        dados_dispositivo['temperatura'] = 'N??o existe nesse dispositivo'
        dados_dispositivo['volume'] = 'N??o existe nesse dispositivo'
        dados_dispositivo['canal'] = 'N??o existe nesse dispositivo'
        dados_dispositivo['modo'] = 'N??o existe nesse dispositivo'
        if type(dispositivo) == Forno or type(dispositivo) == ArCondicionado or type(dispositivo) == Geladeira:
            dados_dispositivo['temperatura'] = dispositivo.temperatura
        if type(dispositivo) == TV:
            dados_dispositivo['canal'] = dispositivo.canal
        if type(dispositivo) == TV or type(dispositivo) == Som:
            dados_dispositivo['volume'] = dispositivo.volume
        if dispositivo.estado == True:
            dados_dispositivo['estado'] = 'Ligado'
        elif dispositivo.estado == False:
            dados_dispositivo['estado'] = 'Desligado'
        if type(dispositivo) == LavadoraDeRoupa or type(dispositivo) == LavaLoucas: 
            dados_dispositivo['modo'] = dispositivo.modo

        self.__tela_dispositivos.mostrar_info_disp(dados_dispositivo)
        

    def controlar_canal(self, dispositivo):
        usuario = self.__controlador_sistema.usuario_atual
        controlando_canal = True
        while controlando_canal == True:
            self.__tela_dispositivos.mostrar_mensagem("Digite o canal de sua escolha: ")
            canal = self.__tela_dispositivos.valor_int() 
            if canal == None:
                controlando_canal = False 
                break
            else:
                try:
                    if  dispositivo.canal_min <= canal <= dispositivo.canal_max:
                        dispositivo.escolher_canal(canal)
                        self.__controlador_sistema.controlador_eventos.registrar_evento(usuario, dispositivo, "Trocou Canal")
                        self.__tela_dispositivos.mostrar_mensagem("Canal trocado com sucesso!")
                        controlando_canal = False
                    else:
                        raise ValueError
                except ValueError:
                    self.__tela_dispositivos.mostrar_mensagem(f"Digite apenas canais dentro do intervalo:\nM??nimo: {dispositivo.canal_min}\nM??ximo: {dispositivo.canal_max}")


    def controlar_volume(self, dispositivo):
        usuario = self.__controlador_sistema.usuario_atual
        self.__tela_dispositivos.mostrar_mensagem("[AUMENTAR VOLUME: 1 / DIMINUIR VOLUME: 2]")
        opcao = self.__tela_dispositivos.controle_volume() 
        if opcao == 1: 
            dispositivo.aumentar_volume() 
            self.__controlador_sistema.controlador_eventos.registrar_evento(usuario, dispositivo, "Aumentou Volume")
            self.__tela_dispositivos.mostrar_mensagem(f"Volume: {dispositivo.volume}")
        elif opcao == 2: 
            dispositivo.diminuir_volume()
            self.__controlador_sistema.controlador_eventos.registrar_evento(usuario, dispositivo, "Diminuiu Volume")
            self.__tela_dispositivos.mostrar_mensagem(f"Volume: {dispositivo.volume}")

    def controlar_musica(self, dispositivo):
        usuario = self.__controlador_sistema.usuario_atual
        # self.__tela_dispositivos.mostrar_mensagem("--- CONTROLE PLAYER DE M??SICA ---")
        # self.__tela_dispositivos.mostrar_mensagem("[TOCAR/PAUSAR: 1 / PR??XIMA M??SICA: 2 / VOLTAR M??SICA: 3]")
        opcao = self.__tela_dispositivos.controle_musica() 
        acao = dispositivo.controlar_musica(opcao)
        if acao == None:
            pass
        else:
            self.__tela_dispositivos.mostrar_mensagem(f"O player {acao} a m??sica.")
            self.__controlador_sistema.controlador_eventos.registrar_evento(usuario, dispositivo, f"{acao} a M??sica")


    def void_func(self, dispositivo):
        pass
                
    def escolhe_dispositivo(self):
        disp = self.__tela_dispositivos.escolhe_dispositivo()
        return disp

    def mostra_dispositivo(self, dados_dispositivo):
        self.__tela_dispositivos.mostra_dispositivo(dados_dispositivo) 

    def voltar(self): 
        self.__controlador_sistema.abre_tela() 




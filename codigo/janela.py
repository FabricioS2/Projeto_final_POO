import tkinter as tk
import pygame
from tela_de_fundo import TelaDeFundo
from jogador import Jogador
from bloco import Bloco
from fogo import Fogo
from inimigo import Inimigo

class Janela():
    def __init__(self):
        self.__largura, self.__altura = self.obter_informacoes_monitor()
        self.__fps = 60
        

    def get_largura(self):
        return self.__largura
    
    def get_altura(self):
        return self.__altura
    
    def get_fps(self):
        return self.__fps
    
    def get_velocidade_jogador(self):
        return self.__velocidade_jogador

    def iniciar_janela(self):
        janela = pygame.display.set_mode((self.get_largura(), self.get_altura()))
        return janela

    def instanciar_janela(self):
        janela = self.iniciar_janela()
        
        relogio = pygame.time.Clock()
        tela_de_funfo = TelaDeFundo()
        backgroun, bg_tela = tela_de_funfo.get_tela_de_fundo("Blue.png", self.get_largura(), self.get_altura())
            
        tamanho_bloco = 96
        jogador = Jogador(self.get_largura()//2,100,50,50)
        inimigo = Inimigo(self.get_largura()//2,130,50,50)
        fogo = Fogo(tamanho_bloco, self.get_altura() - tamanho_bloco*2, tamanho_bloco, 96)
        piso = [Bloco(i * tamanho_bloco, self.get_altura() - tamanho_bloco, tamanho_bloco)
             for i in range(-self.get_largura() // tamanho_bloco, (self.get_largura() * 2) // tamanho_bloco)]
        objetos = [*piso,
                   Bloco(0,self.get_altura()-tamanho_bloco*2,tamanho_bloco),
                   Bloco(tamanho_bloco*3,self.get_altura()-tamanho_bloco*4,tamanho_bloco),
                   fogo,     
                   ]

        pygame.init()
        pygame.mixer.init()

        run = True
        offset_x = 0

        tela_de_funfo.gerar_som()
        while run:
            relogio.tick(self.get_fps())
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and jogador.contador_de_pulo < 2:
                        jogador.pular()
                        jogador.gerar_som()



            jogador.loop_jogador(self.get_fps())
            inimigo.loop_inimigo(self.get_fps())
            inimigo.movimentar_inimigo(inimigo,objetos)
            jogador.mapear_teclas(jogador,objetos)

            tela_de_funfo.desenhar_tela(janela, backgroun, bg_tela, jogador,inimigo,objetos,offset_x)

            if ((jogador.rect.right - offset_x >= self.get_largura()//2) and jogador.x_vel >0 ) or ((jogador.rect.left - offset_x <= self.get_largura()//2) and jogador.x_vel < 0):
                offset_x += jogador.x_vel

        pygame.quit()
        quit()

    def obter_informacoes_monitor(self):
        root = tk.Tk()
        largura = root.winfo_screenwidth()
        altura = root.winfo_screenheight()
        root.destroy()
        
        return int(largura - (largura * 0.2)), int(altura - (altura * 0.2))

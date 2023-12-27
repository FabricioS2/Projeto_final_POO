import pygame
from os.path import join
from soms import MixIn_Son

class TelaDeFundo(MixIn_Son):
    def get_tela_de_fundo(self,nome,LARGURA,ALTURA):
        imagem = pygame.image.load(join("assets","Background",nome))
        _,_,largura,altura = imagem.get_rect()
        TITULOS = []

        for i in range(LARGURA // largura +1):
            for j in range(ALTURA // altura + 1):
                pos = (i * largura,j*altura)
                TITULOS.append(pos)

        return TITULOS,imagem


    def desenhar_tela(self,janela,tela_de_fundo,bg_imagem,jogador,bloco,offset_x):
        for x in tela_de_fundo:
            janela.blit(bg_imagem,x)

        for x in bloco:
            x.inicializar_objeto(janela,offset_x)

        

        jogador.inicializar_jogador(janela,offset_x)
        pygame.display.update() 

    def gerar_som(self):
        audio = pygame.mixer.Sound(join("Soms","som_ambiente.mp3"))
        audio.set_volume(3)
        audio.play(loops=-1)
        
    
    

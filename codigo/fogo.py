from os.path import  join
import pygame
from sprite import SpriteJogo
from objeto import Objeto

# class Fogo(Objeto,SpriteJogo):
#     def __init__(self, x, y, largura, altura):
#         super().__init__(x, y, largura, altura)


class Fogo(Objeto,SpriteJogo):
    

    # def __init__(self, x, y, largura, altura):
    #     super().__init__(x, y, largura, altura)
    #     self.fogo = self.carregar_sprite("Traps", "Fire", largura, altura)
    #     self.imagem = self.fogo["off"][0]
    #     self.mascara = pygame.mask.from_surface(self.imagem)
    #     self.contagem_animacao = 0
    #     self.nome_animacao = "off"
    #     self.atraso_animacao = 3

    # def ligar(self):
    #     self.nome_animacao = "on"

    # def desligar(self):
    #     self.nome_animacao = "off"

    # def loop(self):
    #     sprites = self.fogo[self.nome_animacao]
    #     indice_sprite = (self.contagem_animacao //
    #                      self.atraso_animacao) % len(sprites)
    #     self.imagem = sprites[indice_sprite]
    #     self.contagem_animacao += 1

    #     self.rect = self.imagem.get_rect(topleft=(self.rect.x, self.rect.y))
    #     self.mascara = pygame.mask.from_surface(self.imagem)

    #     if self.contagem_animacao // self.atraso_animacao > len(sprites):
    #         self.contagem_animacao = 0

    # def __init__(self, x, y, tamanho):
    #     super().__init__(x, y, 16, 32)    
    #     bloco = self.obter_bloco(tamanho)
    #     self.image.blit(bloco, (0, 0))
    #     self.mascara = pygame.mask.from_surface(self.image)


    # def obter_bloco(self,tamanho):
    #     caminho = join("assets", "Traps", "fogo.png")
    #     imagem = pygame.image.load(caminho).convert_alpha()
    #     superficie = pygame.Surface((16, 32), pygame.SRCALPHA, 32)
    #     retangulo = pygame.Rect(16, 0, 16, 32)
    #     superficie.blit(imagem, (0, 0), retangulo)
    #     return (superficie)
    def __init__(self, x, y, largura, altura):
        super().__init__(x, y, largura, altura,"fogo")    
        bloco = self.obter_bloco(largura, altura)
        self.image.blit(bloco, (0, 0))
        self.mascara = pygame.mask.from_surface(self.image)

    def obter_bloco(self, largura, altura):
        caminho = join("assets", "Traps", "fogo.png")
        imagem = pygame.image.load(caminho).convert_alpha()
        superficie = pygame.Surface((largura, altura), pygame.SRCALPHA, 32)
        retangulo = pygame.Rect(0, 0, largura, altura)
        superficie.blit(imagem, (0, 0), retangulo)
        return pygame.transform.scale(superficie, (largura*4, altura*4))
        

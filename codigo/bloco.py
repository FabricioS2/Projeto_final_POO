from objeto import Objeto
from os.path import  join
import pygame
from sprite import SpriteJogo

class Bloco(Objeto,SpriteJogo):
    def __init__(self, x, y, tamanho):
        super().__init__(x, y, tamanho, tamanho)    
        bloco = self.obter_bloco(tamanho)
        self.image.blit(bloco, (0, 0))
        self.mascara = pygame.mask.from_surface(self.image)


    def obter_bloco(self,tamanho):
        caminho = join("assets", "Terrain", "Terrain.png")
        imagem = pygame.image.load(caminho).convert_alpha()
        superficie = pygame.Surface((tamanho, tamanho), pygame.SRCALPHA, 32)
        retangulo = pygame.Rect(96, 0, tamanho, tamanho)
        superficie.blit(imagem, (0, 0), retangulo)
        return pygame.transform.scale2x(superficie)
    
    


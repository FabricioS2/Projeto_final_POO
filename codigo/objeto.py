import pygame

class Objeto():
    def __init__(self, x, y, largura, altura, nome=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, largura, altura)
        self.image = pygame.Surface((largura, altura), pygame.SRCALPHA)
        self.largura = largura
        self.altura = altura
        self.nome = nome


    def inicializar_objeto(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))
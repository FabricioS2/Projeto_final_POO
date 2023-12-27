import pygame
from os.path import join
from sprite import SpriteJogo
from colicao import Mixin_colicao
from soms import MixIn_Son
from fogo import Fogo


class Inimigo(SpriteJogo, Mixin_colicao, MixIn_Son):
    def __init__(self, x, y, largura, altura):
        super().__init__()
        self.rect = pygame.Rect(x, y, largura, altura)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.velocidade_inimigo = 15
        self.velocidade_de_caida = 1
        self.contador_de_pulo = 0
        self.gravidade = 1
        self.sprites = self.carregar_sprite(
            "MainCharacters", "MaskDude", 32, 32, True)
        self.dano = False
        self.contador_dano = 0

    #def mover(self, distancia_x, distancia_y):
     #   self.rect.x += distancia_x
      #  self.rect.y += distancia_y

    #def mover_esquerda(self, vel):
     #   self.x_vel = -vel
      #  if self.direcao != "esquerda":
       #     self.direcao = "esquerda"
        #    self.contador_animacao = 0

    #def mover_direita(self, vel):
     #   self.x_vel = vel
      #  if self.direcao != "direita":
       #     self.direcao = "direita"
        #    self.contador_animacao = 0

    #def loop_inimigo(self, fps=60):
     #   self.y_vel += min(1, (self.velocidade_inimigo / fps) * self.gravidade)
      #  self.mover(self.x_vel, self.y_vel)

       # if self.dano:
        #    self.contador_dano += 1
         #   Fogo.gerar_som()

        #if self.contador_dano > fps * 1:
         #   self.dano = False
          #  self.contador_dano = 0

        #self.animar_sprite()

        # Inverter direção após percorrer 100px
        #if self.rect.x > 20:
       #     self.x_vel = -self.velocidade_inimigo
      #  else:
      #      self.x_vel = self.velocidade_inimigo

   # def inicializar_inimigo(self, janela, offset_x):
    #    janela.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))

   # def atualizar_inimigo(self):
     #   self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
     #   self.mask = pygame.mask.from_surface(self.sprite)

    #def gerar_som(self):
     #   audio = pygame.mixer.Sound(join("Soms", "pulo.mp3"))
     #   audio.set_volume(3)
     #   audio.play(loops=0)

    def mover(self, distancia_x, distancia_y):
        self.rect.x += distancia_x
        self.rect.y += distancia_y

    def mover_esquerda(self, vel):
        self.x_vel = -vel
        if self.direcao != "esquerda":
            self.direcao = "esquerda"
            self.contador_animacao = 0

    def mover_direita(self, vel):
        self.x_vel = vel
        if self.direcao != "direita":
            self.direcao = "direita"
            self.contador_animacao = 0

    def loop_inimigo(self, fps=60):
        self.y_vel += min(1, (self.velocidade_de_caida/fps) * self.gravidade)
        self.mover(self.x_vel, self.y_vel)


        self.animar_sprite()
        self.velocidade_de_caida += 1

    def inicializar_inimigo(self, janela, offset_x):
        janela.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))

    def movimentar_inimigo(self, jogador, objeto):
        tecla = pygame.key.get_pressed()

        self.x_vel = 0
        colicao_esquerda = self.colicao_horizontal(
            jogador, objeto, -self.velocidade_inimigo*2)
        colicao_direita = self.colicao_horizontal(
            jogador, objeto, self.velocidade_inimigo*2)

        if tecla[pygame.K_LEFT] and not colicao_esquerda:
            self.mover_esquerda(self.velocidade_inimigo)
        elif tecla[pygame.K_RIGHT] and not colicao_direita:
            self.mover_direita(self.velocidade_inimigo)

        colicao_vertical = self.colicao_vertical(jogador, objeto, self.y_vel)
        checar = [colicao_esquerda, colicao_direita, *colicao_vertical]
       


    def atualizar_jogador(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def gerar_som(self):
        audio = pygame.mixer.Sound(join("Soms", "pulo.mp3"))
        audio.set_volume(3)
        audio.play(loops=0)



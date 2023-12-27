import pygame
from os.path import isfile, join
from os import listdir
from colicao import Mixin_colicao


class SpriteJogo(pygame.sprite.Sprite,Mixin_colicao):
    def __init__(self):
        self.direcao = "esquerda"
        self.contador_animacao = 0
        self.delei_animacao = 3

    def inverter(self,sprites):
        return [pygame.transform.flip(sprite,True,False) for sprite in sprites]

    
    def carregar_sprite(self,diretorio1,diretorio2,largura,altura,direcao = False):
        caminho = join("assets",diretorio1,diretorio2)
        imagems = [f for f in listdir(caminho) if isfile(join(caminho,f))]

        todos_os_sprites = {}


        for imagem in imagems:
            folha_sprite = pygame.image.load(join(caminho,imagem)).convert_alpha()

            sprite = []

            for i in range(folha_sprite.get_width()//largura):
                superfice = pygame.Surface((largura,altura),pygame.SRCALPHA,32)
                rect = pygame.Rect(i * largura,0,largura,altura)
                superfice.blit(folha_sprite,(0,0),rect)
                sprite.append(pygame.transform.scale2x(superfice))

            if direcao:
                todos_os_sprites[imagem.replace(".png","")+"_direita"] = sprite
                todos_os_sprites[imagem.replace(".png","")+"_esquerda"] = self.inverter(sprite)
            else:
                todos_os_sprites[imagem.replace(".png","")] = sprite

        return todos_os_sprites
    
    def animar_sprite(self):
        folha_sprite = "idle"
        if self.dano:
            folha_sprite = "hit"
        elif self.y_vel < 0:
            if self.contador_de_pulo == 1:
                folha_sprite="jump"
            elif self.contador_de_pulo == 2:
                folha_sprite ="double_jump"

        elif self.y_vel > self.gravidade * 2:
            folha_sprite = "fall"

        elif self.x_vel != 0:
            folha_sprite = "run"


        folha_sprite_nome = folha_sprite + "_" + self.direcao
        sprite = self.sprites[folha_sprite_nome]
        caminho_sprite = (self.contador_animacao //
                        self.delei_animacao) % len(sprite)
        self.sprite = sprite[caminho_sprite]
        self.contador_animacao += 1
        self.atualizar_ponto_colizao_jogador()


   

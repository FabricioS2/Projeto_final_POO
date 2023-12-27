import pygame

class Mixin_colicao():
   def atualizar_ponto_colizao_jogador(self):
      self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
      self.mask = pygame.mask.from_surface(self.sprite)

   def pouso(self):
      self.velocidade_de_caida = 0
      self.y_vel = 0
      self.contador_de_pulo = 0

   def colicao_superior(self):
      self.contador = 0
      self.y_vel *= -1


   def colicao_vertical(self,jogador,objetos,cordenada_y):
      colicao_objetos = []
      for obj in objetos:
         if pygame.sprite.collide_mask(jogador,obj):
            if cordenada_y > 0:
               jogador.rect.bottom = obj.rect.top
               jogador.pouso()
            elif cordenada_y < 0:
               jogador.rect.top = obj.rect.bottom
               jogador.colicao_superior()

            colicao_objetos.append(obj)
      return colicao_objetos
   
   def colicao_horizontal(self,jogador,objetos,cordenada_x):
      jogador.mover(cordenada_x,0)
      jogador.atualizar_jogador()
      abjetos_colidindo = None
      for obj in objetos:
         if pygame.sprite.collide_mask(jogador,obj):
            abjetos_colidindo = obj
            break
      jogador.mover(-cordenada_x,0)
      jogador.atualizar_jogador()
      return abjetos_colidindo
      
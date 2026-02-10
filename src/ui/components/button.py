import pygame
class Button:
  def __init__(self, x, y, width, height):
    self.rect = pygame.Rect(x, y, width, height)
  def draw(self, surface):
    # TIP: Si alguna vez necesitas ver dónde están, descomenta esto:
        # pygame.draw.rect(surface, (255, 0, 0), self.rect, width=2)
    pass
  def is_clicked(self, mouse_pos):
    return self.rect.collidepoint(mouse_pos)
#Clase para los botones de las pantallas

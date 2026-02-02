import pygame
from settings.py import Settings
class Menu(): 
  def __init__(self,screen):
    self.screen = screen
    self.fondo = pygame.image.load("Menu.Jpg.jpg.png").convert()
    self.fondo = pygame.transform.scale(self.fondo, (800, 600))
    self.boton_jugar = pygame.Rect(300, 200, 200, 50)
    self.boton_ajustes = pygame.Rect(300, 300, 200, 50)
    self.boton_salir = pygame.Rect(300, 400, 200, 50)
  def ejecutar(self):
class MenuJuego(Menu):
   def __init__(self):
    fondo=Menu.Jpg.jpg
    screen.blit(MenuInGame.jpg, (0, 0))
    pygame.display.flip()
   def Menu(self):
     pass

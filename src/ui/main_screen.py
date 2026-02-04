from ui.base_screen import BaseScreen
from ui.components.button import Button
import pygame
class MainScreen(BaseScreen):
    def __init__(self): 
      self.bg_image = None
      try:
        #self.bg_image = pygame.image.load("assets/images/background_menu.png").convert() poner la imagen basicamente
        pass
      except (FileNotFoundError,pygame.error):
        print("ADVERTENCIA: No se encontró la imagen de fondo. Usando color sólido.")
        self.bg_image = None # Usaremos un color de respaldo
      x_pos = 515
      width = 250
      height = 70
      self.btn_play=Button(x_pos, 280, width, height)
      self.btn_config=Button(x_pos, 370, width, height)
      self.btn_credits = Button(x_pos, 460, width, height)
      self.btn_exit    = Button(x_pos, 550, width, height)
      self.buttons = [self.btn_play, self.btn_config, self.btn_credits, self.btn_exit]
    def update(self,dt):
      #Por ahora no hay nada de darle alguna animacion por pasar el click por encima o de cambiar el color o algo asi, asi que por ahora es innecesario
      pass
    def draw(self,surface):
      surface.fill((0, 105, 148)) 
      for btn in self.buttons:
             pygame.draw.rect(surface, (0, 0, 0), btn.rect, width=2) # Ambas el for y el surface.fill mientras tanto no tenemos la imagen pero cuando la tengamos quito los comentarios de abajo y eso sera
      #if self.bg_image:
            #surface.blit(self.bg_image, (0, 0))
        #else:
            # Color de respaldo (Azul Océano)
            #surface.fill((0, 105, 148))
      for btn in self.buttons:
            btn.draw(surface)
            # Descomenta las siguientes 2 líneas si quieres VER dónde están los botones
            # for btn in self.buttons:
            #     pygame.draw.rect(surface, (255, 0, 0), btn.rect, width=2)
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.btn_play.is_clicked(mouse_pos):
                    return "GOTO_MODES"
                elif self.btn_config.is_clicked(mouse_pos):
                    return "GOTO_CONFIG"
                elif self.btn_credits.is_clicked(mouse_pos):
                    return "GOTO_CREDITS"
                elif self.btn_exit.is_clicked(mouse_pos):
                    return "EXIT"
        return None

import pygame
from src.config.settings import Settings
from ui.base_screen import BaseScreen
from ui.components.button import Button

class CreditsScreen(BaseScreen):
    def __init__(self, screen):
        super().__init__(screen)
        self.fondo = pygame.image.load("src/ui/images/CreditsScreen.jpg").convert() #Imagen de creditos 
        self.fondo = pygame.transform.scale(self.fondo, (self.screen.get_width(), self.screen.get_height())) #para el tamaño
        # Definiendo fuentes
        self.font_title = pygame.font.Font(None, 80)  # Título
        self.font_authors = pygame.font.Font(None, 40) # Nombres
      #de aqui en adelante en init configuracion para los botones
        btn_width = 200
        btn_height = 60
        center_x_btn = (self.screen.get_width() - btn_width) // 2
        pos_y_btn = 500 # Altura aproximada donde está la piedra en la imagen
        self.btn_back = Button(center_x_btn, pos_y_btn, btn_width, btn_height) 
    def handle_events(self, events):
        for event in events:
            # Si intentan cerrar la ventana (X), volvemos al menú
            if event.type == pygame.QUIT:
                return "quit"
            
            # Si hacen clic con el mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.btn_back.is_clicked(event.pos):
                    return "menu" # Volver al menú principal
        return None

    def update(self):
        pass

    def draw(self):
        # 1. Dibujar el fondo
        self.screen.blit(self.fondo, (0, 0))

        # 2. Dibujar el Título "Créditos"
        text_title = self.font_title.render("Créditos", True, (255, 255, 255))
        # Centrado horizontalmente, a 80px desde arriba
        rect_title = text_title.get_rect(center=(self.screen.get_width() // 2, 80))
        self.screen.blit(text_title, rect_title)

        # 3. Dibujar la Lista de Autores (El código la genera desde Settings)
        start_y = 180  # Altura donde empieza el primer nombre
        gap = 50       # Separación entre nombres

        for i, author in enumerate(Settings.AUTHORS):
            # Renderizar nombre en blanco o gris claro
            author_surf = self.font_authors.render(author, True, (240, 240, 240))
            
            # Calcular posición Y para cada uno
            pos_y = start_y + (i * gap)
            
            # Centrar y dibujar
            author_rect = author_surf.get_rect(center=(self.screen.get_width() // 2, pos_y))
            self.screen.blit(author_surf, author_rect)

        # Si es necesario ver el boton despues decomentar la siguiente linea
        # pygame.draw.rect(self.screen, (255, 0, 0), self.btn_back.rect, 2)

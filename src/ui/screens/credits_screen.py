import pygame
from src.config.settings import Settings
from src.managers.asset_manager import AssetManager
from src.ui.base_screen import BaseScreen
from src.ui.components.button import Button

class CreditsScreen(BaseScreen):
    def __init__(self):
        self.bg_image = AssetManager.get_image("bg_credits")

        self.title_font = pygame.font.Font(None, 80)
        self.authors_font = pygame.font.Font(None, 40)

        btn_w, btn_h = 200, 60
        center_x = (Settings.S_WIDTH - btn_w) // 2
        y_pos = 500

        self.back_button = Button(center_x, y_pos, btn_w, btn_h)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button.is_clicked(event.pos):
                    return "GOTO_MENU"

        return None

    def update(self, dt):
        pass

    def draw(self, surface):
        # Dibujar el fondo
        if self.bg_image:
            scaled_bg = pygame.transform.scale(self.bg_image, surface.get_size())
            surface.blit(scaled_bg, (0, 0))
        else:
            # Fondo oscuro de respaldo
            surface.fill((20, 20, 40))

        # Dibujar el Título "Créditos"
        title_surf = self.title_font.render("Créditos", True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(surface.get_width() // 2, 80))
        surface.blit(title_surf, title_rect)

        # Dibujar la Lista de Autores (El código la genera desde Settings)
        start_y = 180
        line_spacing = 50

        for i, author in enumerate(Settings.AUTHORS):
            author_surf = self.authors_font.render(author, True, (240, 240, 240))
            pos_y = start_y + (i * line_spacing)
            author_rect = author_surf.get_rect(center=(surface.get_width() // 2, pos_y))
            surface.blit(author_surf, author_rect)

        self.back_button.draw(surface)
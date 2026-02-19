import pygame

from src.config.settings import Settings

from src.managers.asset_manager import AssetManager

from src.ui.base_screen import BaseScreen
from src.ui.components.button import Button

class CreditsScreen(BaseScreen):
    def __init__(self):
        self.bg_image = AssetManager.get_image("main_bg")
        
        screen_w = Settings.S_WIDTH
        screen_h = Settings.S_HEIGHT

        center_x = screen_w // 2
        start_y = 200
        btn_w, btn_h = 250, 70
        line_spacing = 60

        font_path = AssetManager.get_font("title_font")
        if font_path:
            self.title_font = pygame.font.Font(font_path, 80)
            self.authors_font = pygame.font.Font(font_path, 40)
        else:
            self.title_font = pygame.font.SysFont("sans-serif", 80, bold=True)
            self.authors_font = pygame.font.SysFont("sans-serif", 40)

        self.title_surf = self.title_font.render("CRÉDITOS", True, (255, 255, 255))
        self.title_rect = self.title_surf.get_rect(center=(center_x, 80))

        self.author_surfaces = []

        for i, author in enumerate(Settings.AUTHORS):
            surf = self.authors_font.render(author, True, (240, 240, 240))
            rect = surf.get_rect(center=(center_x, start_y + (i * line_spacing)))
            self.author_surfaces.append((surf, rect))

        self.back_button = Button(center_x, screen_h - 100, btn_w, btn_h, "VOLVER")

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button.is_clicked(event.pos):
                    return "GOTO_MENU"
                
        return None

    def update(self, dt):
        pass

    def draw(self, surface):
        if self.bg_image:
            scaled_bg = pygame.transform.scale(self.bg_image, surface.get_size())
            surface.blit(scaled_bg, (0, 0))
        else:
            surface.fill((20, 20, 40))

        panel_w, panel_h = 450, 420
        screen_center_x = surface.get_width() // 2
        screen_center_y = surface.get_height() // 2
        
        panel_surf = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
        pygame.draw.rect(panel_surf, (0, 192, 210, 180), panel_surf.get_rect(), border_radius=20)
        
        panel_rect = panel_surf.get_rect(center=(screen_center_x, screen_center_y - 40))
        surface.blit(panel_surf, panel_rect)

        self.title_rect.center = (screen_center_x, panel_rect.top + 60)
        surface.blit(self.title_surf, self.title_rect)

        authors_start_y = panel_rect.top + 150
        line_spacing = 65
        
        for i, (surf, rect) in enumerate(self.author_surfaces):
            rect.center = (screen_center_x, authors_start_y + (i * line_spacing))
            surface.blit(surf, rect)

        self.back_button.draw(surface)
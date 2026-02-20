import pygame

from src.config.settings import Settings

from src.managers.asset_manager import AssetManager

from src.ui.base_screen import BaseScreen
from src.ui.components.button import Button

class ModesScreen(BaseScreen):
    def __init__(self):
        self.bg_image = AssetManager.get_image("main_bg")
        
        screen_w = Settings.S_WIDTH
        screen_h = Settings.S_HEIGHT

        center_x = screen_w // 2
        center_y = screen_h // 2
        btn_w, btn_h = 250, 70
        spacing = 90
        
        panel_w, panel_h = 450, 450
        panel_y_start = (screen_h - panel_h) // 2 - 50
        
        start_y = panel_y_start + 180

        font_path = AssetManager.get_font("title_font")
        self.title_font = pygame.font.Font(font_path, 70) if font_path else pygame.font.SysFont("sans-serif", 70, bold=True)
        self.title_surf = self.title_font.render("DIFICULTAD", True, (255, 255, 255))
        self.title_rect = self.title_surf.get_rect()

        self.buttons = {
            "EASY":   Button(center_x, start_y, btn_w, btn_h, "FÁCIL"),
            "MEDIUM": Button(center_x, start_y + spacing, btn_w, btn_h, "NORMAL"),
            "HARD":   Button(center_x, start_y + (spacing * 2), btn_w, btn_h, "DIFÍCIL"),
            "BACK":   Button(center_x, screen_h - 100, btn_w, btn_h, "VOLVER")
        }

    def handle_events(self, events):
        event_map = {
            "EASY": "START_EASY",
            "MEDIUM": "START_MEDIUM",
            "HARD": "START_HARD",
            "BACK": "GOTO_MENU"
        }

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for key, button in self.buttons.items():
                    if button.is_clicked(mouse_pos):
                        return event_map.get(key)
                    
        return None

    def update(self, dt):
        pass

    def draw(self, surface):
        if self.bg_image:
            scaled_bg = pygame.transform.scale(self.bg_image, surface.get_size())
            surface.blit(scaled_bg, (0, 0))
        else:
            surface.fill((10, 40, 70))

        panel_w, panel_h = 450, 450
        screen_center_x = surface.get_width() // 2
        screen_center_y = surface.get_height() // 2
        
        panel_surf = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
        pygame.draw.rect(panel_surf, (0, 192, 210, 180), panel_surf.get_rect(), border_radius=25)
        
        panel_rect = panel_surf.get_rect(center=(screen_center_x, screen_center_y - 50))
        surface.blit(panel_surf, panel_rect)

        self.title_rect.center = (screen_center_x, panel_rect.top + 70)
        surface.blit(self.title_surf, self.title_rect)

        for button in self.buttons.values():
            button.draw(surface)
import pygame

from src.config.settings import Settings

from src.managers.asset_manager import AssetManager

from src.ui.base_screen import BaseScreen
from src.ui.components.button import Button

class MainScreen(BaseScreen):
    def __init__(self):
        self.bg_image = AssetManager.get_image("main_bg")

        screen_w = Settings.S_WIDTH
        screen_h = Settings.S_HEIGHT

        center_x = screen_w // 2
        start_y = screen_h // 2
        btn_w, btn_h = 250, 70
        spacing = 90

        self.title_text = Settings.TITLE.upper()
        font_path = AssetManager.get_font("title_font")

        if font_path:
            self.title_font = pygame.font.Font(font_path, 90)
        else:
            self.title_font = pygame.font.SysFont("sans-serif", 90, bold=True)
            
        self.title_surf = self.title_font.render(self.title_text, True, (255, 255, 255))
        self.title_rect = self.title_surf.get_rect(center=(center_x, screen_h // 4))

        self.buttons = {
            "PLAY": Button(center_x, start_y, btn_w, btn_h, "JUGAR"),
            "INSTRUCTIONS": Button(center_x, start_y + spacing, btn_w, btn_h, "INSTRUCCIONES"),
            "CREDITS": Button(center_x, start_y + (spacing * 2), btn_w, btn_h, "CRÉDITOS"),
            "EXIT": Button(center_x, start_y + (spacing * 3), btn_w, btn_h, "SALIR"),
        }

    def handle_events(self, events):
        event_map = {
            "PLAY": "GOTO_MODES",
            "INSTRUCTIONS": "GOTO_INSTR",
            "CREDITS": "GOTO_CREDITS",
            "EXIT": "EXIT",
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
            surface.fill((0, 105, 148))

        surface.blit(self.title_surf, self.title_rect)

        for button in self.buttons.values():
            button.draw(surface)
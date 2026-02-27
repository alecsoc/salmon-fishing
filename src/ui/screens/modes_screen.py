import pygame

from src.config.settings import Settings

from src.managers.asset_manager import AssetManager

from src.ui.base_screen import BaseScreen
from src.ui.components.button import Button
from src.ui.components.text_label import TextLabel

class ModesScreen(BaseScreen):
    def __init__(self):
        self.bg_image = AssetManager.get_image("main_bg")
        
        screen_w = Settings.S_WIDTH
        screen_h = Settings.S_HEIGHT

        center_x = screen_w // 2
        start_y = screen_h // 2 - 50
        spacing = 95

        self.title_label = TextLabel(
            x=center_x,
            y=screen_h // 4,
            text="SELECCIONA DIFICULTAD",
            font_key="primary_font",
            font_size=70
        )

        self.buttons = {
            "EASY": Button(center_x, start_y, 300, 80, "FÁCIL"),
            "MEDIUM": Button(center_x, start_y + spacing, 300, 80, "INTERMEDIO"),
            "HARD": Button(center_x, start_y + (spacing * 2), 300, 80, "DIFÍCIL"),
            "BACK": Button(center_x, screen_h - 100, 200, 60, "VOLVER")
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
                for key, button in self.buttons.items():
                    if button.is_clicked(event.pos):
                        return event_map.get(key)
                    
        return None
    
    def update(self, dt):
        return super().update(dt)

    def draw(self, surface):
        if self.bg_image:
            scaled_bg = pygame.transform.scale(self.bg_image, surface.get_size())
            surface.blit(scaled_bg, (0, 0))
        else:
            surface.fill((0, 80, 120))

        self.title_label.draw(surface)

        for button in self.buttons.values():
            button.draw(surface)
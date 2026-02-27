import pygame

from src.config.settings import Settings

from src.managers.asset_manager import AssetManager

from src.ui.base_screen import BaseScreen
from src.ui.components.button import Button
from src.ui.components.text_label import TextLabel

class CreditsScreen(BaseScreen):
    def __init__(self):
        self.bg_image = AssetManager.get_image("main_bg")
        
        screen_w = Settings.S_WIDTH
        screen_h = Settings.S_HEIGHT
        center_x = screen_w // 2
        
        panel_y_center = screen_h // 2 - 40
        authors_start_y = panel_y_center - 60
        line_spacing = 65

        self.title_label = TextLabel(
            x=center_x,
            y=panel_y_center - 150,
            text="CRÉDITOS",
            font_key="primary_font",
            font_size=60,
            color=Settings.COLORS["WHITE"]
        )

        self.author_labels = []
        for i, author in enumerate(Settings.AUTHORS):
            label = TextLabel(
                x=center_x,
                y=authors_start_y + (i * line_spacing),
                text=author,
                font_key="secondary_font",
                font_size=30,
                color=(240, 240, 240)
            )

            self.author_labels.append(label)

        self.back_button = Button(center_x, screen_h - 100, 250, 70, "VOLVER")

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button.is_clicked(event.pos):
                    return "GOTO_MENU"
                
        return None
    
    def update(self, dt):
        return super().update(dt)

    def draw(self, surface):
        if self.bg_image:
            scaled_bg = pygame.transform.scale(self.bg_image, surface.get_size())
            surface.blit(scaled_bg, (0, 0))
        else:
            surface.fill((20, 20, 40))

        panel_w, panel_h = 450, 420
        panel_surf = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
        pygame.draw.rect(panel_surf, Settings.COLORS["PANEL_COLOR"], panel_surf.get_rect(), border_radius=20)
        
        panel_rect = panel_surf.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2 - 40))
        surface.blit(panel_surf, panel_rect)

        self.title_label.draw(surface)

        for label in self.author_labels:
            label.draw(surface)

        self.back_button.draw(surface)
import pygame

from src.config.settings import Settings

from src.managers.asset_manager import AssetManager

from src.ui.base_screen import BaseScreen
from src.ui.components.button import Button
from src.ui.components.text_label import TextLabel

class ResultsScreen(BaseScreen):
    def __init__(self, score=0):
        self.bg_image = AssetManager.get_image("main_bg")
        self.final_score = score
        
        screen_w = Settings.S_WIDTH
        screen_h = Settings.S_HEIGHT

        center_x = screen_w // 2
        panel_y_center = screen_h // 2 - 20

        rank_letter, rank_color, rank_title = self._get_rank_data()

        self.title_label = TextLabel(
            x=center_x,
            y=panel_y_center - 130,
            text="RESULTADOS DE PESCA",
            font_key="primary_font",
            font_size=45,
            color=Settings.COLORS["WHITE"]
        )

        self.score_label = TextLabel(
            x=center_x,
            y=panel_y_center - 60,
            text=f"PUNTOS: {self.final_score}",
            font_key="secondary_font",
            font_size=32,
            color=(240, 240, 240)
        )

        self.rank_label = TextLabel(
            x=center_x,
            y=panel_y_center + 20,
            text=rank_letter,
            font_key="primary_font",
            font_size=110,
            color=rank_color
        )

        self.rank_title_label = TextLabel(
            x=center_x,
            y=panel_y_center + 100,
            text=rank_title,
            font_key="secondary_font",
            font_size=28,
            color=rank_color
        )

        self.back_button = Button(center_x, screen_h - 100, 250, 70, "VOLVER")

    def _get_rank_data(self):
        s = self.final_score

        if s >= 6000: return "S+", Settings.COLORS["WHITE"], "SEÑOR DE TODOS LOS SALMONES"
        if s >= 4000: return "S", Settings.COLORS["GOLD"], "MAESTRO DE LAS MAREAS"
        if s >= 2000: return "A", Settings.COLORS["AQUA"], "PESCADOR DE ÉLITE"
        if s >= 1000: return "B", Settings.COLORS["PASTEL_GREEN"], "ARPÓN AUDAZ"
        if s >= 500:  return "C", Settings.COLORS["PASTEL_ORANGE"], "AFICIONADO CON RED"

        return "D", Settings.COLORS["PASTEL_RED"], "CARNADA DE TIBURÓN"

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

        panel_w, panel_h = Settings.S_WIDTH // 1.6, Settings.S_HEIGHT // 2.0
        panel_surf = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
        pygame.draw.rect(panel_surf, Settings.COLORS["PANEL_COLOR"], panel_surf.get_rect(), border_radius=25)
        
        panel_rect = panel_surf.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2 - 20))
        surface.blit(panel_surf, panel_rect)

        self.title_label.draw(surface)
        self.score_label.draw(surface)
        self.rank_label.draw(surface)
        self.rank_title_label.draw(surface)
        self.back_button.draw(surface)
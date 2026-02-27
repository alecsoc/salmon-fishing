import pygame

from src.config.settings import Settings

from src.managers.asset_manager import AssetManager

from src.ui.base_screen import BaseScreen
from src.ui.components.button import Button
from src.ui.components.text_label import TextLabel

class InstructionsScreen(BaseScreen):
    def __init__(self):
        self.bg_image = AssetManager.get_image("main_bg")
        
        screen_w = Settings.S_WIDTH
        screen_h = Settings.S_HEIGHT
        center_x = screen_w // 2
        
        panel_y_center = screen_h // 1.75 - 20

        self.title_label = TextLabel(
            x=center_x,
            y=panel_y_center - 200,
            text="CÓMO JUGAR",
            font_key="primary_font",
            font_size=55,
            color=Settings.COLORS["WHITE"]
        )

        instructions = [
            "1. Mira el color del pez objetivo en la nube.",
            "2. Usa la LINTERNA para revelar a los peces.",
            "3. Clica solo los del color correcto en el objetivo (+100).",
            "4. Colores incorrectos restan puntos (-100).",
            "5. Usa el SONAR (barra inferior de carga) para revelarlos todos."
        ]

        self.instruction_labels = []
        line_spacing = 50
        start_y = panel_y_center - 110

        for i, text in enumerate(instructions):
            label = TextLabel(
                x=center_x,
                y=start_y + (i * line_spacing),
                text=text,
                font_key="secondary_font",
                font_size=24,
                color=(230, 230, 230)
            )

            self.instruction_labels.append(label)

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

        panel_w, panel_h = Settings.S_WIDTH // 1.5, Settings.S_HEIGHT // 1.75
        panel_surf = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
        pygame.draw.rect(panel_surf, Settings.COLORS["PANEL_COLOR"], panel_surf.get_rect(), border_radius=25)
        
        panel_rect = panel_surf.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2 - 20))
        surface.blit(panel_surf, panel_rect)

        self.title_label.draw(surface)

        for label in self.instruction_labels:
            label.draw(surface)

        self.back_button.draw(surface)
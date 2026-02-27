import pygame

from src.config.settings import Settings

from src.managers.asset_manager import AssetManager

class TextLabel:
    def __init__(
        self,
        x,
        y,
        text="",
        color=Settings.COLORS["WHITE"],
        font_key="secondary_font",
        font_size=40,
        alpha=None,
        border=None # (Color, Thickness, Padding, Radius)
    ):
        self.x, self.y = x, y
        self.text = text
        self.color = color
        self.font_size = font_size
        self.font_key = font_key
        self.alpha = alpha
        self.border = border

        self.font = self._load_custom_font(self.font_key, self.font_size)
        self.image = None
        self.rect = pygame.Rect(x, y, 0, 0)
        
        self._render_surface()

    def _load_custom_font(self, key, size):
        try:
            font_path = AssetManager.get_font(key)
            if font_path:
                return pygame.font.Font(font_path, size)
        except Exception as e:
            print(f"Error al cargar la fuente {key}: {e}")

        return pygame.font.SysFont("sans-serif", size)

    def _render_surface(self):
        self.image = self.font.render(self.text, True, self.color)

        if self.alpha is not None:
            self.image.set_alpha(self.alpha)

        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update_text(self, new_text):
        if self.text != new_text:
            self.text = new_text
            self._render_surface()

    def draw(self, surface):
        if self.border:
            border_color, thickness, padding, radius = self.border
            border_rect = self.rect.inflate(padding * 2, padding * 2)

            pygame.draw.rect(
                surface,
                border_color,
                border_rect,
                width=thickness,
                border_radius=radius,
            )

        surface.blit(self.image, self.rect)

import pygame

from src.config.settings import Settings

from src.managers.asset_manager import AssetManager
from src.managers.sound_player import SoundPlayer

class Button:
    def __init__(
        self, 
        x, 
        y, 
        width, 
        height, 
        text="", 
        image_key=None, 
        font_key="secondary_font", 
        font_size=25, 
        text_color=Settings.COLORS["WHITE"]
    ):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)
        self.text = text
        self.text_color = text_color
        self.image = None
        self.font = self._load_custom_font(font_key, font_size)

        if image_key:
            raw = AssetManager.get_image(image_key)

            if raw:
                self.image = pygame.transform.scale(raw, (width, height))

    def _load_custom_font(self, key, size):
        try:
            path = AssetManager.get_font(key)

            if path:
                return pygame.font.Font(path, size)
        except Exception:
            pass

        return pygame.font.SysFont("Verdana", size, bold=True)

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = self.rect.collidepoint(mouse_pos)
        
        alpha = 170 if is_hovered else 255

        if self.image:
            temp_image = self.image.copy()
            temp_image.set_alpha(alpha)
            surface.blit(temp_image, self.rect)
        else:
            s = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
            pygame.draw.rect(s, (*Settings.COLORS["BUTTON_COLOR"], alpha), s.get_rect(), border_radius=12)
            pygame.draw.rect(s, (*Settings.COLORS["WHITE"], alpha), s.get_rect(), width=3, border_radius=12)
            surface.blit(s, self.rect.topleft)

        if self.text:
            text_surf = self.font.render(self.text, True, self.text_color)
            text_surf.set_alpha(alpha)
            surface.blit(text_surf, text_surf.get_rect(center=self.rect.center))

    def is_clicked(self, pos):
        if self.rect.collidepoint(pos):
            SoundPlayer.play_sfx("choose")
            return True
        return False
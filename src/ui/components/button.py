import pygame

from src.managers.asset_manager import AssetManager

class Button:
    def __init__(self, x, y, width, height, text="", image_key=None, font_key=None, font_size=30, text_color=(255, 255, 255)):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)
        self.text = text
        self.text_color = text_color
        
        self.image = None
        if image_key:
            try:
                raw_image = AssetManager.get_image(image_key)
                if raw_image:
                    self.image = pygame.transform.scale(raw_image, (width, height))
            except Exception as e:
                print(f"Error al cargar la imagen del botón: {e}")

        self.font = self._load_custom_font(font_key, font_size)

    def _load_custom_font(self, key, size):
        try:
            font_path = AssetManager.get_font(key)
            if font_path:
                return pygame.font.Font(font_path, size)
        except Exception as e:
            print(f"Error al cargar la fuente {key}: {e}")
        return pygame.font.SysFont("sans-serif", size)

    def draw(self, surface):
        if self.image:
            surface.blit(self.image, self.rect)
        else:
            pygame.draw.rect(surface, (0, 192, 210), self.rect, border_radius=10)
            pygame.draw.rect(surface, (255, 255, 255), self.rect, width=4, border_radius=10)

        if self.text:
            text_surf = self.font.render(self.text, True, self.text_color)
            text_rect = text_surf.get_rect(center=self.rect.center)
            surface.blit(text_surf, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
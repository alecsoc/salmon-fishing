import pygame

from src.config.settings import Settings

class HUDElement:
    def __init__(self):
        font_label = Settings.FONTS.get("hud_label")
        font_value = Settings.FONTS.get("hud_value")
        
        self.font_label = font_label if font_label is not None else pygame.font.SysFont("Arial", 22, bold=True)
        self.font_value = font_value if font_value is not None else pygame.font.SysFont("Arial", 32, bold=True)
            
        self.panel_color = Settings.COLORS["GRAY_ALPHA"]

class Score(HUDElement):
    def __init__(self, x=20, y=20):
        super().__init__()
        self.rect = pygame.Rect(x, y, 220, 80)
        self.score = 0
        self._render_texts()

    def _render_texts(self):
        self.lbl_surf = self.font_label.render("SCORE", True, Settings.COLORS["PASTEL_YELLOW"])
        self.val_surf = self.font_value.render(str(self.score), True, Settings.COLORS["PASTEL_ORANGE"])

    def update_score(self, new_score):
        self.score = new_score
        self._render_texts()

    def draw(self, surface):
        panel = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(panel, self.panel_color, panel.get_rect(), border_radius=15)
        surface.blit(panel, self.rect.topleft)
        pygame.draw.rect(surface, Settings.COLORS["WHITE"], self.rect, 2, border_radius=15)
        
        surface.blit(self.lbl_surf, (self.rect.x + 15, self.rect.y + 10))
        surface.blit(self.val_surf, (self.rect.x + 15, self.rect.y + 35))

class Timer(HUDElement):
    def __init__(self, x=None, y=20):
        super().__init__()
        self.width = 180
        self.x = x if x else Settings.S_WIDTH - self.width - 20
        self.rect = pygame.Rect(self.x, y, self.width, 80)
        self.game_time = 0

    def update(self, dt_time):
        self.game_time = dt_time

    def draw(self, surface):
        panel = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(panel, self.panel_color, panel.get_rect(), border_radius=15)
        surface.blit(panel, self.rect.topleft)
        pygame.draw.rect(surface, Settings.COLORS["WHITE"], self.rect, 2, border_radius=15)

        time_color = Settings.COLORS["PASTEL_RED"] if self.game_time <= 10 else Settings.COLORS["PASTEL_BLUE"]
        
        minutes = int(self.game_time) // 60
        seconds = int(self.game_time) % 60
        time_str = f"{minutes:02}:{seconds:02}"
        
        lbl_surf = self.font_label.render("TIME", True, Settings.COLORS["PASTEL_YELLOW"])
        val_surf = self.font_value.render(time_str, True, time_color)
        
        surface.blit(lbl_surf, (self.rect.x + 15, self.rect.y + 10))
        surface.blit(val_surf, (self.rect.x + 15, self.rect.y + 35))

class TargetDisplay:
    def __init__(self, assets):
        self.assets = assets
        self.rect = pygame.Rect(Settings.S_WIDTH // 2 - 60, 20, 120, 90)

    def draw(self, surface, target_color_name, target_color_rgb):
        cloud_img = self.assets.get("thought_cloud")
        if cloud_img:
            surface.blit(cloud_img, self.rect.topleft)
        else:
            pygame.draw.ellipse(surface, Settings.COLORS["WHITE"], self.rect)
            pygame.draw.ellipse(surface, (200, 200, 200), self.rect, 2)
        
        fish_key = f"{target_color_name}_fish"
        fish_img = self.assets.get(fish_key)
        
        if fish_img:
            fish_rect = fish_img.get_rect(center=self.rect.center)
            surface.blit(fish_img, fish_rect)
        else:
            body_rect = pygame.Rect(0, 0, 50, 25)
            body_rect.center = self.rect.center
            pygame.draw.rect(surface, target_color_rgb, body_rect, border_radius=8)
            pygame.draw.rect(surface, (50, 50, 50), body_rect, 2, border_radius=8)
            
            eye_pos = (body_rect.right - 10, body_rect.centery - 5)
            pygame.draw.circle(surface, Settings.COLORS["WHITE"], eye_pos, 4)
            
            tail_points = [
                (body_rect.left, body_rect.centery),
                (body_rect.left - 10, body_rect.top),
                (body_rect.left - 10, body_rect.bottom)
            ]
            pygame.draw.polygon(surface, target_color_rgb, tail_points)
            pygame.draw.polygon(surface, (50, 50, 50), tail_points, 2)

class ComboCounter:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 40, bold=True)
        self.combo = 0
        self.scale = 1.0

    def add(self):
        self.combo += 1
        self.scale = 1.5

    def reset(self):
        self.combo = 0

    def update(self):
        if self.scale > 1.0:
            self.scale -= 0.05

    def draw(self, surface):
        if self.combo > 1:
            text = f"¡{self.combo} SALMONES!"
            surf = self.font.render(text, True, Settings.COLORS["PASTEL_YELLOW"])
            if self.scale > 1.0:
                new_size = (int(surf.get_width() * self.scale), int(surf.get_height() * self.scale))
                surf = pygame.transform.scale(surf, new_size)
            
            rect = surf.get_rect(center=(Settings.S_WIDTH // 2, Settings.S_HEIGHT - 120))
            surface.blit(surf, rect)

class GameBanner:
    def __init__(self, text):
        self.font = pygame.font.SysFont("Arial", 60, bold=True)
        self.text = text
        self.rect = pygame.Rect(0, 0, Settings.S_WIDTH, 150)
        self.rect.center = (Settings.S_WIDTH // 2, Settings.S_HEIGHT // 2)

    def draw(self, surface):
        overlay = pygame.Surface((Settings.S_WIDTH, Settings.S_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        surface.blit(overlay, (0,0))

        pygame.draw.rect(surface, Settings.COLORS["PASTEL_RED"], self.rect)
        pygame.draw.rect(surface, Settings.COLORS["WHITE"], self.rect, 5)
        
        text_surf = self.font.render(self.text, True, Settings.COLORS["WHITE"])
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
import pygame

from src.config.settings import Settings

from src.ui.components.text_label import TextLabel

class HUDElement:
    def __init__(self):
        self.panel_color = Settings.COLORS["GRAY_ALPHA"]

class Score(HUDElement):
    def __init__(self, x=20, y=20):
        super().__init__()
        self.rect = pygame.Rect(x, y, 200, 100)
        self.score = 0
        self.lbl_label = TextLabel(
            x + 15, y + 30, "SCORE",
            font_key="primary_font",
            color=Settings.COLORS["PASTEL_YELLOW"], 
            font_size=22
        )

        self.val_label = TextLabel(
            x + 15, y + 65, str(self.score),
            font_key="primary_font",
            color=Settings.COLORS["PASTEL_ORANGE"], 
            font_size=32
        )

        self._align_labels()

    def _align_labels(self):
        self.lbl_label.rect.left = self.rect.x + 15
        self.val_label.rect.left = self.rect.x + 15

    def update_score(self, new_score):
        self.score = new_score
        self.val_label.update_text(str(self.score))
        self._align_labels()

    def draw(self, surface):
        panel = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(panel, self.panel_color, panel.get_rect(), border_radius=15)

        surface.blit(panel, self.rect.topleft)
        pygame.draw.rect(surface, Settings.COLORS["WHITE"], self.rect, 3, border_radius=15)
        
        self.lbl_label.draw(surface)
        self.val_label.draw(surface)

class Timer(HUDElement):
    def __init__(self, x=None, y=20):
        super().__init__()
        self.width = 200
        self.x = x if x else Settings.S_WIDTH - self.width - 20
        self.rect = pygame.Rect(self.x, y, self.width, 100)
        self.game_time = 0

        self.lbl_label = TextLabel(
            self.x + 15, y + 30, "TIME",
            font_key="primary_font",
            color=Settings.COLORS["PASTEL_YELLOW"], 
            font_size=22
        )

        self.val_label = TextLabel(
            self.x + 15, y + 65, "00:00",
            font_key="primary_font",
            color=Settings.COLORS["PASTEL_BLUE"], 
            font_size=32
        )

        self._align_labels()

    def _align_labels(self):
        self.lbl_label.rect.left = self.rect.x + 15
        self.val_label.rect.left = self.rect.x + 15

    def update(self, dt):
        self.game_time = dt

        minutes = int(self.game_time) // 60
        seconds = int(self.game_time) % 60
        time_str = f"{minutes:02}:{seconds:02}"
        
        time_color = Settings.COLORS["PASTEL_RED"] if self.game_time <= 10 else Settings.COLORS["PASTEL_BLUE"]

        self.val_label.color = time_color
        self.val_label.update_text(time_str)
        self._align_labels()

    def draw(self, surface):
        panel = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(panel, self.panel_color, panel.get_rect(), border_radius=15)

        surface.blit(panel, self.rect.topleft)
        pygame.draw.rect(surface, Settings.COLORS["WHITE"], self.rect, 3, border_radius=15)

        self.lbl_label.draw(surface)
        self.val_label.draw(surface)

class TargetDisplay:
    def __init__(self, assets):
        self.assets = assets
        self.rect = pygame.Rect(Settings.S_WIDTH // 2 - 75, 20, 180, 120)
        self.cloud_surf = None
        
        self._prepare_cloud()

    def _prepare_cloud(self):
        raw = self.assets.get("thought_cloud")

        if raw:
            self.cloud_surf = pygame.transform.scale(raw, (self.rect.width, self.rect.height)).convert_alpha()

    def draw(self, surface, target_color_name, target_color_rgb):
        if self.cloud_surf:
            shadow = self.cloud_surf.copy()
            shadow.fill((0, 0, 0, 100), special_flags=pygame.BLEND_RGBA_MULT)
            surface.blit(shadow, (self.rect.x + 3, self.rect.y + 3))
            surface.blit(self.cloud_surf, self.rect.topleft)
        else:
            pygame.draw.ellipse(surface, Settings.COLORS["WHITE"], self.rect)
            pygame.draw.ellipse(surface, (50, 50, 50), self.rect, 3)
        
        fish_key = f"{target_color_name}_fish"
        raw_fish = self.assets.get(fish_key)
        
        if raw_fish:
            f_w, f_h = 95, 40
            scaled_fish = pygame.transform.scale(raw_fish, (f_w, f_h)).convert_alpha()
            f_rect = scaled_fish.get_rect(center=self.rect.center)
            f_rect.centery -= 8
            surface.blit(scaled_fish, f_rect)
        else:
            body = pygame.Rect(0, 0, 60, 30)
            body.center = self.rect.center
            body.centery -= 8
            pygame.draw.rect(surface, target_color_rgb, body, border_radius=10)
            pygame.draw.rect(surface, (50, 50, 50), body, 2, border_radius=10)

class ComboCounter:
    def __init__(self):
        self.combo = 0
        self.scale = 1.0

        self.label = TextLabel(
            Settings.S_WIDTH // 2, Settings.S_HEIGHT - 120, "",
            font_key="primary_font",
            color=Settings.COLORS["PASTEL_ORANGE"], 
            font_size=40
        )

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
            self.label.update_text(text)
        
            if self.label.image is None:
                return

            if self.scale > 1.0:
                img = self.label.image
                new_size = (int(img.get_width() * self.scale), int(img.get_height() * self.scale))
                scaled_surf = pygame.transform.scale(img, new_size)
                rect = scaled_surf.get_rect(center=(Settings.S_WIDTH // 2, Settings.S_HEIGHT - 120))
                surface.blit(scaled_surf, rect)
            else:
                self.label.draw(surface)

class GameBanner:
    def __init__(self, text):
        self.text = text
        self.rect = pygame.Rect(0, 0, Settings.S_WIDTH, 150)
        self.rect.center = (Settings.S_WIDTH // 2, Settings.S_HEIGHT // 2)

        self.label = TextLabel(
            self.rect.centerx, self.rect.centery, self.text,
            font_key="primary_font",
            color=Settings.COLORS["WHITE"], 
            font_size=60
        )

    def draw(self, surface):
        overlay = pygame.Surface((Settings.S_WIDTH, Settings.S_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        surface.blit(overlay, (0,0))

        pygame.draw.rect(surface, Settings.COLORS["PASTEL_RED"], self.rect)
        pygame.draw.rect(surface, Settings.COLORS["WHITE"], self.rect, 5)
        
        self.label.draw(surface)
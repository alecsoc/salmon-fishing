import math
import pygame

from src.config.settings import Settings

class Sonar:
    def __init__(self):
        self.cycle_duration = Settings.SONAR_CYCLE_DURATION
        self.active_duration = Settings.SONAR_ACTIVE_DURATION
        self.timer = 0.0
        self.is_active = False
        self.progress = 0.0
        self.alpha = 0

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.cycle_duration:
            self.timer = 0.0
        
        self.progress = self.timer / self.cycle_duration
        
        time_until_end = self.cycle_duration - self.timer

        if time_until_end <= self.active_duration:
            normalized = time_until_end / self.active_duration
            self.alpha = int(math.sin(normalized * math.pi) * 255)
        else:
            self.alpha = 0

    def draw_bar(self, surface):
        bar_w, bar_h = Settings.S_WIDTH - 80, 15
        x, y = 40, Settings.S_HEIGHT - 40
        
        bg_rect = pygame.Rect(x, y, bar_w, bar_h)
        pygame.draw.rect(surface, Settings.COLORS["GRAY_ALPHA"], bg_rect, border_radius=7)
        
        fill_w = bar_w * self.progress
        fill_rect = pygame.Rect(x, y, fill_w, bar_h)
        pygame.draw.rect(surface, Settings.COLORS["PASTEL_TEAL"], fill_rect, border_radius=7)
        
        pygame.draw.rect(surface, Settings.COLORS["WHITE"], bg_rect, 2, border_radius=7)
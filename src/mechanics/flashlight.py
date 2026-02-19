import pygame

from src.config.settings import Settings
from src.config.game_modes import MODES, ACTUAL_MODE

class Flashlight:
    def __init__(self):
        self.base_radius = Settings.FLASHLIGHT_RADIUS_BASE
        self.multiplier = MODES[ACTUAL_MODE]["flashlight_mult"]
        self.radius = self.base_radius * self.multiplier
        self.pos = (0, 0)
        self.inner_radius = 5

    def update(self, mouse_pos):
        self.pos = mouse_pos

    def draw(self, surface):
        pygame.draw.circle(surface, Settings.COLORS["PASTEL_YELLOW"], self.pos, self.radius, 4)
        pygame.draw.circle(surface, Settings.COLORS["PASTEL_YELLOW"], self.pos, self.inner_radius, 2)
import random
import pygame
from src.config.settings import Settings

class Fish:
    def __init__(self, x, y, speed, fish_image):
        self.image = (
            pygame.transform.flip(fish_image, True, False)
            if self.speed < 0
            else fish_image
        )

        self.rect = self.image.get_rect(topleft=(x, y))
        self.x = float(x)
        self.y = float(y)
        self.speed = speed

        self.color = random.choice(
            [
                Settings.COLORS["RED_COLOR"],
                Settings.COLORS["GREEN_COLOR"],
                Settings.COLORS["BLUE_COLOR"],
            ]
        )

    def update_fish_movement(self, dt):
        """Actualiza la posición física del pez según el Delta Time (dt)."""
        self.x += self.speed * dt * 60
        self.rect.x = int(self.x)

    def is_offscreen(self):
        """Verifica si el pez salió de los límites de la pantalla."""
        if self.speed > 0:
            return self.rect.x > Settings.S_WIDTH + Settings.SPAWN_MARGIN
        else:
            return self.rect.x < -Settings.SPAWN_MARGIN - self.rect.width

    def draw(self, surface):
        surface.blit(self.image, self.rect)
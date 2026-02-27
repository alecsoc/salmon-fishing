import random
import pygame
import math

from src.config.settings import Settings

class Fish:
    def __init__(self, x, y, speed, fish_assets, color_type):
        self.speed = speed
        self.x = float(x)
        self.y = float(y)
        self.color_type = color_type
        
        self.is_revealed = False
        self._setup_sprites(fish_assets)
        
        if self.image_hidden:
            self.rect = self.image_hidden.get_rect(topleft=(x, y))
        else:
            self.rect = pygame.Rect(x, y, 60, 30)

    def _setup_sprites(self, assets):
        color_name = "red" if self.color_type == Settings.COLORS["RED_COLOR"] else \
                     "green" if self.color_type == Settings.COLORS["GREEN_COLOR"] else "blue"
        
        img_hidden = assets.get("hidden_fish")
        img_revealed = assets.get(f"{color_name}_fish")

        target_size = (120, 60)

        def process_sprite(img):
            if img:
                scaled = pygame.transform.scale(img, target_size)
                
                if self.speed > 0: 
                    return pygame.transform.flip(scaled, True, False)
                
                return scaled
            
            return None

        self.image_hidden = process_sprite(img_hidden)
        self.image_revealed = process_sprite(img_revealed)

    def update_fish_movement(self, dt):
        self.x += self.speed * dt * 60
        self.rect.x = int(self.x)

    def is_offscreen(self):
        if self.speed > 0:
            return self.rect.x > Settings.S_WIDTH + Settings.SPAWN_MARGIN
        else:
            return self.rect.x < -Settings.SPAWN_MARGIN - self.rect.width

    def _draw_geometric_fish(self, surface, color, alpha=255):
        s = pygame.Surface((self.rect.width + 20, self.rect.height), pygame.SRCALPHA)
        body_rect = pygame.Rect(10, 0, 50, 25)

        pygame.draw.rect(s, (*color, alpha), body_rect, border_radius=8)
        pygame.draw.rect(s, (Settings.COLORS["GRAY_ALPHA"]), body_rect, 2, border_radius=8)
        
        eye_x = body_rect.right - 10 if self.speed > 0 else body_rect.left + 10
        pygame.draw.circle(s, (*Settings.COLORS["WHITE"], alpha), (eye_x, body_rect.centery - 5), 4)
        
        if self.speed > 0:
            pts = [(body_rect.left, body_rect.centery), (0, 0), (0, body_rect.height)]
        else:
            pts = [(body_rect.right, body_rect.centery), (s.get_width(), 0), (s.get_width(), body_rect.height)]
            
        pygame.draw.polygon(s, (*color, alpha), pts)
        pygame.draw.polygon(s, (Settings.COLORS["GRAY_ALPHA"]), pts, 2)
        
        surface.blit(s, (self.rect.x - 10 if self.speed > 0 else self.rect.x, self.rect.y))

    def draw(self, surface, mouse_pos, flashlight_radius, sonar_alpha):
        dist = math.hypot(self.rect.centerx - mouse_pos[0], self.rect.centery - mouse_pos[1])
        is_in_light = dist < flashlight_radius
        self.is_revealed = is_in_light or sonar_alpha > 100

        if is_in_light:
            if self.image_revealed:
                surface.blit(self.image_revealed, self.rect)
            else:
                self._draw_geometric_fish(surface, self.color_type)
        elif sonar_alpha > 0:
            if self.image_revealed:
                temp_img = self.image_revealed.copy()
                temp_img.set_alpha(sonar_alpha)
                surface.blit(temp_img, self.rect)
            else:
                self._draw_geometric_fish(surface, self.color_type, sonar_alpha)
        else:
            if self.image_hidden:
                surface.blit(self.image_hidden, self.rect)
            else:
                self._draw_geometric_fish(surface, (30, 60, 90))
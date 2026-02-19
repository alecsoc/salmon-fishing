import pygame

class SlideTransition:
    def __init__(self, speed=8):
        self.speed = speed
        self.alpha = 0
        self.active = False
        self.state = "FADE_OUT"
        self.prev_screen = None
        self.next_screen = None
        self.target_key = None
        self.delay_timer = 0
        self.max_delay = 12

    def start(self, current, next_obj, next_key):
        self.prev_screen = current
        self.next_screen = next_obj
        self.target_key = next_key
        self.alpha = 0
        self.state = "FADE_OUT"
        self.delay_timer = 0
        self.active = True

    def update(self):
        if not self.active: return None

        if self.state == "FADE_OUT":
            self.alpha += self.speed
            if self.alpha >= 255:
                self.alpha = 255
                self.state = "DELAY"
        
        elif self.state == "DELAY":
            self.delay_timer += 1
            if self.delay_timer >= self.max_delay:
                self.state = "FADE_IN"
        
        elif self.state == "FADE_IN":
            self.alpha -= self.speed
            if self.alpha <= 0:
                self.alpha = 0
                self.active = False
                return self.target_key
        return None

    def draw(self, surface):
        if not self.active: return

        if self.state == "FADE_OUT":
            if self.prev_screen:
                self.prev_screen.draw(surface)
        else:
            if self.next_screen:
                self.next_screen.draw(surface)

        overlay = pygame.Surface((surface.get_width(), surface.get_height()))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(self.alpha)
        surface.blit(overlay, (0, 0))
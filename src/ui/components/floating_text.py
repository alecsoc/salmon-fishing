import pygame

from src.config.settings import Settings

class FloatingText:
    def __init__(self, x, y, text, color, font):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.font = font
        self.life = 1.5
        self.alpha = 255
        self.speed = 50

    def update(self, dt):
        self.life -= dt
        self.y -= self.speed * dt
        if self.life < 0.5:
            self.alpha = int((self.life / 0.5) * 255)

    def draw(self, surface):
        if self.life > 0:
            text_surf = self.font.render(self.text, True, self.color)
            text_surf.set_alpha(self.alpha)
            surface.blit(text_surf, (self.x - text_surf.get_width() // 2, self.y))

class FloatingTextManager:
    def __init__(self, font):
        self.font = font
        self.texts = []

    def spawn(self, x, y, amount):
        text = f"+{amount}" if amount > 0 else str(amount)
        color = Settings.COLORS["PASTEL_YELLOW"] if amount > 0 else Settings.COLORS["PASTEL_RED"]
        self.texts.append(FloatingText(x, y, text, color, self.font))

    def update(self, dt):
        for text in self.texts:
            text.update(dt)
        self.texts = [t for t in self.texts if t.life > 0]

    def draw(self, surface):
        for text in self.texts:
            text.draw(surface)
import pygame

from src.config.settings import Settings

from src.ui.components.text_label import TextLabel

class FloatingText:
    def __init__(self, x, y, text, color):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.life = 1.5
        self.alpha = 255
        self.speed = 50

        self.label = TextLabel(
            x=self.x,
            y=self.y,
            text=self.text,
            color=self.color,
            font_key="secondary_font",
            font_size=30,
            alpha=self.alpha
        )

    def update(self, dt):
        self.life -= dt
        self.y -= self.speed * dt

        if self.life < 0.5:
            self.alpha = int((self.life / 0.5) * 255)
        
        self.label.y = self.y
        self.label.alpha = self.alpha
        self.label._render_surface()

    def draw(self, surface):
        if self.life > 0:
            self.label.draw(surface)

class FloatingTextManager:
    def __init__(self):
        self.texts = []

    def spawn(self, x, y, amount):
        text = f"+{amount}" if amount > 0 else str(amount)
        color = Settings.COLORS["PASTEL_YELLOW"] if amount > 0 else Settings.COLORS["PASTEL_RED"]
        self.texts.append(FloatingText(x, y, text, color))

    def update(self, dt):
        for text in self.texts:
            text.update(dt)

        self.texts = [t for t in self.texts if t.life > 0]

    def draw(self, surface):
        for text in self.texts:
            text.draw(surface)
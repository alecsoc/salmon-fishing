import pygame

class Score:
    def __init__(self, x=10, y=10):
        self.x = x
        self.y = y
        self.score = 0
        # la font es mientras tanto, todavia no la hemos definido tengo entendido
        self.font = pygame.font.SysFont("Arial", 30, bold=True)
        self.color = (255, 255, 255)  # (asumo que el puntaje en blanco)
        self.text_surface = self.font.render(
            f"Score: {self.score}", True, self.color
        )  # para renderizarlo por 1era vez

    def update_score(self, new_score):
        # recibe el puntaje actualizado
        self.score = new_score
        self.text_surface = self.font.render(
            f"Score: {self.score}", True, self.color
        )  # basicamente renderizar el puntaje

    def draw(self, screen):
        screen.blit(self.text_surface, (self.x, self.y))
        # solo el blit para no renderizar a menos que se cambie el puntaje

class Timer:
    pass

class FishTarget:
    pass
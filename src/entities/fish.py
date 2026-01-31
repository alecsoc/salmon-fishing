import pygame
from settings import Settings
import random

class Fish:
    def __init__(self, fish_image, difficulty):
        #with y height no son el tamnano del pez sino la posicion de los peces en la pantalla
        #el normal_image se refiere a que la image no ha sido volteada en x(mas abajo se explica)
        #Coloco 1280 y 720 visto que es la resolucion base para todo
        self.normal_image = False
        self.image = fish_image
        self.width = 65
        self.height = 35
        self.color.type = random.choice(Settings.COLORS["RED_COLOR"], Settings.COLORS["BLUE_COLOR"], Settings.COLORS["RED_COLOR"])
        self.direction = random.choice(True, False)
        if self.direction == True:
            self.x = self.width
            self.normal_image = True
            if difficulty == "EASY":
               self.speed = random.uniform(2, 4)
            if difficulty == "MEDIUM":
                self.speed = random.uniform(3.5, 5.5)
            if difficulty == "HARD":
                self.speed = random.uniform(5, 7.3)

        else:
            self.x = 1280 + self.width
            if difficulty == "EASY":
               self.speed = random.uniform(2, 4) * -1
            if difficulty == "MEDIUM":
                self.speed = random.uniform(3.5, 5.5) * -1
            if difficulty == "HARD":
                self.speed = random.uniform(5, 7.3) * -1

        self.y = random.randint(110, 720- 110)

    def turn(self, interface):
        #flip necesita la imagen, la posicion en X y Y, por eso es que en la parte de flip al final esta en falso haciendo refeencia a que la imagen no se volteara de arriba hacia abajo(eje y)
        flipped_image = pygame.transform.flip(self.image, self.normal_image, False)
        interface.blit(flipped_image)

    def update_fish_movement(self):
        #esto es para que el pez no se quede estatico y vaya avanzando independientemente de su direccion, como se ve arriba en la part de la dificultad se suma o se resta si self.speed es negativo o positivo
        self.x += self.speed


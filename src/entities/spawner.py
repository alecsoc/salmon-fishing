from fish import Fish 

class Spawn_manager():
    def __int__(self, spawn_timer, fishes):
        #spawn timer cuando llegue dependiendo del nivel a los valores constantes, se genera un pez con las reglas de la clase Fish()
        self.spawn_timer = 0
        self.fishes = []

    def update_spawn(self, difficulty):
        #estos serian "milisengundos"
        SPAWN_RATE_EASY = 26
        SPAWN_RATE_MEDIUM = 22
        SPAWN_RATE_HARD = 17

        if difficulty == "EASY":
           #coloque el spawn time en cero al final del bucle para que se reinicie el contador y asi se genere otro pez
           self.spawn_timer += 1
           if self.spawn_timer == SPAWN_RATE_EASY:
              self.fishes.append(Fish())
              self.spawn_time = 0

        if difficulty == "MEDIUM":
           self.spawn_timer += 1
           if self.spawn_timer == SPAWN_RATE_MEDIUM:
              self.fishes.append(Fish())
              self.spawn_time = 0

        if difficulty == "HARD":
           self.spawn_timer += 1
           if self.spawn_timer == SPAWN_RATE_HARD:
              self.fishes.append(Fish())
              self.spawn_time = 0
        
        #este bucle de abajo es para que los peces que esten muy lejos de la pantalla se elminen, the_fishes.x es simplemente la variable x de la clase Fish junto con el bucle, recordando que self.x se refiere a las coordenadas en x
        #se tiene que ir a la funcion update_fish_movement para que el self.x de la clase fish aumente progresivamente
        fishes_on_screen = []
        for the_fishes in self.fishes:
           the_fishes.update_fish_movement()
           #-100 y 1280 -100 estan practicamente fuera de los limites de la pantalla
           if the_fishes.x > -100 and the_fishes.x < 1280 + 100:
              #aqui agregamos uno por uno a los peces que cumplen las condiciones
              fishes_on_screen.append(the_fishes)
           #esta parte solo reemplaza todos los peces, tantp por fuera como en la pantalla por los peces que estan en ka pantalla
           self.fishes = fishes_on_screen

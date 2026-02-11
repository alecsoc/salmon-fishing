import random
from src.config.settings import Settings
from src.config.game_modes import MODES
from src.managers.asset_manager import AssetManager
from src.entities.fish import Fish

class SpawnManager:
    def __init__(self):
        self.spawn_timer = 0
        self.fishes = []

    def _create_fish(self, difficulty):
        """Método fábrica (Factory Method) encargado de definir y crear peces según su dificultad."""
        is_from_left = random.choice(
            [True, False]
        )  # True = sale por la izquierda, False = sale por la derecha

        if is_from_left:
            x_pos = -Settings.SPAWN_MARGIN
        else:
            x_pos = Settings.S_WIDTH + Settings.SPAWN_MARGIN

        y_pos = random.randint(
            int(Settings.S_HEIGHT * 0.2), int(Settings.S_HEIGHT * 0.8)
        )

        base_speed = random.uniform(Settings.FISH_SPEED_MIN, Settings.FISH_SPEED_MAX)
        multiplier = MODES[difficulty]["speed"]

        speed = base_speed * multiplier
        if not is_from_left:
            speed *= -1  # se invierte la dirección

        fish_image = AssetManager.get_image("fish")
        new_fish = Fish(x_pos, y_pos, speed, fish_image)
        self.fishes.append(new_fish)

    def update_spawn(self, dt, difficulty):
        self.spawn_timer += dt
        spawn_cooldown = (
            MODES[difficulty]["spawn"] / 1000.0
        )  # conversión de milisegundos a segundos para comparar con el dt

        if self.spawn_timer >= spawn_cooldown:
            self._create_fish(difficulty)
            self.spawn_timer = 0  # se reinicia para crear el siguiente pez

        for fish in self.fishes:
            fish.update_fish_movement(dt)

        self.fishes = [fish for fish in self.fishes if not fish.is_offscreen()]

    def draw(self, surface):
        for fish in self.fishes:
            fish.draw(surface)
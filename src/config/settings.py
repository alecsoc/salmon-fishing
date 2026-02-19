from enfocate import SCREEN_SIZE
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings:
    # Metadata
    TITLE = "Pescar Al Salmón"
    DESCRIPTION = (
        "Minijuego de integración al proyecto final de Objetos y Abstracción de Datos."
    )
    AUTHORS = [
        "Abelardo Drika",
        "Adrián Zambrano",
        "Alejandro Capriles",
        "Luciano Pietrucci",
    ]
    GROUP_NUMBER = 10

    # --- Game parameters ---

    # Screen parameters
    S_WIDTH, S_HEIGHT = SCREEN_SIZE

    # Visibility / Lantern
    FLASHLIGHT_RADIUS_BASE = 100
    SONAR_CYCLE_DURATION = 5.0
    SONAR_ACTIVE_DURATION = 0.8
    GAME_OVER_WAIT_TIME = 5.0

    # Entities (Fish)
    FISH_SIZE = (60, 30)
    SPAWN_MARGIN = 100
    FISH_SPEED_MIN = 3.0
    FISH_SPEED_MAX = 7.0

    # Assets directions
    ASSETS_PATH = BASE_DIR / "assets"
    IMAGES_PATH = ASSETS_PATH / "images"
    SOUNDS_PATH = ASSETS_PATH / "sounds"
    FONTS_PATH = ASSETS_PATH / "fonts"

    IMAGES_MAP = {
        "main_bg": "background.jpg",
        "hidden_fish": "hidden_fish.png",
        "red_fish": "red_fish.png",
        "green_fish": "green_fish.png",
        "blue_fish": "blue_fish.png",
        "thought_cloud": "thought_cloud.png",
    }

    SOUNDS_MAP = {}
    FONTS_MAP = {}

    IMAGES = {}
    SOUNDS = {}
    FONTS = {}

    # Colors
    COLORS = {
        "RED_COLOR": (255, 65, 54),
        "GREEN_COLOR": (46, 204, 64),
        "BLUE_COLOR": (0, 116, 217),
        "PASTEL_YELLOW": (253, 253, 150),
        "PASTEL_ORANGE": (255, 179, 71),
        "PASTEL_BLUE": (174, 198, 207),
        "PASTEL_RED": (255, 105, 97),
        "PASTEL_TEAL": (100, 200, 190),
        "WHITE": (255, 255, 255),
        "GRAY_ALPHA": (50, 50, 50, 150)
    }
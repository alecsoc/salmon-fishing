import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings:
    # Metadata
    TITLE = "Pescar Al Salmón"
    DESCRIPTION = "Minijuego de integración al proyecto final de Objetos y Abstracción de Datos."
    AUTHORS = ["Abelardo Drika", "Adrián Zambrano", "Alejandro Capriles", "Luciano Pietrucci"]
    GROUP_NUMBER = 10

    # --- Game parameters ---

    # Visibility / Lantern
    FLASHLIGHT_RADIUS_BASE = 100
    SONAR_CYCLE_DURATION = 5.0
    SONAR_ACTIVE_DURATION = 0.8

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

    IMAGES_MAP = {}

    SOUNDS_MAP = {}

    FONTS_MAP = {}

    IMAGES = {}
    SOUNDS = {}
    FONTS = {}
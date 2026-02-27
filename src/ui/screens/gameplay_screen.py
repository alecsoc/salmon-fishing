import pygame
import random

from src.config.settings import Settings
import src.config.game_modes as game_modes

from src.managers.asset_manager import AssetManager
from src.managers.sound_player import SoundPlayer

from src.ui.base_screen import BaseScreen

from src.ui.components.hud import Score, Timer, TargetDisplay, ComboCounter, GameBanner
from src.ui.components.floating_text import FloatingTextManager

from src.entities.spawner import SpawnManager

from src.mechanics.flashlight import Flashlight
from src.mechanics.sonar import Sonar

class GameplayScreen(BaseScreen):
    def __init__(self):
        self.bg_image = AssetManager.get_image("main_bg")

    def reset_game(self):
        self.mode = game_modes.ACTUAL_MODE 
        mode_settings = game_modes.MODES[self.mode]
        
        self.game_time = float(mode_settings["time"])
        self.current_score = 0
        
        self.target_color_name = random.choice(["red", "green", "blue"])
        self.target_color_rgb = Settings.COLORS[f"{self.target_color_name.upper()}_COLOR"]
        self.target_switch_timer = 0

        SoundPlayer.play_music("main_theme")
        
        self.spawner = SpawnManager()
        self.flashlight = Flashlight()
        self.sonar = Sonar()
        
        self.score_display = Score(x=20, y=20)
        self.timer_display = Timer(y=20)
        
        self.target_display = TargetDisplay({
            "thought_cloud": AssetManager.get_image("thought_cloud"),
            "red_fish": AssetManager.get_image("red_fish"),
            "green_fish": AssetManager.get_image("green_fish"),
            "blue_fish": AssetManager.get_image("blue_fish")
        })
        
        self.combo_counter = ComboCounter()
        
        f_floating = Settings.FONTS.get("floating_font")
        if not f_floating: f_floating = pygame.font.SysFont("Arial", 28, bold=True)
        self.floating_texts = FloatingTextManager()
        
        self.game_over_active = False
        self.game_over_timer = 0
        self.banner = GameBanner("¡SE ACABÓ EL TIEMPO!")

    def handle_events(self, events):
        if self.game_over_active: return None

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_click(event.pos)

        return None

    def _handle_click(self, mouse_pos):
        hit = False

        for fish in self.spawner.fishes:
            if fish.rect.collidepoint(mouse_pos) and fish.is_revealed:
                is_correct = fish.color_type == self.target_color_rgb
                points = 100 if is_correct else -100
                
                self.current_score += points
                
                if points > 0:
                    self.combo_counter.add()
                    SoundPlayer.play_sfx("correct")
                else:
                    self.combo_counter.reset()
                    SoundPlayer.play_sfx("fail")
                
                self.score_display.update_score(self.current_score)
                self.floating_texts.spawn(mouse_pos[0], mouse_pos[1], points)
                self.spawner.fishes.remove(fish)
                hit = True
                
                break
        
        if not hit:
            self.combo_counter.reset()

    def update(self, dt):
        if self.game_over_active:
            self.game_over_timer += dt
            
            if self.game_over_timer >= Settings.GAME_OVER_WAIT_TIME:
                pygame.mouse.set_visible(True)
                return ("GOTO_RESULTS", self.current_score)
            
            return

        self.game_time -= dt
        if self.game_time <= 0:
            self.game_time = 0
            self._handle_game_over()

        self.target_switch_timer += dt
        if self.target_switch_timer >= 15.0:
            self._switch_target()

        self.flashlight.update(pygame.mouse.get_pos())
        self.sonar.update(dt)
        self.timer_display.update(self.game_time)
        self.combo_counter.update()
        self.floating_texts.update(dt)
        
        self.spawner.update_spawn(dt, self.mode)

    def _handle_game_over(self):
        self.game_over_active = True
        SoundPlayer.stop_music()
        SoundPlayer.play_sfx("time_up", 0.8)

    def _switch_target(self):
        self.target_color_name = random.choice(["red", "green", "blue"])
        self.target_color_rgb = Settings.COLORS[f"{self.target_color_name.upper()}_COLOR"]
        self.target_switch_timer = 0

    def draw(self, surface):
        if self.bg_image:
            scaled_bg = pygame.transform.scale(self.bg_image, surface.get_size())
            surface.blit(scaled_bg, (0, 0))
        else:
            surface.fill((0, 50, 100))

        self.spawner.draw(surface, self.flashlight.pos, self.flashlight.radius, self.sonar.alpha)
        
        self.flashlight.draw(surface)
        self.sonar.draw_bar(surface)
        
        self.target_display.draw(surface, self.target_color_name, self.target_color_rgb)
        self.score_display.draw(surface)
        self.timer_display.draw(surface)
        
        self.combo_counter.draw(surface)
        self.floating_texts.draw(surface)

        if self.game_over_active:
            self.banner.draw(surface)

    def on_enter(self):
        pygame.mouse.set_visible(False)
        SoundPlayer.play_music("main_theme")
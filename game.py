import pygame
from typing import List
from pygame.event import Event

from enfocate import GameBase, GameMetadata

from src.config.settings import Settings
import src.config.game_modes as game_modes

from src.managers.asset_manager import AssetManager
from src.managers.sound_player import SoundPlayer

from src.ui.components.slide import SlideTransition

from src.ui.screens.main_screen import MainScreen
from src.ui.screens.modes_screen import ModesScreen
from src.ui.screens.gameplay_screen import GameplayScreen
from src.ui.screens.results_screen import ResultsScreen
from src.ui.screens.instructions_screen import InstructionsScreen
from src.ui.screens.credits_screen import CreditsScreen

class Game(GameBase):
    def __init__(self) -> None:
        meta = GameMetadata(
            Settings.TITLE,
            Settings.DESCRIPTION,
            Settings.AUTHORS,
            Settings.GROUP_NUMBER
        )

        super().__init__(meta)
        
        self.modes = ["START_EASY", "START_MEDIUM", "START_HARD"]
        self.transition = SlideTransition(speed=40)

    def on_start(self) -> None:
        AssetManager.load_all_assets()

        SoundPlayer.play_music("menu_theme")

        self.screens = {
            "MAIN_MENU": MainScreen(),
            "MODES": ModesScreen(),
            "GAMEPLAY": GameplayScreen(),
            "RESULTS": ResultsScreen(),
            "INSTRUCTIONS": InstructionsScreen(),
            "CREDITS": CreditsScreen()
        }

        self.current_screen = self.screens["MAIN_MENU"]
    
    def handle_events(self, events: List[Event]) -> None:
        if self.transition.active: return
        
        result = self.current_screen.handle_events(events)

        if result == "GOTO_MODES":
            self.transition.start(self.current_screen, self.screens["MODES"], "MODES")
        elif result == "GOTO_CREDITS":
            self.transition.start(self.current_screen, self.screens["CREDITS"], "CREDITS")
        elif result == "GOTO_INSTR":
            self.transition.start(self.current_screen, self.screens["INSTRUCTIONS"], "INSTRUCTIONS")
        elif result == "GOTO_MENU":
            self.transition.start(self.current_screen, self.screens["MAIN_MENU"], "MAIN_MENU")
        elif result in self.modes:
            game_modes.ACTUAL_MODE = result.replace("START_", "")
            
            self.screens["GAMEPLAY"].reset_game()
            self.screens["GAMEPLAY"].on_enter()
            self.transition.start(self.current_screen, self.screens["GAMEPLAY"], "GAMEPLAY")
        elif result == "EXIT":
            self._stop_context()
    
    def update(self, dt: float) -> None:
        new_screen_key = self.transition.update()

        if new_screen_key:
            self.current_screen = self.screens[new_screen_key]

        if not self.transition.active and self.current_screen:
            result = self.current_screen.update(dt)

            if result == "GOTO_MENU":
                self.transition.start(self.current_screen, self.screens["MAIN_MENU"], "MAIN_MENU")
            elif isinstance(result, tuple):
                signal, score_data = result

                if signal == "GOTO_RESULTS":
                    SoundPlayer.play_music("menu_theme")
                    
                    self.screens["RESULTS"] = ResultsScreen(score=score_data)
                    self.transition.start(self.current_screen, self.screens["RESULTS"], "RESULTS")

        is_game = self.current_screen == self.screens["GAMEPLAY"]
        pygame.mouse.set_visible(not is_game or self.transition.active)
    
    def draw(self) -> None:
        if self.transition.active:
            self.transition.draw(self.surface)
        elif self.current_screen:
            self.current_screen.draw(self.surface)
    
    def on_stop(self) -> None:
        print("Cerrando Pescar Al Salmón...")
        SoundPlayer.stop_all()

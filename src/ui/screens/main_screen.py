import pygame
from src.managers.asset_manager import AssetManager
from src.ui.base_screen import BaseScreen
from src.ui.components.button import Button

class MainScreen(BaseScreen):
    def __init__(self):
        self.bg_image = AssetManager.get_image("bg_main")

        # Coordenadas y botones
        x_pos = 515
        btn_w, btn_h = 250, 70

        self.buttons = {
            "PLAY": Button(x_pos, 280, btn_w, btn_h),
            "CONFIG": Button(x_pos, 370, btn_w, btn_h),
            "CREDITS": Button(x_pos, 460, btn_w, btn_h),
            "EXIT": Button(x_pos, 550, btn_w, btn_h),
        }

    def handle_events(self, events):
        # Mapa de eventos para desacoplar la clave del botón del retorno
        event_map = {
            "PLAY": "GOTO_MODES",
            "CONFIG": "GOTO_CONFIG",
            "CREDITS": "GOTO_CREDITS",
            "EXIT": "EXIT",
        }

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                # No importa cuántos botones añadas, esta lógica no cambia
                for key, button in self.buttons.items():
                    if button.is_clicked(mouse_pos):
                        return event_map.get(key)

        return None

    def update(self, dt):
        pass

    def draw(self, surface):
        # Logica de dibujo actualizada: Si hay imagen la usa, sino usa el azul
        if self.bg_image:
            # Escalamos la imagen al tamaño de la ventana actual para que cubra todo
            scaled_bg = pygame.transform.scale(self.bg_image, surface.get_size())
            surface.blit(scaled_bg, (0, 0))
        else:
            # Color de respaldo (Azul Océano)
            surface.fill((0, 105, 148))

        # Dibujamos los botones
        for button in self.buttons.values():
            button.draw(surface)
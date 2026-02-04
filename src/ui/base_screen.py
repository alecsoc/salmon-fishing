from abc import ABC, abstractmethod
class BaseScreen(ABC):
    @abstractmethod
    def update(self,dt):
        #actualiza la logica matematica 
      pass
    @abstractmethod
    def draw(self,surface):
        #dibuja los elementos visuales
      pass
    @abstractmethod
    def handle_events(self, events):
        #recibe la lista de eventos
        pass

#Intento de menu abstracto para tomar como base para los menus (Inicio,Gameplay,Configuracion)


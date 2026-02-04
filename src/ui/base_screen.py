from abc import ABC, abstractmethod
class BaseScreen(ABC):
    @abstractmethod
    def update(self,events):
      pass
    @abstractmethod
    def draw(self,screen):
      pass

#Intento de menu abstracto para tomar como base para los menus (Inicio,Gameplay,Configuracion)

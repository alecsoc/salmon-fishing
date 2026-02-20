from abc import ABC, abstractmethod

class BaseScreen(ABC):
    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def handle_events(self, events):
        pass
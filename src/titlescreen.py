import pygame, os
from src.state import State
from src.mainscreen import MainScreen

class TitleScreen(State):
    def __init__ (self, game):
        State.__init__(self, game)
        self.image = pygame.image.load(os.path.join(self.game.assets_dir, "title.png"))

    def update(self, deltaTime, actions):
        if actions["start"]:
            new_state = MainScreen("overworld", self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.image, (0, 0))
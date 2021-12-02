import pygame, os
from src.state import State
from src.titlescreen import TitleScreen

class SplashScreen(State):
    def __init__ (self, game):
        State.__init__(self, game)
        self.image = pygame.image.load(os.path.join(self.game.assets_dir, "splash.png"))

    def update(self, deltaTime, actions):
        if actions["start"] or actions["abutton"]:
            new_state = TitleScreen(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.image, (0, 0))
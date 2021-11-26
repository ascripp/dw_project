import pygame, os
from src.state import State
from src.titlescreen import TitleScreen

class SplashScreen(State):
    def __init__ (self, game):
        State.__init__(self, game)

    def update(self, deltaTime, actions):
        if actions["start"]:
            new_state = TitleScreen(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((255, 255, 255))
        self.game.draw_text(display, "Splash Screen Test", (0, 0, 0), self.game.screenWidth/2, 
            self.game.screenHeight/2)
#------------------------- Import libraries
import os, sys, math, time, pygame

from src.title import Title

class Game():

    def __init__(self):
        pygame.init()
        self.screenWidth = 960
        self.screenHeight = 960
        self.gameCanvas = pygame.Surface((self.screenWidth, self.screenHeight))
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_caption('Dragon Warrior Pygame')
        self.running, self.playing = True, True
        self.actions = {"left": False, "right": False, "up": False, "down": False, "abutton": False,
        "bbutton": False, "start": False, "select": False}
        self.deltaTime, self.prevTime = 0, 0
        self.stateStack = []
        self.load_assets()
        self.load_states()

    def game_loop(self):
        while self.playing:
            self.get_deltaTime()
            self.get_actions()
            self.update()
            self.render()

    def get_actions(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.running = False
                if event.key == pygame.K_UP:
                    self.actions['up'] = True
                if event.key == pygame.K_DOWN:
                    self.actions['down'] = True
                if event.key == pygame.K_LEFT:
                    self.actions['left'] = True
                if event.key == pygame.K_RIGHT:
                    self.actions['right'] = True
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = True
                if event.key == pygame.K_RSHIFT:
                    self.actions['select'] = True
                if event.key == pygame.K_a:
                    self.actions['abutton'] = True
                if event.key == pygame.K_b:
                    self.actions['bbutton'] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.actions['up'] = False
                if event.key == pygame.K_DOWN:
                    self.actions['down'] = False
                if event.key == pygame.K_LEFT:
                    self.actions['left'] = False
                if event.key == pygame.K_RIGHT:
                    self.actions['right'] = False
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = False
                if event.key == pygame.K_RSHIFT:
                    self.actions['select'] = False
                if event.key == pygame.K_a:
                    self.actions['abutton'] = False
                if event.key == pygame.K_b:
                    self.actions['bbutton'] = False

    def update(self):
        self.stateStack[-1].update(self.deltaTime, self.actions)

    def render(self):
        self.stateStack[-1].render(self.gameCanvas)
        self.screen.blit(self.gameCanvas, (0, 0))
        pygame.display.flip()

    def get_deltaTime(self):
        now = time.time()
        self.deltaTime = now - self.prevTime
        self.prevTime = now

    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        #text_surface.set_colorkey((0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def load_assets(self):
        self.assets_dir = os.path.join("assets")
        self.sprite_dir = os.path.join(self.assets_dir, "sprites")
        self.font_dir = os.path.join(self.assets_dir, "font")
        self.font = pygame.font.Font(os.path.join(self.font_dir, "PressStart2P.ttf"), 20)

    def load_states(self):
        self.title_screen = Title(self)
        self.stateStack.append(self.title_screen)

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False


if __name__ == "__main__":
    game = Game()
    
    while game.running:
        game.game_loop()
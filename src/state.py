class State():
    def __init__(self, game):
        self.game = game
        self.prev_state = None

    def update(self, deltaTime, actions, firstCall):
        pass

    def render(self, surface):
        pass

    def enter_state(self):
        if len(self.game.stateStack) > 1:
            self.prev_state = self.game.stateStack[-1]
        self.game.stateStack.append(self)

    def exit_state(self):
        self.game.stateStack.pop()
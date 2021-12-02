import pygame, os
from src.state import State
from assets.menudata import *
from src.test import testfunc

class mainMenu(State):
    def __init__(self, menuname, game):
        self.game = game
        State.__init__(self, game)
        # Set the menu
        self.menubasesheet = pygame.image.load(os.path.join(self.game.assets_dir, "bordertiles.png"))
        self.menutextsheet = pygame.image.load(os.path.join(self.game.assets_dir, "textiles.png"))
        self.menuname = menuname
        self.menulocation = list(map(int, menuLocations[menuname]))
        self.menulist = list(map(int, menus[menuname]))
        self.menutitle = list(map(str, titles[menuname]))
        #self.menuOptions = menuOptions[menuname]
        self.baseimage_width, self.baseimage_height = self.menubasesheet.get_size()
        self.basetile_width, self.basetile_height = 64, 64
        self.textimage_width, self.textimage_height = self.menutextsheet.get_size()
        self.texttile_width, self.texttile_height = 32, 32
        self.menux_size = self.basetile_width * self.menulist[-2]
        self.title_size = len(self.menutitle) * self.texttile_width
        self.title_location = (self.menulocation[0] * self.basetile_width) + \
            ((self.menux_size / 2) - (self.title_size / 2))
        self.basetile_table = []
        self.texttile_table = []
        for tile_y in range(0, self.baseimage_height//self.basetile_height):
            for tile_x in range(0, self.baseimage_width//self.basetile_width): 
                rect = (tile_x*self.basetile_width, tile_y*self.basetile_height, 
                self.basetile_width, self.basetile_height) 
                self.basetile_table.append(self.menubasesheet.subsurface(rect))
        for tile_y in range(0, self.textimage_height//self.texttile_height):
            for tile_x in range(0, self.textimage_width//self.texttile_width):
                rect = (tile_x*self.texttile_width, tile_y*self.texttile_height, 
                self.texttile_width, self.texttile_height)
                self.texttile_table.append(self.menutextsheet.subsurface(rect))
        self.cursortile = self.texttile_table[79]
        self.moretile = self.texttile_table[80]

        # Set the cursor and menu states
        #self.menu_options = {0 :"Talk", 1 : "Status", 2 :"Stairs", 3 : "Search", 4 : "Spell", 
        #5 : "Item", 6 : "Door", 7 : "Take"}
        #self.index = 0
        #self.cursor_img = pygame.image.load(os.path.join(self.game.assets_dir, "map", "cursor.png"))
        #self.cursor_rect = self.cursor_img.get_rect()
        #self.cursor_pos_y = self.menu_rect.y + 38
        #self.cursor_rect.x, self.cursor_rect.y = self.menu_rect.x + 10, self.cursor_pos_y

    def load_menu(self):
        x, y = 0, 1
        self.current_menu = []
        menu_width = self.menulist[-2]
        menu_height = self.menulist[-1]
        for a in range(0, menu_height):
            for b in range(0, menu_width):
                self.current_menu.append(self.menulist[x])
                x += 1
            y += 1
        return self.current_menu

    def draw_menu(self, menu_tiles, display):
        menu_width = self.menulist[-2]
        menu_height = self.menulist[-1]        
        x = 0
        x_pos = self.menulocation[0] * self.basetile_width
        y_pos = self.menulocation[1] * self.basetile_height
        for a in range(0, menu_height):
            for b in range(0, menu_width):
                display.blit(menu_tiles[self.current_menu[x] -1], (x_pos, y_pos))
                x_pos += self.basetile_width
                x += 1
            x_pos = self.menulocation[0] * self.basetile_width
            y_pos += self.basetile_height

    def draw_title(self, title_tiles, display):
        a, b = 0, 0
        title = []
        x_pos = self.title_location
        y_pos = self.menulocation[1] * self.basetile_height
        for i in range(0, len(self.menutitle)):
            title.append(alphabet[self.menutitle[a]])
            a += 1
        for i in range(0, len(title)):
            display.blit(title_tiles[title[b] -1], (x_pos, y_pos))
            x_pos += self.texttile_width
            b += 1

    def draw_text(self, text_tiles, display):
        for i in range(0, len(menuOptions[self.menuname])):
            a = 0
            optionText = list(map(str, menuOptions[self.menuname][i][0]))
            text = []
            x_pos = (self.menulocation[0] + menuOptions[self.menuname][i][1]) * self.basetile_width
            y_pos = (self.menulocation[1] + menuOptions[self.menuname][i][2]) * self.basetile_height
            for j in range(0, len(optionText)):
                text.append(alphabet[optionText[a]])
                display.blit(text_tiles[text[a] -1], (x_pos, y_pos))
                x_pos += self.texttile_width
                a += 1

    def update(self, delta_time, actions):  
        #self.update_cursor(actions)      
        if actions["abutton"]:
            pass
        if actions["bbutton"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        # render the gameworld behind the menu, which is right before the pause menu on the stack
        #self.game.stateStack[-2].render(display)
        self.prev_state.render(display)
        self.load_menu()
        self.draw_menu(self.basetile_table, display)
        self.draw_title(self.texttile_table, display)
        self.draw_text(self.texttile_table, display)

    #def transition_state(self):
    #    if self.menu_options[self.index] == "Status": 
    #        new_state = PartyMenu(self.game)
    #        new_state.enter_state()
    #    elif self.menu_options[self.index] == "Spell": 
    #        pass # TO-DO
    #    elif self.menu_options[self.index] == "Item": 
    #        pass # TO-DO
    #    elif self.menu_options[self.index] == "Exit": 
    #        while len(self.game.state_stack) > 1:
    #            self.game.state_stack.pop()


    #def update_cursor(self, actions):
    #    if actions['down']:
    #        if self.index != 3 or self.index != 7:
    #           self.index = (self.index + 1) % len(self.menu_options)
    #    elif actions['up']:
    #        if self.index != 0 or self.index != 4:
    #           self.index = (self.index - 1) % len(self.menu_options)
    #    elif actions['right']:
    #        if self.index < 4:
    #           self.index = (self.index + 4) % len(self.menu_options)
    #    elif actions['left']:
    #        if self.index > 3:
    #           self.index = (self.index = 4) % len(self.menu_options)
    #    self.cursor_rect.y = self.cursor_pos_y + (self.index * 32)

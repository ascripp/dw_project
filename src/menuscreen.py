import pygame, os
from src.state import State
from assets.menudata import *
from assets.playerdata import playerData

class Menu(State):
    def __init__(self, menuname, game):
        self.game = game
        State.__init__(self, game)
        self.menubasesheet = pygame.image.load(os.path.join(self.game.assets_dir, "bordertiles.png"))
        self.menutextsheet = pygame.image.load(os.path.join(self.game.assets_dir, "textiles.png"))
        self.menuname = menuname
        self.menulocation = list(map(int, menuLocations[menuname]))
        self.menulist = list(map(int, menus[menuname]))
        self.menutitle = list(map(str, titles[menuname]))
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
        self.cursortile = self.texttile_table[78]
        self.moretile = self.texttile_table[79]
        self.cursorindex = 0


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
            optionText = list(map(str, menuOptions[self.menuname][i]['text']))
            text = []
            x_pos = (self.menulocation[0] + menuOptions[self.menuname][i]['xloc']) \
            * self.basetile_width
            y_pos = (self.menulocation[1] + menuOptions[self.menuname][i]['yloc']) \
            * self.basetile_height
            for j in range(0, len(optionText)):
                text.append(alphabet[optionText[a]])
                display.blit(text_tiles[text[a] -1], (x_pos, y_pos))
                x_pos += self.texttile_width
                a += 1

    def draw_cursor(self, display):
        x_pos = (self.menulocation[0] + menuOptions[self.menuname][self.cursorindex]['xloc'] - .5) \
        * self.basetile_width
        y_pos = (self.menulocation[1] + menuOptions[self.menuname][self.cursorindex]['yloc']) \
        * self.basetile_height
        #flip back and forth every 1/4 second
        if self.game.animationCounter <= (self.game.FPS/4):
            display.blit(self.texttile_table[78], (x_pos, y_pos))
        elif self.game.animationCounter >= ((self.game.FPS/4)+1):
            display.blit(self.texttile_table[80], (x_pos, y_pos))
        #display.blit(self.cursortile, (x_pos, y_pos))  

    def update(self, delta_time, actions):  
        #advance counter for animation
        if self.game.animationCounter < self.game.FPS/2:
            self.game.animationCounter += 1
        elif self.game.animationCounter >= self.game.FPS/2:
            self.game.animationCounter = 1    
        self.update_cursor(actions)      
        if actions["abutton"]:
            self.menu_action()
        if actions["bbutton"]:
            if self.menuname == "main":
                self.exit_state()
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        self.prev_state.render(display)
        self.load_menu()
        self.draw_menu(self.basetile_table, display)
        self.draw_title(self.texttile_table, display)
        self.draw_text(self.texttile_table, display)
        if self.menuname != "status" and self.menuname != "ministat":
            self.draw_cursor(display)

    def render_mini(self, display):
        self.load_menu()
        self.draw_menu(self.basetile_table, display)
        self.draw_title(self.texttile_table, display)
        self.draw_text(self.texttile_table, display)

    def menu_action(self):
        if menuOptions[self.menuname][self.cursorindex]['text'] == "STATUS": 
            new_state = Menu("status", self.game)
            new_state.enter_state()
        elif menuOptions[self.menuname][self.cursorindex]['text'] == "SPELL":
            pass 
            #new_state = Menu("spell", self.game)
            #new_state.enter_state()
        elif menuOptions[self.menuname][self.cursorindex]['text'] == "ITEM":
            pass 
            #new_state = Menu("item", self.game)
            #new_state.enter_state()
        elif menuOptions[self.menuname][self.cursorindex]['text'] == "TALK": 
            pass
            #menuOptions[self.menuname][self.cursorindex]['action']()
        elif menuOptions[self.menuname][self.cursorindex]['text'] == "SEARCH": 
            pass
            #menuOptions[self.menuname][self.cursorindex]['action']()
        elif menuOptions[self.menuname][self.cursorindex]['text'] == "STAIRS": 
            pass
            #menuOptions[self.menuname][self.cursorindex]['action']()
        elif menuOptions[self.menuname][self.cursorindex]['text'] == "DOOR": 
            pass
            #menuOptions[self.menuname][self.cursorindex]['action']()
        elif menuOptions[self.menuname][self.cursorindex]['text'] == "TAKE": 
            pass
            #menuOptions[self.menuname][self.cursorindex]['action']()



    def update_cursor(self, actions):
        if actions["down"]:
            if self.cursorindex != 3 or self.cursorindex != 7:
                self.cursorindex = (self.cursorindex + 1)
        elif actions["up"]:
            if self.cursorindex != 0 or self.cursorindex != 4:
                self.cursorindex = (self.cursorindex - 1)
        elif actions["right"]:
            if self.cursorindex < 4:
                self.cursorindex = (self.cursorindex + 4)
        elif actions["left"]:
            if self.cursorindex > 3:
                self.cursorindex = (self.cursorindex - 4)

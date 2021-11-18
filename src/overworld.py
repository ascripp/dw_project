import pygame, os
from src.state import State

class Overworld(State):
    def __init__ (self, mapname, game):
        State.__init__(self, game)
        self.image = pygame.image.load(os.path.join(self.game.assets_dir, "tiles.png"))
        self.mapname = []
        with open(mapname + '.maptiles') as mapfile:
            self.mapname = list(map(int, mapfile.read().split('\n')))
        self.image_width, self.image_height = self.image.get_size()
        #initialize list to hold tiles
        self.tile_table = []
        #load tiles into list
        for tile_y in range(0, self.image_height//64): #split image into rows by tile height
            for tile_x in range(0, self.image_width//64):  #split rows into tiles by tile width
                rect = (tile_x*64, tile_y*64, 64, 64)  #grab a tile
                self.tile_table.append(self.image.subsurface(rect))  #add tile to the map list

    def load_map(self, x_off, y_off):
        # initialize variables
        x_off = x_off - 7  #x and y offsets to place character in the middle of the screen
        y_off = y_off - 7
        temp_map = self.mapname
        self.current_map = []
        map_width = self.mapname[-1]  #the last index in the list is the width of the map
        #load visible part of map
        for a in range(0, 15):
            for b in range(0, 15):
                self.current_map.append(temp_map[x_off + (y_off * map_width)] - 1)
                x_off += 1
            y_off += 1
            x_off -= 15
        #return 15 x 15 visible map
        return self.current_map
        
    def get_map(self):
        return self.current_map
    
    def draw_map(self, terrain_tiles, display):
        x = 0
        x_position = 0
        y_position = 0
        #draw 15 x 15 square visible portion of map
        for a in range(0, 15):
            for b in range(0, 15):
                display.blit(terrain_tiles[self.current_map[x]], (x_position, y_position))
                x_position += 64
                x += 1
            x_position = 0
            y_position += 64

    def update(self, deltaTime, actions):
        pass

    def render(self, display):
        self.load_map(46, 47)
        self.draw_map(self.tile_table, display)

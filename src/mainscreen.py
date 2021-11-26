import pygame, os
from time import sleep
from src.state import State
from assets.mapdata import *
from assets.player import playerData

class MainScreen(State):
    def __init__ (self, mapname, game):
        State.__init__(self, game)
        self.image = pygame.image.load(os.path.join(self.game.assets_dir, "tiles.png"))
        self.maplist = list(map(int, maps[mapname]))
        self.collisionTiles = list(map(int, collisionTiles))
        self.exitTiles = list(map(int, exitTiles))
        self.frameTimer = 0
        self.character = Character(self.game)
        self.startLocation = list(map(int, startLocation[mapname]))
        self.herox = self.startLocation[0]
        self.heroy = self.startLocation[1]
        self.image_width, self.image_height = self.image.get_size()
        self.tile_width, self.tile_height = 64, 64
        #initialize list to hold tiles
        self.tile_table = []
        #load tiles into list
        for tile_y in range(0, self.image_height//self.tile_height): #split image into rows by tile height
            for tile_x in range(0, self.image_width//self.tile_width):  #split rows into tiles by tile width
                rect = (tile_x*self.tile_width, tile_y*self.tile_height, 
                self.tile_width, self.tile_height)  #set location of tile on screen
                self.tile_table.append(self.image.subsurface(rect))  #add tile to the map list

    def load_map(self, x_off, y_off):
        # initialize variables
        x_off = x_off - 7  #x and y offsets to place character in the middle of the screen
        y_off = y_off - 7
        self.current_map = [] #list to hold tiles for visible portion of map
        map_width = self.maplist[-1]  #the last index in the list is the width of the map
        #load visible part of map
        for a in range(0, 15): #15 rows
            for b in range(0, 15): #15 columns
                #place tiles in current_map from temp_map based on offsets from hero coords
                self.current_map.append(self.maplist[x_off + (y_off * map_width)] - 1)
                x_off += 1 #increment x for columns
            y_off += 1 #increment y for rows
            x_off -= 15 #reset x for column 1
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

    def do_movement(self, deltaTime, actions):
        if actions["up"]:
            if self.current_map[97] not in self.collisionTiles:
                self.heroy -= 1
                if self.current_map[97] in self.exitTiles:
        elif actions["down"]:
            if self.current_map[127] not in self.collisionTiles:
                self.heroy += 1
                if self.current_map[127] in self.exitTiles:
        elif actions["left"]:
            if self.current_map[111] not in self.collisionTiles:
                self.herox -= 1
                if self.current_map[111] in self.exitTiles:
        elif actions["right"]:
            if self.current_map[113] not in self.collisionTiles:
                self.herox += 1
                if self.current_map[113] in self.exitTiles:
        #elif event.key == pygame.K_RETURN:
        #elif event.key == pygame.K_ESCAPE:
        #self.frameTimer += deltaTime
        #if self.frameTimer > .25:
        #    self.frameTimer = 0

    def update(self, deltaTime, actions):
        self.character.update(actions)
        self.do_movement(deltaTime, actions)


    def render(self, display):
        self.load_map(self.herox, self.heroy)
        self.draw_map(self.tile_table, display)
        self.character.render(display)


class Character():
    def __init__(self, game):
        self.game = game
        self.sprite_frame = 0 #map(int, playerData[sprite_frame])
        self.animationCounter = 0
        self.image = pygame.image.load(os.path.join(self.game.assets_dir, "tchars.png"))
        self.image_width, self.image_height = self.image.get_size()
        self.tile_width, self.tile_height = 64, 64
        self.sprite_table = []
        for tile_y in range(0, self.image_height//self.tile_height): #split image into rows by tile height
            for tile_x in range(0, self.image_width//self.tile_width):  #split rows into tiles by tile width
                rect = (tile_x*self.tile_width, tile_y*self.tile_height, 
                self.tile_width, self.tile_height)  #set tile location on screen
                self.sprite_table.append(self.image.subsurface(rect))  #add tile to the map list

    def draw_character(self, char_sprites, display):
         #set up variables for animation frames
        hero_frame_one = self.sprite_frame
        hero_frame_two = self.sprite_frame + 1
        #flip back and forth every 30 ticks
        if self.animationCounter <= 2:
            display.blit(self.sprite_table[hero_frame_one], (448, 448))
        elif self.animationCounter >= 3:
            display.blit(self.sprite_table[hero_frame_two], (448, 448)) 

    def update(self, actions):
        #advance counter for animation
        if self.animationCounter < 4:
            self.animationCounter += 1
        elif self.animationCounter >= 4:
            self.animationCounter = 1

        if actions["up"]:
            self.sprite_frame = 4
        elif actions["down"]:
            self.sprite_frame = 0
        elif actions["left"]:
            self.sprite_frame = 2
        elif actions["right"]:
            self.sprite_frame = 6
        #elif event.key == pygame.K_RETURN:
        #elif event.key == pygame.K_ESCAPE:

    def render(self, display):
        self.draw_character(self.sprite_table, display)
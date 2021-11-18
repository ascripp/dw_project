#------------------------- Import libraries
import os, sys, math, pygame
from pygame.locals import *

#------------------------- Global variables and initialize modules
#initialize pygame
pygame.init()
#initialize clock for timing
fpsClock = pygame.time.Clock()   
#initialize display at 960 pixels square for a 15 x 15 grid of 64 pixel square tiles
gameScreen = pygame.display.set_mode((960, 960))  
#simple name for the window  
pygame.display.set_caption('Dragon Warrior Pygame') 
#start counter at 0 - used for animations
counter = 0


#------------------------- Classes and functions
class Character:

    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.sprite_frame = 0

    def set_stats(self, level, xp, maxhp, maxmp, strength, agility):
        self.level = level
        self.xp = xp
        self.maxhp = maxhp
        self.maxmp = maxmp
        self.strength = strength
        self.agility = agility
        self.attack = self.strength + self.weapon
        self.defence = math.floor(self.agility / 2) + self.armor + self.shield

    def get_stats(self):
        self.stats = [self.level, self.xp, self.maxhp, self.maxmp, self.strength, \
        self.agility, self.attack, self.defence]
        return self.stats

    def set_gear(self, weapon, armor, shield):
        self.weapon = weapon
        self.armor = armor
        self.shield = shield

    def get_gear(self):
        self.gear = [self.weapon, self.armor, self.shield]
        return self.gear

class Map:

    def __init__(self, mapname):
        self.mapname = []
        with open(mapname + '.maptiles') as mapfile:
            self.mapname = list(map(int, mapfile.read().split('\n')))

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
    
    def draw_map(self, terrain_tiles):
        x = 0
        x_position = 0
        y_position = 0
        #draw 15 x 15 square visible portion of map
        for a in range(0, 15):
            for b in range(0, 15):
                gameScreen.blit(terrain_tiles[self.current_map[x]], (x_position, y_position))
                x_position += 64
                x += 1
            x_position = 0
            y_position += 64

def load_tileset(filename, width, height):
    #load image
    image = pygame.image.load(filename)
    #get size of image and store
    image_width, image_height = image.get_size()
    #initialize list to hold tiles
    tile_table = []
    #load tiles into list
    for tile_y in range(0, image_height//height): #split image into rows by tile height
        for tile_x in range(0, image_width//width):  #split rows into tiles by tile width
            rect = (tile_x*width, tile_y*height, width, height)  #grab a tile
            tile_table.append(image.subsurface(rect))  #add tile to the map list
    #return the list
    return tile_table

def draw_characters():
    #set up variables for animation frames
    hero_frame_one = hero.sprite_frame
    hero_frame_two = hero.sprite_frame + 1
    #flip back and forth every 7 ticks
    if counter < 16:
        gameScreen.blit(char_sprites[hero_frame_one], (448, 448))
    elif counter >= 16:
        gameScreen.blit(char_sprites[hero_frame_two], (448, 448))


def do_movement(current_map):
    #create list of collision tiles
    uncrossable_tiles = []
    with open('forbidden.maptiles') as mapfile:
        uncrossable_tiles = list(map(int, mapfile.read().split('\n')))
    #check for keypresses and act accordingly
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                hero.sprite_frame = 4
                if current_map[97] not in uncrossable_tiles:
                    hero.y_position -= 1
            elif event.key == K_DOWN:
                hero.sprite_frame = 0
                if current_map[127] not in uncrossable_tiles:
                    hero.y_position += 1
            elif event.key == K_LEFT:
                hero.sprite_frame = 2
                if current_map[111] not in uncrossable_tiles:
                    hero.x_position -= 1
            elif event.key == K_RIGHT:
                hero.sprite_frame = 6
                if current_map[113] not in uncrossable_tiles:
                    hero.x_position += 1
            #elif event.key == K_RETURN:
            elif event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


#------------------------- Instantiate classes outside of game loop
#create class for hero passing in start location
hero = Character(46, 47)
#create initial map starting in the overworld
level_map = Map('overworld')
#------------------------- Initialize external data
#load tiles into list - all maps use same tiles
terrain_tiles = load_tileset("tiles.png", 64, 64)
#load sprites - all characters are in the same spritesheet
char_sprites = load_tileset("tchars.png", 64, 64)


#start game loop
while True:
    #load the base map into a list
    level_map.load_map(hero.x_position, hero.y_position)
    #draw the visible portion of the map on the screen
    level_map.draw_map(terrain_tiles)
    #draw character on screen
    draw_characters()
    #load a copy of the current base map
    move_map = level_map.get_map()
    #move the character on current map
    do_movement(move_map)
    #update all display elements
    pygame.display.update()
    #recycling counter for animation
    if counter < 30:
        counter += 1
    elif counter >= 30:
        counter = 1
    #update the clock - limited to 30 fps
    fpsClock.tick(60)
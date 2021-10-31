import os, sys, pygame
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

gameScreen = pygame.display.set_mode((960, 960))
pygame.display.set_caption('Dragon Warrior Pygame')

overworld = []
with open('overworld.txt') as mapfile:
    overworld = list(map(int, mapfile.read().split('\n')))

tantagel = []
with open('tantagel.txt') as mapfile:
    tantagel = list(map(int, mapfile.read().split('\n')))

x_offset = 15
y_offset = 0
counter = 0


class Character:

	def __init__(self, x_position, y_position):
		self.x_position = x_position
		self.y_position = y_position
		self.sprite_frame = 0

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

def load_map(mapname, x_off, y_off):
	# initialize variables
	x_off = x_off - 7  #x and y offsets to place character in the middle of the screen
	y_off = y_off - 7
	temp_map = mapname
	current_map = []
	map_width = mapname[-1]  #the last index in the list is the width of the map

	for a in range(0, 15):
		for b in range(0, 15):
			current_map.append(temp_map[x_off + (y_off * map_width)] - 1)
			x_off += 1
		y_off += 1
		x_off -= 15

	return current_map

def draw_map(current_map):
	x = 0
	x_position = 0
	y_position = 0

	for a in range(0, 15):
		for b in range(0, 15):
			gameScreen.blit(terrain_tiles[current_map[x]], (x_position, y_position))
			x_position += 64
			x += 1
		x_position = 0
		y_position += 64

def draw_characters():

	hero_frame_one = hero.sprite_frame
	hero_frame_two = hero.sprite_frame + 1

	if counter < 7:
		gameScreen.blit(char_sprites[hero_frame_one], (448, 448))
	elif counter >= 7:
		gameScreen.blit(char_sprites[hero_frame_two], (448, 448))


def do_movement(current_map):

	#create list of collision tiles
	uncrossable_tiles = []
	with open('forbidden.txt') as mapfile:
	    uncrossable_tiles = list(map(int, mapfile.read().split('\n')))

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
			elif event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()



terrain_tiles = load_tileset("tiles.png", 64, 64)
char_sprites = load_tileset("tchars.png", 64, 64)

hero = Character(46, 47)


while True:


	level_map = load_map(overworld, hero.x_position, hero.y_position)

	draw_map(level_map)

	draw_characters()

	pygame.display.update()

	do_movement(level_map)

	if counter < 15:
		counter += 1
	elif counter >= 15:
		counter = 1


	fpsClock.tick(30)





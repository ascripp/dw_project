def testfunc(self):
    for tile_y in range(0, self.baseimage_height//self.basetile_height):
        for tile_x in range(0, self.baseimage_width//self.basetile_width): 
            rect = (tile_x*self.basetile_width, tile_y*self.basetile_height, 
            self.basetile_width, self.basetile_height) 
            self.basetile_table.append(self.menubasesheet.subsurface(rect))    
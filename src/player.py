playerData = {
    "x_position": 0
    "y_position": 0
    "sprite_frame": 0
}

self.x_position = x_position
self.y_position = y_position
self.sprite_frame = 0
self.level = level
self.xp = xp
self.maxhp = maxhp
self.maxmp = maxmp
self.strength = strength
self.agility = agility
self.attack = self.strength + self.weapon
self.defence = math.floor(self.agility / 2) + self.armor + self.shield
self.stats = [self.level, self.xp, self.maxhp, self.maxmp, self.strength, \
self.agility, self.attack, self.defence]
self.weapon = weapon
self.armor = armor
self.shield = shield
self.gear = [self.weapon, self.armor, self.shield]

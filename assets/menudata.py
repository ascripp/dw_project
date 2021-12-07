menuLocations = {
    "ministat": [0, 2],
    "main": [6, 1],
    "status": [5, 3]
}

titles = {
    "ministat": "plac",
    "main": "COMMAND",
    "combat": "COMMAND",
    "spell": "SPELL",
    "item": "",
    "status": ""
}

menus = {
    "ministat": [
        1, 2, 2, 3,
        4, 5, 5, 6,
        4, 5, 5, 6,
        4, 5, 5, 6,
        4, 5, 5, 6,
        7, 8, 8, 9,
        4, 6
        ],

    "main": 
        [1, 2, 2, 2, 2, 2, 2, 3,
         4, 5, 5, 5, 5, 5, 5, 6,
         4, 5, 5, 5, 5, 5, 5, 6,
         4, 5, 5, 5, 5, 5, 5, 6,
         7, 8, 8, 8, 8, 8, 8, 9,
         8, 5
         ],

    "status": [
        1, 2, 2, 2, 2, 2, 2, 2, 2, 3,
        4, 5, 5, 5, 5, 5, 5, 5, 5, 6,
        4, 5, 5, 5, 5, 5, 5, 5, 5, 6,
        4, 5, 5, 5, 5, 5, 5, 5, 5, 6,
        4, 5, 5, 5, 5, 5, 5, 5, 5, 6,
        4, 5, 5, 5, 5, 5, 5, 5, 5, 6,
        4, 5, 5, 5, 5, 5, 5, 5, 5, 6,
        4, 5, 5, 5, 5, 5, 5, 5, 5, 6,
        4, 5, 5, 5, 5, 5, 5, 5, 5, 6,
        4, 5, 5, 5, 5, 5, 5, 5, 5, 6,
        7, 8, 8, 8, 8, 8, 8, 8, 8, 9,
        10, 11
        ],
        
}

menuOptions = {
    "main": [
    {'text': "TALK", 'xloc': 1, 'yloc': 1, 'action': 'talk'}, 
    {'text': "STATUS", 'xloc': 1, 'yloc': 2, 'action': 'status'}, 
    {'text': "STAIRS", 'xloc': 1, 'yloc': 3, 'action': 'stairs'}, 
    {'text': "SEARCH", 'xloc': 1, 'yloc': 4, 'action': 'search'}, 
    {'text': "SPELL", 'xloc': 5, 'yloc': 1, 'action': 'spell'}, 
    {'text': "ITEM", 'xloc': 5, 'yloc': 2, 'action': 'item'}, 
    {'text': "DOOR", 'xloc': 5, 'yloc': 3, 'action': 'door'}, 
    {'text': "TAKE", 'xloc': 5, 'yloc': 4, 'action': 'take'}
    ],

    "status": [
    {'text': "NAME:", 'xloc': 3, 'xloc_r': 9, 'yloc': .5, 'action': 'pass'},
    {'text': "STRENGTH:", 'xloc': 3.5, 'xloc_r': 9, 'yloc': 1.5, 'action': 'pass'},
    {'text': "AGILITY:", 'xloc': 4, 'xloc_r': 9, 'yloc': 2.5, 'action': 'pass'},
    {'text': "MAXIMUM HP:", 'xloc': 2.5, 'xloc_r': 9, 'yloc': 3.5, 'action': 'pass'},
    {'text': "MAXIMUM MP:", 'xloc': 2.5, 'xloc_r': 9, 'yloc': 4.5, 'action': 'pass'},
    {'text': "ATTACK POWER:", 'xloc': 1.5, 'xloc_r': 9, 'yloc': 5.5, 'action': 'pass'},
    {'text': "DEFENSE POWER:", 'xloc': 1, 'xloc_r': 9, 'yloc': 6.5, 'action': 'pass'},
    {'text': "WEAPON:", 'xloc': 1.5, 'xloc_r': 9, 'yloc': 7.5, 'action': 'pass'},
    {'text': "ARMOR:", 'xloc': 2, 'xloc_r': 9, 'yloc': 8.5, 'action': 'pass'},
    {'text': "SHIELD:", 'xloc': 1.5, 'xloc_r': 9, 'yloc': 9.5, 'action': 'pass'}
    ],

    "ministat": [
    {'text': "LV", 'xloc': .5, 'yloc': 1, 'action': 'pass'},
    {'text': "HP", 'xloc': .5, 'yloc': 2, 'action': 'pass'},
    {'text': "MP", 'xloc': .5, 'yloc': 3, 'action': 'pass'},
    {'text': "G", 'xloc': .5, 'yloc': 4, 'action': 'pass'},
    {'text': "E", 'xloc': .5, 'yloc': 5, 'action': 'pass'},
    ]
}

alphabet = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
    "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26,
    "a": 27, "b": 28, "c": 29, "d": 30, "e": 31, "f": 32, "g": 33, "h": 34, "i": 35, "j": 36, "k": 37, "l": 38, "m": 39,
    "n": 40, "o": 41, "p": 42, "q": 43, "r": 44, "s": 45, "t": 46, "u": 47, "v": 48, "w": 49, "x": 50, "y": 51, "z": 52,
    "0": 53, "1": 54, "2": 55, "3": 56, "4": 57, "5": 58, "6": 59, "7": 60, "8": 61, "9": 62, ".": 63, ",": 64, """: 65,
    """: 66, "'": 67, "'": 68, "?": 69, "!": 70, "*": 71, "&": 72, "(": 73, ")": 74, "-": 75, ":": 76, ";": 77, " ": 78,
    "cursor": 79, "more": 80
}
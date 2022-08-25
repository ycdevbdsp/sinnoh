from PyQt5.QtGui import QColor

#MAP EXTENT VALUES
MAP_WIDTH = 32
MAP_HEIGHT = 32

#COLORS
alpha = int(255*0.25)
GRIDLINE = QColor(0, 0, 0)
BLACK = QColor(0, 0, 0, alpha)
BLUE = QColor(0, 255, 247, alpha)
GREEN = QColor(0, 255, 0, alpha)
WHITE = QColor(255, 255, 255, alpha)
ORANGE = QColor(250, 124, 4, alpha)
RED = QColor(255, 0, 0, alpha)
YELLOW = QColor(255, 252, 5, alpha)
SELECTED = QColor(255, 255, 0, 255)


#COLLISION VALUES
COLLISIONS = {
    'UNKNOWN': -1,
    'WALKABLE': 0,
    'WALL': 128,
    'GRASS': 2000,
    'TALLGRASS': 3000,
    'GRASS2': 4000,
    'GRASS3': 5000,
    'PONDWATER': 16000,
    'OCEANWATER': 21000,
    'PUDDLE': 22000,
    'WALKABLEWATER': 23000,
    'PUDDLE2': 24000,
    'SAND': 33000,
    'LEDGERIGHT': 56128,
    'LEDGELEFT': 57128,
    'LEDGEDOWN': 59128,
    'LEDGEDOWNLEFT': 63128,
    'ROCKCLIMBVERT': 75128,
    'ROCKCLIMBHORI': 76128,
    '???': 99128,
    'PASSAGEUP': 101000,
    'DOOR?': 105128,
    'PASSAGELEFT': 108000,
    'PASSAGERIGHT': 109000,
    'PASSAGEDOWN': 110000,
    'TREEENTER': 110128,
    'BRIDGESTART?': 112000,
    'BRDGOVRGRND': 113000,
    'BRDGOVRWATER': 115000,
    'BIKELEDGERIDE': 118000,
    'BIKELEDGEHORI': 124000,
    'BERRYSOIL': 160128,
    'SINKSNOW': 161000,
    'SINKSNOWPRMTR': 162000,
    'MUD': 164000,
    'SNOW': 168000,
    'GRASSINSNOW': 169000,
    'BIKERACK': 219128,
    -1: 'UNKNOWN',
    0: 'WALKABLE',
    128: 'WALL',
    2000: 'GRASS',
    3000: 'TALLGRASS',
    4000: 'GRASS2',
    5000: 'GRASS3',
    16000: 'PONDWATER',
    21000: 'OCEANWATER',
    22000: 'PUDDLE',
    23000: 'WALKABLEWATER',
    24000: 'PUDDLE2',
    33000: 'SAND',
    56128: 'LEDGERIGHT',
    57128: 'LEDGELEFT',
    59128: 'LEDGEDOWN',
    63128: 'LEDGEDOWNLEFT',
    75128: 'ROCKCLIMBVERT',
    76128: 'ROCKCLIMBHORI',
    99128: '???',
    101000: 'PASSAGEUP',
    105128: 'DOOR?',
    108000: 'PASSAGELEFT',
    109000: 'PASSAGERIGHT',
    110000: 'PASSAGEDOWN',
    110128: 'TREEENTER',
    112000: 'BRIDGESTART?',
    113000: 'BRDGOVRGRND',
    115000: 'BRDGOVRWATER',
    118000: 'BIKELEDGERIDE',
    124000: 'BIKELEDGEHORI',
    160128: 'BERRYSOIL',
    161000: 'SINKSNOW',
    162000: 'SINKSNOWPRMTR',
    164000: 'MUD',
    168000: 'SNOW',
    169000: 'GRASSINSNOW',
    219128: 'BIKERACK'
}


PLACEDATA_BLANK = {
    "ID": "",
    "zoneID": 0,
    "TrainerID": 0,
    "ObjectGraphicIndex": 1,
    "ColorIndex": 0,
    "Position": {
        "x": 0,
        "y": 0
    },
    "HeightLayer": 1,
    "HeightIgnore": 0,
    "Size": {
        "x": 0,
        "y": 0
    },
    "Rotation": 90,
    "MoveLimit": {
        "x": 1,
        "y": 0
    },
    "EventType": 0,
    "MoveCode": 3,
    "MoveParam0": 0,
    "MoveParam1": 0,
    "MoveParam2": 0,
    "TalkLabel": "",
    "ContactLabel": "",
    "Work": 4000,
    "Dowsing": 0,
    "LoadFirst": 0,
    "DoNotLoad": 4000,
    "TalkToRange": 1.25,
    "TalkToSize": {
        "x": 0,
        "y": 0
    },
    "TalkBit": 15
}

PLACEDATA_NEW = {
    "filename": "",
    "index": -1,
    "data": PLACEDATA_BLANK
}

ROTATION_UP = 180
ROTATION_DOWN = 0
ROTATION_LEFT = 90
ROTATION_RIGHT = 270

ROTATION = {
    0: "DOWN",
    90: "LEFT",
    180: "UP",
    270: "RIGHT"
}
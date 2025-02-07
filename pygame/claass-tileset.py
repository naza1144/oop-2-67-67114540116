import json
import pygame

def load_tileset(fname):
    with open(fname, 'r') as f:
        data = json.load(f)
    return data

class Tile(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class Layer(object):
    def __init__(self, **data):
        self.tiles = []
        for tile in data['tiles']:
            t = Tile(**tile)  # Use Tile class instead of tile function
            self.tiles.append(t)  # Use lowercase tiles
        data.pop('tiles')
        self.__dict__.update(data)


import base64, io
from PIL import Image  # Change the import

def strToImage(v):
    b = base64.b64decode(v[22:])
    bb = io.BytesIO(b)
    img = Image.open(bb)  # Use Image.open instead of Image constructor
    return pygame.image.fromstring(img.tobytes(), img.size, img.mode)


class Tileset(object):
    def __init__(self, fname='Tiny_Swords/map.json'):
        data = load_tileset(fname)
        self.layers = []
        for layer in data['layers']:
            _layer = Layer(**layer)  # Add ** here
            self.layers.append(_layer)  # Also add this line to store the layer
        self.spriteSheets = {}
        for k, v in data['spriteSheets'].items():
            self.spriteSheets[k] = strToImage(v)
        self.names = list(self.spriteSheets.keys())
        self.name_index = 0
        data.pop('layers')
        data.pop('spriteSheets')
        self.__dict__.update(data)

    def show_spritesheet_name(self, font,screen):
        name = self.names[self.name_index]
        text = font.render(name, True, 30)
        screen.blit(text, (20, 550))

    def show_fps(self, font, screen, clock):
        massge = f"FPS: {clock.get_fps():.2f} fps"
        text = font.render(massge, True, 30)
        screen.blit(text, (800-text.get_width(), 550))

    def drwaw(self, screen):
        name = self.names[self.name_index]
        screen.blit(self.spriteSheets[name], (10, 20))

    def up(self):
        self.name_index = (self.name_index + 1) % len(self.names)

    def down(self):
        self.name_index = (self.name_index - 1) % len(self.names)



from pygame.locals import * 
from pygame.font import Font

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
logo = pygame.image.load('Tiny_Swords\pngtree-cute-rat-isolated-png-image_13147967.png')
pygame.display.set_icon(logo)
pygame.display.set_caption('Rattatuie')
font = Font('Monoton\Monoton-Regular.ttf', 20)
runing = True
Tileset = Tileset()
clock = pygame.time.Clock()
running = True

 
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            break
        elif e.type == pygame.KEYDOWN:
            if e.key in [K_LEFT, K_DOWN]:
                Tileset.down()
            elif e.key in [K_RIGHT, K_UP]:
                Tileset.up()

    screen.fill((160, 160, 160))
    # In the main loop, change:
    Tileset.show_spritesheet_name(font, screen)
    Tileset.show_fps(font, screen, clock)
    Tileset.drwaw(screen)

    clock.tick(60)
    pygame.display.flip()
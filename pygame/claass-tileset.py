import json

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


class Tileset(object):
    def __init__(self, fname='Tiny_Swords/map.json'):
        data = load_tileset(fname)
        self.layers = []
        for layer in data['layers']:
            _layer = Layer(**layer)  # Add ** here
            self.layers.append(_layer)  # Also add this line to store the layer
        self.spriteSheets = {}
        data.pop('layers')
        data.pop('spriteSheets')
        self.__dict__.update(data)

t = Tileset()
for layer in t.layers:
    print(layer.id, layer.name)

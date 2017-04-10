from ships import Carrier, Battleship, Submarine, Cruiser, Patrol
from player import Player

class Game:
    grid = {(x,y) for x in range(10) for y in range(10)}

    def __init__(self, **kwargs):
        self.first = kwargs.get("first", "Player One")
        self.second = kwargs.get("second", "Player Two")
        self.board_size = kwargs.get("size", 10)  

    def translate_coord(self, string):
        letter = string[0]
        number = string[1:]
        x = ord(letter) - ord('a')
        y = abs(int(number) - self.board_size)
        return x, y

    def get_ship_length(self, name):
        pass
    
    def line(self, point, vector, length):
        horizontal, vertical = vector
        step = 1 if max(vector) == 1 else -1
        step_start, anchor = point if horizontal else point[::-1]
        step_stop = step_start + length if 1 == step else step_start - length
        run = range(step_start, step_stop, step)
        a, b = run, [anchor] if horizontal else [anchor], run
        return {(x, y) for x in a for y in b}

    def get_ship(self, coord_set):
        len(coord_set)
        pass
        
    def place_ship(self, coord, vector, length, name):
        point = self.translate_coord(coord)
        shipline = line(point, vector, length)
        if not shipline - grid:
           grid = grid - shipline 
           ship = get_ship(name, shipline) 

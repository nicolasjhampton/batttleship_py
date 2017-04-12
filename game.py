from player import Player

class Game:

    turn = False

    def __init__(self, **kwargs):
        self.first = kwargs.get("first", Player("First"))
        self.second = kwargs.get("second", Player("Second"))

    def translate_coord(self, string):
        """Turns the letter/number string input from the user into 
        coordinates for the grid model"""
        letter = string[0]
        number = string[1:]
        x = ord(letter) - ord('a')
        y = abs(int(number) - self.board_size)
        return x, y
 
    def line(self, point, vector, length):
        horizontal, vertical = vector
        step = 1 if max(vector) == 1 else -1
        step_start, anchor = point if horizontal else point[::-1]
        step_stop = step_start + length if 1 == step else step_start - length
        run = range(step_start, step_stop, step)
        a, b = run, [anchor] if horizontal else [anchor], run
        return {(x, y) for x in a for y in b}

    def get_player(self):
        return self.first if self.turn else self.second

    def get_next_player(self):
        self.turn = not self.turn
        return get_player()

    def get_ship(self, player):
        try:
            ship = player.next_ship()
        except ValueError:
            raise ValueError("{} is out of ships".format(player.name))
        else:
            return ship
        
    def place_ship(self, player, coord, vector):
        player = self.first if self.turn else self.second
        point = self.translate_coord(coord)
        try:
            ship = player.pop_ship()      
        except IndexError:
            return -1
        else:
            shipline = line(point, vector, ship.get_size())
            if not shipline - player.get_grid():
                ship.set_state(shipline)
                player.set_ship(ship)
                return 1
            else:
                player.put_ship_back(ship)
                return -1
                



 

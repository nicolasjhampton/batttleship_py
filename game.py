from player import Player

class Game:

    turn = False
 
    def __init__(self, **kwargs):
        self.first = kwargs.get("first", Player(name="First"))
        self.second = kwargs.get("second", Player(name="Second"))

    def __str__(self):
        return "Game: {}'s turn against {}.".format(self.first.name, 
                                                    self.second.name)

    def translate_coord(self, coord):
        """Turns the letter/number string input from the user into
        coordinates for the grid model"""
        letter = coord[0]
        number = coord[1:]
        x = ord(letter) - ord('a')
        y = abs(int(number) - 10)
        return x, y

    def line(self, point, vector, length):
        horizontal, vertical = vector
        step = 1 if max(vector) == 1 else -1
        step_start, anchor = point if horizontal else point[::-1]
        step_stop = step_start + length if 1 == step else step_start - length
        run = range(step_start, step_stop, step)
        anchor = [anchor]
        b = anchor if horizontal else run
        a = run if horizontal else anchor
        return {(x, y) for x in a for y in b}

    def get_player(self):
        return self.first if self.turn else self.second

    def get_next_player(self):
        self.turn = not self.turn
        return self.get_player()

    def get_ship(self, player):
        try:
            ship = self.get_player().next_ship()
        except ValueError:
            return 0
        else:
            return ship

    def place_ship(self, player, coord, vector):
        player = self.get_player()
        point = self.translate_coord(coord)
        try:
            ship = player.pop_ship()
        except IndexError:
            return 0
        else:
            shipline = self.line(point, vector, ship.get_size())
            if not shipline - player.get_grid():
                ship.set_state(shipline)
                player.set_ship(ship)
                return 1
            else:
                player.put_ship_back(ship)
                return -1





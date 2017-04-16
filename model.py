from player import Player

class Model:
    def __init__(self, **kwargs):
        self.players = []
        self.turn = False

    def __str__(self):
        return "Game: {}'s turn against {}.".format(self.players[0].name,
                                                    self.players[1].name)

    def set_player(self, name):
        formatted_name = name[:10].strip().title()
        player = Player(name=formatted_name)
        self.players.append(player)

    def translate_coord(self, coord):
        """Turns the letter/number string input from the user into
        coordinates for the grid model"""
        letter = coord[0]
        number = coord[1:]
        x = ord(letter) - ord('a')
        y = int(number) - 1
        return x, y

    def translate_direction(self, direction):
        if direction == 'u':
            return (0, -1)
        elif direction == 'r':
            return (1, 0)
        elif direction == 'd':
            return (0, 1)
        elif direction == 'l':
            return (-1, 0)

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
        return self.players[0] if self.turn else self.players[1]

    def get_opponent(self):
        return self.players[1] if self.turn else self.players[0]

    def get_next_player(self):
        self.turn = not self.turn
        return self.get_player()

    def get_ship(self):
        try:
            ship = self.get_player().next_ship()
        except ValueError:
            return 0
        else:
            return ship

    def get_current_board(self):
        player = self.get_player()
        return {
            "grid": player.get_grid(),
            "guesses": player.get_guesses()
        }

    def place_ship(self, coord, direction):
        player = self.get_player()
        point = self.translate_coord(coord)
        vector = self.translate_direction(direction)
        try:
            ship = player.pop_ship()
        except IndexError:
            return 0
        else:
            shipline = self.line(point, vector, ship.get_size())
            grid = player.get_grid()
            if not shipline - grid["spaces"]:
                ship.set_state(shipline)
                player.set_ship(ship)
                return 1
            else:
                player.put_ship_back(ship)
                return -1

    def fire(self, coord):
        hit = 0
        player = self.get_player()
        opponent = self.get_opponent()
        point = self.translate_coord(coord)
        fleet = opponent.get_fleet()
        for ship in fleet:
            result = ship.is_hit(point)
            if abs(result) == 1:
                player.log_hit(point)
                hit = result
                break
        if not hit:
            player.log_miss(point)
        return hit

    def is_win(self):
        player = self.get_player()
        hits = player.get_guesses()["hits"]
        if len(hits) == 17:
            return True
        else:
            return False

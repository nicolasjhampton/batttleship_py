from ships import Carrier, Battleship, Submarine, Cruiser, Patrol


class Player:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "Player")
        self.guesses = {
            "hits": [],
            "misses": []
        }
        self.grid = {
            "spaces": {
                (x, y) for x in range(10) for y in range(10)
            },
            "fleet": []
        }
        self.ships = [
            Carrier(),
            Battleship(),
            Cruiser(),
            Submarine(),
            Patrol()
        ]

    def __str__(self):
        return "Player {} has hit {} times and missed {} shots".format(
            self.name, len(self.guesses["hits"]), len(self.guesses["misses"]))

    def get_grid(self):
        return self.grid

    def get_fleet(self):
        return self.grid["fleet"]

    def get_guesses(self):
        return self.guesses

    def get_name(self):
        return self.name.title()

    def get_ships(self):
        def ship_key(ship):
            size = ship.get_size()
            name = ship.get_name()
            return size, name
        if self.ships:
            self.ships.sort(key=ship_key, reverse=True)
        return self.ships

    def next_ship(self):
        ship = self.get_ships()[0]
        return ship.get_name(), ship.get_size()

    def pop_ship(self):
        return self.get_ships().pop(0)

    def put_ship_back(self, ship):
        self.ships.insert(0, ship)

    def set_ship(self, ship):
        position, toss, axis = ship.get_state()
        self.grid["spaces"] -= set(position)
        self.grid["fleet"].append(ship)

    def log_miss(self, miss):
        misses = self.guesses["misses"]
        misses.append(miss)

    def log_hit(self, hit):
        hits = self.guesses["hits"]
        hits.append(hit)

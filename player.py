from ships import Carrier, Battleship, Submarine, Cruiser, Patrol

class Player:

    grid = {
        "spaces": {
            (x,y) for x in range(10) for y in range(10)
        },
        "fleet": []
    }

    ships = [
        Carrier(),
        Battleship(),
        Cruiser(),
        Submarine(),
        Patrol()
    ]

    guesses = {
        "hits": [],
        "misses": []
    }

    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "Player")
    
    def __str__(self):
        return "Player {} has hit {} times and missed {} shots".format(
            self.name, len(self.guesses["hits"]), len(self.guesses["misses"])) 

    def get_ships(self):
        def ship_key(ship):
            size = ship.get_size()
            name = ship.get_name()
            return size, name
        self.ships.sort(key=ship_key, reverse=True)
        return self.ships

    def next_ship(self):
        ship = self.get_ships()[0]
        return ship.get_name(), ship.get_size()

    def pop_ship(self):
        return self.get_ships().pop(0)

    def get_grid(self):
        return self.grid["spaces"]

    def put_ship_back(self, ship):
        self.ships.insert(0, ship)

    def set_ship(self, ship):
        position, toss = ship.get_state()
        self.grid["spaces"] -= set(position)
        self.grid["fleet"].append(ship) 

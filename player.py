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

    def ship_key(ship):
        return ship.get_size(), ship.get_name

    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "Player")
    
    def get_ships(self):
        return sort(self.ships, key=ship_key)

    def next_ship(self):
        ship = self.get_ships()[0]
        return ship.get_name(), ship.get_size()

    def pop_ship(self):
        return self.get_ships().pop()
   
    def get_grid(self):
        return self.grid["spaces"]

    def set_ship(self, ship):
        position, toss = ship.get_state()
        self.grid["spaces"] -= set(position)
        self.grid["fleet"].append(ship) 

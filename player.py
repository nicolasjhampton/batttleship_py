

class Player:

    grid = tuple((x,y) for x in range(10) for y in range(10))
    
    guesses = {
        "hits": [],
        "misses": []
    }


    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "Player")
        self.ships = []

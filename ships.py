from functools import reduce

class Ship:
    
    size = 1
    hits = []

    def __init__(self, *args):
        self.is_valid_ship(args)  
        self.position = args
        self.left = list(self.position)
    
    def __str__(self):
        return "{} from {} to {} taken {} damage".format(
            self.name.title(),
            self.position[0],
            self.position[-1],
            len(self.hits))

    def is_valid_ship(self, points):
        """Tests ship for correct coordinates. Ship has to be straight,
        solid, continuous, and have the correct length (unique)"""
        xAxis = {x for x, y in points}
        yAxis = {y for x, y in points}
        run = xAxis if xAxis > yAxis else yAxis
        width = yAxis if xAxis > yAxis else xAxis
        straight = len(width) == 1
        unique = len(run) == self.size
        diff = reduce(lambda x, y: x + y, range(len(run)))
        continuous = (max(run) * len(run) - sum(run)) == diff
        if not straight or not unique or not continuous:
            raise ValueError("{} has inconsistent coords".format(self.name))
        if not len(points) == self.size:
            raise ValueError("Wrong size ({}) entered for {}.".format(
                                len(points), 
                                self.__class__.__name__))
        
    def is_hit(self, point):
        """Returns falsy if miss, truthy if hit, and updates the ship"""
        try:
            hit = self.left.index(point)
        except ValueError:
            return 0;
        else:
            self.hits.append(self.left.pop(hit))
            if not self.left:
                return -1
            else:
                return 1
    
    def report(self):
        """Gives information needed to draw ship"""
        return (sorted(self.position), self.hits[:])

class Carrier(Ship):
    size = 5
    name = "aircraft carrier"

class Battleship(Ship):
    size = 4
    name = "battleship"

class Submarine(Ship):
    size = 3
    name = "submarine"

class Crusier(Ship):
    size = 3
    name = "crusier"

class Patrol(Ship):
    size = 2
    name = "patrol ship"

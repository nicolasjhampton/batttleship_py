from functools import reduce, partial

class Ship:

    TYPES = {
        "Carrier": 5,
        "Battleship": 4,
        "Submarine": 3,
        "Cruiser": 3,
        "Patrol": 2
    }

    def __str__(self):
        try:
            position, hits = self.get_state()
        except (AttributeError, TypeError) as e:
            return "{} has not been placed.".format(self.get_name())
        else:
            line = sorted(list(position))
            return "{} from {} to {} taken {} damage".format(
                       self.get_name(),
                       line[0],
                       line[-1],
                       len(hits))

    def get_name(self):
        return self.__class__.__name__

    def get_size(self):
        """Returns the correct ship size for each type of ship"""
        return self.TYPES[self.get_name()]

    def is_valid(self, points):
        """Tests ship for correct coordinates. Ship has to be straight,
        solid, continuous, and have the correct length (unique)"""
        size = self.get_size()
        xAxis = {x for x, y in points}
        yAxis = {y for x, y in points}
        width = xAxis if len(xAxis) < len(yAxis) else yAxis
        run = yAxis if len(xAxis) < len(yAxis) else xAxis
        straight = len(width) == 1
        unique = len(run) == size
        diff = reduce(lambda x, y: x + y, range(len(run)))
        continuous = (max(run) * len(run) - sum(run)) == diff
        if not straight or not unique or not continuous:
            raise ValueError("{} has inconsistent coords".format(self.get_name()))
        if not len(points) == size:
            raise ValueError("Wrong size ({}) entered for {}.".format(
                                len(points),
                                self.get_name()))
        return sorted(points)

    def set_state(self, args):
        """sets the coordinates of the ship on the board"""
        position = self.is_valid(args)
        self.position = partial(lambda x: x, args)
        self.hits = partial(lambda x: x, [])

    def get_state(self):
        """Gives information needed to draw ship"""
        try:
            return sorted(list(self.position())), sorted(list(self.hits()))
        except AttributeError:
            return -1

    def is_hit(self, point):
        """Returns falsy if miss, truthy if hit, and updates the ship"""
        position, hits = self.get_state()
        previously_sunk = len(position) == len(hits)
        previously_hit_point = point in hits
        if previously_hit_point or previously_sunk:
            return 0
        try:
            position.index(point)
        except ValueError:
            return 0
        else:
            new_hits = [point] + hits
            self.hits = partial(lambda args: args, new_hits)
            sunk = len(new_hits) == len(position)
            return -1 if sunk else 1


class Carrier(Ship):
    pass


class Battleship(Ship):
    pass


class Submarine(Ship):
    pass


class Cruiser(Ship):
    pass


class Patrol(Ship):
    pass

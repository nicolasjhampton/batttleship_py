SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

BOARD_SIZE = 10

SHIP = u"\u2588"
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'


def clear_screen():
    print("\033c", end="")


def print_board_heading():
    print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))


def print_board(board):
    print_board_heading()

    row_num = 1
    for row in board:
        print(str(row_num).rjust(2) + " " + (" ".join(row)))
        row_num += 1


def map_spaces(game):
    board = []
    for y in range(10):
        row = []
        for x in range(10):
            sprite = get_space_sprite(game, (x, y))
            row.append(sprite)
        board.append(row)
    return game, board


def get_ship_sprites(position, hits):
    if len(position) == len(hits):
        return SUNK, SUNK
    else:
        return SHIP, HIT

def get_space_sprite(game, point):
    return EMPTY if game.check_spaces(point) else " "

def map_ships(args):
    game, board = args
    fleet = game.get_fleet()
    for ship in fleet:
        position, hits = ship.get_state()
        positive, negative = get_ship_sprites(position, hits)
        for x, y in position:
            board[y][x] = positive
        for x, y in hits:
            board[y][x] = negative
    return board


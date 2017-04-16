class Display:

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

    def __init__(self):
        pass

    def clear_screen(self):
        print("\033c",end="")

    def print_board_heading(self):
        print("|   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + self.BOARD_SIZE)]) + "|")

    def print_board(self, board):
        self.print_board_heading()

        row_num = 1
        for row in board:
            print("|" + str(row_num).rjust(2) + " " + (" ".join(row)) + "|")
            row_num += 1

    def prompt_player(self, index):
        print("Please enter name for player {}:".format(index))
        return input("> ")[:10].strip()

    def player_switch(self, player):
        self.clear_screen()
        message = "It\'s {}\'s turn! \n".format(player.get_name())
        message += "Please switch admirals now and keep your ships hidden..."
        input(message)

    def generate_blank_board(self):
        row = [self.EMPTY for x in range(self.BOARD_SIZE)]
        return [row[:] for y in range(self.BOARD_SIZE)]

    def map_sprite(self, board, input, sprite):
        for x, y in input:
            board[y][x] = sprite
        return board

    def get_ship_sprites(self, position, hits):
        if len(position) == len(hits):
            return self.SUNK, self.SUNK
        else:
            return self.SHIP, self.HIT

    # def get_ship_sprites(self, position, hits):
    #     if len(position) == len(hits):
    #         return self.SUNK, self.SUNK
    #     else:
    #         return self.SHIP, self.HIT

    def map_guesses(self, board, guesses):
        guess_hits = guesses.get("hits")
        guess_misses = guesses.get("misses")
        missed_guesses = self.map_sprite(board, guess_misses, self.MISS)
        full_guesses = self.map_sprite(missed_guesses, guess_hits, self.HIT)
        return full_guesses


    def map_fleet(self, board, fleet):
        for ship in fleet:
            position, hits = ship.get_state()
            positive, negative = self.get_ship_sprites(position, hits)
            ship_placed = self.map_sprite(board, position, positive)
            board = self.map_sprite(ship_placed, hits, negative)
        return board

    def display_board(self, board):
        guesses = board.get("guesses")
        grid_fleet = board.get("grid").get("fleet")

        blank_guesses = self.generate_blank_board()
        blank_grid = self.generate_blank_board()

        full_guesses = self.map_guesses(blank_guesses, guesses)
        filled_grid = self.map_fleet(blank_grid, grid_fleet)

        self.clear_screen()
        print("-"*24)
        self.print_board(full_guesses)
        print("-"*24)
        self.print_board(filled_grid)
        print("-"*24)


    def validate_direction(self, direction):
        direction = direction[0].lower()
        if direction not in ['l', 'r', 'u', 'd']:
            raise ValueError("Invalid direction")
        else:
            return direction

    def validate_coordinate(self, coord):
        column = coord[0].lower()
        row = coord[1:3].strip()
        try:
            number = int(row)
        except ValueError:
            raise ValueError("Invalid row number")
        else:
            if number > 10 or number < 0:
                raise ValueError("Row number out of range")
            else:
                if ord(column) < ord('a') or ord(column) > ord('j'):
                    raise ValueError("Column number out of range")
                else:
                    return column + row

    def enter_direction(self):
        print("Enter a direction:")
        print("Examples: [L]eft, [R]ight, [U]p, [D]own")
        direction = self.validate_direction(input("Enter direction > "))
        return direction

    def enter_coordinate(self):
        print("Enter a column letter and row number:")
        print("Examples: d7, A10, J1")
        coord = self.validate_coordinate(input("Enter coordinate > "))
        return coord

    def enter_ship(self, index):
        print("Place {}:".format(self.SHIP_INFO[index][0]))
        coord = self.enter_coordinate()
        direction = self.enter_direction()
        return coord, direction

    def enter_shot(self):
        print("Batten the hatches! Fire!")
        coord = self.enter_coordinate()
        return coord

    def splash_win(self, player):
        self.clear_screen()
        input("Congratulations {}! You've won!".format(player.get_name()))

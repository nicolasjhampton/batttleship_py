class Display:
   
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
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + self.BOARD_SIZE)]))


    def print_board(self, board):
        self.print_board_heading()

        row_num = 1
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1


    def map_spaces(self, spaces):
        board = []
        for y in range(10):
            row = []
            for x in range(10):
                sprite = self.get_space_sprite(spaces, (x, y))
                row.append(sprite)
            board.append(row)
        return board


    def get_ship_sprites(self, position, hits):
        if len(position) == len(hits):
            return self.SUNK, self.SUNK
        else:
            return self.SHIP, self.HIT

    def get_space_sprite(self, spaces, point):
        return self.EMPTY if point in spaces else " "

    def map_fleet(self, board, fleet):
        for ship in fleet:
            position, hits = ship.get_state()
            positive, negative = self.get_ship_sprites(position, hits)
            for x, y in position:
                board[y][x] = positive
            for x, y in hits:
                board[y][x] = negative
        return board
     

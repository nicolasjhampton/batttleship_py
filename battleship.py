import os

from display import Display
from model import Model

class Battleship:
    def __init__(self):
        self.model = Model()
        self.display = Display()

    def get_player_count(self):
        return len(self.model.players)

    def init_player(self, index):
        self.model.set_player(self.display.prompt_player(index))

    def change_and_announce_player(self):
        self.display.player_switch(self.model.get_next_player())

    def choose_ships(self):
        for x in range(5):
            while True:
                self.display.display_board(self.model.get_current_board())
                try:
                    position = self.display.enter_ship(x)
                except ValueError as e:
                    input("Bad input: {}".format(e))
                else:
                    result = self.model.place_ship(*position)
                    if result == 1:
                        break
                    elif result == -1:
                        input("Ship can't be placed here")
                    elif result == 0:
                        input("Out of ships!")
                        break

    def make_move(self):
        while True:
            self.display.display_board(self.model.get_current_board())
            try:
                shot = self.display.enter_shot()
            except ValueError as e:
                input("Bad input: {}".format(e))
            else:
                result = self.model.fire(shot)
                if result == 1:
                    input("Ship was hit!")
                elif result == 0:
                    input("Missed...")
                elif result == -1:
                    input("Ship hit was sunk!")
                    win = self.model.is_win()
                    return win
                return result

    def win(self):
        self.display.splash_win(self.game.get_player())
        sys.exit()

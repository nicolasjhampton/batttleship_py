#from battleship import print_board, map_ships, map_spaces
from display import Display
from game import Game

game = Game()

display = Display()

print(game.place_ship('a1', (1, 0)))

print(game.place_ship('b3', (1, 0)))

print(game.place_ship('c5', (1, 0)))

print(game.place_ship('a6', (0, 1)))

print(game.place_ship('d7', (1, 0)))

fleet = game.get_fleet()
spaces = game.get_spaces()

display.print_board(display.map_fleet(display.map_spaces(spaces),fleet))            

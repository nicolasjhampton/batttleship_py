from game import Game

game = Game()
player = game.get_player()
ship = game.get_ship(player)
print(game)
print(player)
print(ship)
result = game.place_ship(player, 'a1', (1, 0))
print(result)
print(game.get_ship(player))
print(game.get_ship(player))
result = game.place_ship(player, 'a1', (0, -1))
print(result)
result = game.place_ship(player, 'a2', (0, -1))
print(result)
print(game.get_player().get_grid())
print(player)
print(player.grid["spaces"])
print(player.ships)
result = game.place_ship(player, 'b2', (1, 0))
print(result)
result = game.place_ship(player, 'b3', (1, 0))
print(result)
result = game.place_ship(player, 'a6', (0, -1))
print(result)
result = game.place_ship(player, 'c2', (1, 0))
print(result)
print(game.get_player().get_grid())

from battleship import Battleship

if __name__ == "__main__":
    game = Battleship()

    # Show game splash screen

    # Input for first and second player
    for x in range(2):
        game.init_player(x + 1)

    turns = range(game.get_player_count())

    for x in turns:
        game.change_and_announce_player()
        game.choose_ships()

    # Announce start of game
    while True:
        game.change_and_announce_player()
        win = game.make_move()
        if win is True:
            break

    # Show win screen
    game.win()

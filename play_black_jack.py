from black_jack.games.game import Game

interactive_game = Game(nbr_players=2, nbr_decks=8)
interactive_game.ifu()
interactive_game.print_state()

print()
print()
print()

interactive_game.play()

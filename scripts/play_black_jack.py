from black_jack.games.interactive_game import InteractiveGame

interactive_game = InteractiveGame(nbr_players=1, nbr_decks=8)
interactive_game.ifu()
interactive_game.print_state()

print()
print()
print()

interactive_game.play()

from black_jack.games.interactive_game import InteractiveGame

interactive_game = InteractiveGame(nbr_players=1, nbr_decks=8)
if len(interactive_game.black_jacks) < len(interactive_game.agents):
    interactive_game.ifu()
    interactive_game.print_state()
    print()

interactive_game.play()

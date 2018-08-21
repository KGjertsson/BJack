from ...games import agent_game, interactive_game


def play_game(agent_type, game_type, nbr_players, nbr_decks, starting_cash, possible_actions, verbose):
    if game_type == 'interactive':
        game = interactive_game.InteractiveGame(nbr_players, nbr_decks)
    else:
        game = agent_game.AgentGame(nbr_players=nbr_players,
                                    nbr_decks=nbr_decks,
                                    cash=starting_cash,
                                    agent_type=agent_type,
                                    actions=possible_actions,
                                    verbose=verbose)
    game.play()

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
    return game.play()


def play_while_cash_left(current_cash, **play_kwargs):
    money_over_time = list()
    while current_cash > 0:
        stats, bets = play_game(**play_kwargs)

        # TODO: make general, i.e. for more than 1 agent
        if stats[0] == 0:
            current_cash -= bets[0]
        elif stats[0] == 1:
            current_cash += bets[0]
        elif stats[0] == 3:
            current_cash += bets[0] * 1.5

        # print(stats, bets, current_cash)
        money_over_time.append(current_cash)
    return money_over_time

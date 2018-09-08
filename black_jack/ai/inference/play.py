from ...games import agent_game, interactive_game


def play_game(agent_type, game_type, nbr_players, nbr_decks, starting_cash, possible_actions, verbose, **game_kwargs):
    if game_type == 'interactive':
        game = interactive_game.InteractiveGame(nbr_players, nbr_decks)
    else:
        game = agent_game.AgentGame(nbr_players=nbr_players,
                                    nbr_decks=nbr_decks,
                                    cash=starting_cash,
                                    agent_type=agent_type,
                                    actions=possible_actions,
                                    verbose=verbose,
                                    **game_kwargs)
    return game.play()


def play_while_cash_left(current_cash, **play_kwargs):
    # TODO: make current_cash into a list with each agent cash so that multiple agents can play at the same time
    money_over_time = list()
    while current_cash > 0:
        stats, bets = play_game(**play_kwargs)

        for stat, bet in zip(stats, bets):
            if stat == 0:
                current_cash -= bet
            elif stat == 1:
                current_cash += bet
            elif stat == 3:
                current_cash += bet * 1.5

        # print(stats, bets, current_cash)
        money_over_time.append(current_cash)
    return money_over_time

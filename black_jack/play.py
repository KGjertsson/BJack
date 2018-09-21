from black_jack.games import agent_game


def play_while_cash_left(agent_configs, nbr_decks, verbose):
    game = agent_game.AgentGame(agent_configs, nbr_decks, verbose)
    continue_playing = True
    while continue_playing:
        stats, bets, ancestor_indices = game.play()

        for agent_id, (stat, bet, agent, ancestor_index) in enumerate(zip(stats, bets, game.agents, ancestor_indices)):
            current_agent = agent if ancestor_index is None else game.agents[ancestor_index]
            if current_agent.cash > 0:
                current_agent.cash = _manage_returned_cash(stat, bet, current_agent.cash)
                current_cash = max(current_agent.cash, 0)
            else:
                current_cash = 0
            money_id = agent_id if ancestor_index is None else ancestor_index
            game.agents[money_id].cash_progression.append(current_cash)

        game.reset_board()
        if sum([agent.cash_progression[-1] for agent in game.agents]) == 0:
            continue_playing = False

    return game.agents


def _manage_returned_cash(stat, bet, current_cash):
    if stat == 0:
        current_cash -= bet
    elif stat == 1:
        current_cash += bet
    elif stat == 3:
        current_cash += bet * 1.5
    elif stat == 4:
        current_cash += bet * 2
    elif stat == 5:
        current_cash -= bet * 2
    return current_cash

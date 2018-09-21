from ...games import agent_game


# class Money:
#     def __init__(self, name):
#         self.name = name  # str
#         self.cash = list()  # list


def manage_returned_cash(stat, bet, current_cash):
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


def play_while_cash_left(agent_configs, nbr_decks, verbose):
    # money_over_time = list()
    # for agent_config in agent_configs:
    #
    #     init_id = 0
    #     for money in money_over_time:
    #         if str(agent_config['agent_type']) in money.name:
    #             init_id += 1
    #
    #     money_over_time.append(Money(str(agent_config['agent_type']) + str(init_id)))

    game = agent_game.AgentGame(agent_configs, nbr_decks, verbose)
    continue_playing = True
    while continue_playing:
        stats, bets, ancestor_indices = game.play()

        for agent_id, (stat, bet, agent, ancestor_index) in enumerate(zip(stats, bets, game.agents, ancestor_indices)):
            current_agent = agent if ancestor_index is None else game.agents[ancestor_index]
            if current_agent.cash > 0:
                current_agent.cash = manage_returned_cash(stat, bet, current_agent.cash)
                current_cash = max(current_agent.cash, 0)
            else:
                current_cash = 0
            money_id = agent_id if ancestor_index is None else ancestor_index
            # money_over_time[money_id].cash.append(current_cash)
            game.agents[money_id].cash_progression.append(current_cash)

        game.reset_board()
        if sum([agent.cash_progression[-1] for agent in game.agents]) == 0:
            continue_playing = False

    return game.agents

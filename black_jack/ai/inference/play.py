from ...games import agent_game, interactive_game


class Money:
    def __init__(self, name):
        self.name = name  # str
        self.cash = list()  # list


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

        money_over_time.append(current_cash)
    return money_over_time


def play_while_cash_left_multiple_agents(agent_configs, nbr_decks, verbose):
    money_over_time = list()
    for agent_config in agent_configs:

        init_id = 0
        for money in money_over_time:
            if agent_config['agent_type'] in money.name:
                init_id += 1

        money_over_time.append(Money(agent_config['agent_type'] + str(init_id)))

    game = agent_game.MultipleAgentGame(agent_configs, nbr_decks, verbose)
    continue_playing = True
    while continue_playing:
        stats, bets = game.play()

        for agent_id, (stat, bet, agent) in enumerate(zip(stats, bets, game.agents)):
            if agent.cash > 0:
                if stat == 0:
                    agent.cash -= bet
                elif stat == 1:
                    agent.cash += bet
                elif stat == 3:
                    agent.cash += bet * 1.5
                current_cash = max(agent.cash, 0)
            else:
                current_cash = 0

            money_over_time[agent_id].cash.append(current_cash)

        if sum([money.cash[-1] for money in money_over_time]) == 0:
            continue_playing = False
        else:
            game.reset_board()

    return money_over_time

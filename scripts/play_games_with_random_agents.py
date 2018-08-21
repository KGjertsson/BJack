import numpy as np
import matplotlib.pyplot as plt

from black_jack.ai.inference import play

if __name__ == '__main__':
    agent_type = 'random'
    game_type = 'agent_game'
    nbr_players = 1
    nbr_decks = 6
    starting_cash = 1000
    current_cash = starting_cash
    possible_actions = [0, 1]
    verbose = 0

    money_over_time = list()
    while current_cash > 0:
        stats, bets \
            = play.play_game(agent_type, game_type, nbr_players, nbr_decks, starting_cash, possible_actions, verbose)

        if stats[0] == 0:
            current_cash -= bets[0]
        elif stats[0] == 1:
            current_cash += bets[0]

        # print(stats, bets, current_cash)
        money_over_time.append(current_cash)

    plt.show(plt.plot(np.stack(money_over_time)))

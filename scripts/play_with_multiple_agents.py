import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

from black_jack.agents.heuristic_agent import HeuristicAgent
from black_jack.agents.random_agent import RandomAgent
from black_jack.ai.inference import play

if __name__ == '__main__':
    number_iterations = 10
    verbose = 0
    plot_figures = True
    nbr_decks = 6
    starting_cash = 1000
    performance = list()

    for _ in tqdm(range(number_iterations)):
        heuristic_agent_config = {
            'agent_type': HeuristicAgent,
            'cash': starting_cash,
            'actions': [0, 1, 2, 3],
            'betting_strategy': 'fixed'
        }

        random_agent_config = {
            'agent_type': RandomAgent,
            'cash': starting_cash,
            'actions': [0, 1, 2, 3],
            'betting_strategy': 'fixed'
        }

        agent_configs = [heuristic_agent_config, random_agent_config]

        money_over_time = play.play_while_cash_left(
            agent_configs=agent_configs,
            nbr_decks=nbr_decks,
            verbose=verbose)

        performance.append(money_over_time)

    print('-')
    print('-')
    print('-')
    print(np.mean([len(hand[0].cash) for hand in performance]))

    if plot_figures:
        for money_over_time in performance:
            for money in money_over_time:
                plt.plot(money.cash, label=money.name)
        plt.legend(loc="upper right")
        plt.xlabel('iteration')
        plt.ylabel('US$')
        plt.show()

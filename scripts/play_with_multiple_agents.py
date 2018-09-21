import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import copy

from black_jack.agents.heuristic_agent import HeuristicAgent
from black_jack.agents.random_agent import RandomAgent
from black_jack.ai.inference import play

if __name__ == '__main__':
    number_iterations = 1
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

        agent_configs = [heuristic_agent_config, copy.copy(heuristic_agent_config)]

        agents = play.play_while_cash_left(
            agent_configs=agent_configs,
            nbr_decks=nbr_decks,
            verbose=verbose)

        performance.append([{'cash': agent.cash_progression, 'name': str(agent)} for agent in agents])

    print('-')
    print('-')
    print('-')
    print(np.mean([nbr_rounds for nbr_rounds in
                   [[len(agent['cash']) for agent in bj_round] for bj_round in performance]]))

    if plot_figures:
        for agents in performance:
            for money in agents:
                plt.plot(money['cash'], label=money['name'])
        plt.legend(loc="upper right")
        plt.xlabel('iteration')
        plt.ylabel('US$')
        plt.show()

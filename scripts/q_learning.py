from black_jack.ai.inference import play
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    number_iterations = 1
    verbose = 0
    plot_figures = True
    nbr_decks = 6
    starting_cash = 1000
    performance = list()

    for _ in tqdm(range(number_iterations)):
        agent_configs = [{
            'agent_type': 'q_learning',
            'alpha': 0.1,
            'epsilon': 0.1,
            'gamma': 0.1,
            'learning_rate': 0.1,
            'current_cash': starting_cash,
            'possible_actions': [0, 1, 2, 3],
            'betting_strategy': 'fixed'
        }]

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

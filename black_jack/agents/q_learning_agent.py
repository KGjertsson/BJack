import sys

import numpy as np

from black_jack.agents.abstract_agent import AbstractAgent


class QLearningState:
    def __init__(self, game_state):
        self.state = game_state
        self.actions = dict()

    def __eq__(self, other):
        same = True
        for my_dealer_card, other_dealer_card in zip(self.state['dealer'].hand, other.state['dealer'].hand):
            if my_dealer_card.value != other_dealer_card.value:
                same = False

        my_cards_value = sorted([card.value for card in self.state['player'].hand])
        other_cards_value = sorted([card.value for card in other.state['player'].hand])

        for my_card_value, other_card_value in zip(my_cards_value, other_cards_value):
            if my_card_value != other_card_value:
                same = False

        return same

    def __hash__(self):
        return hash(self.__str__()) % ((sys.maxsize + 1) * 2)

    def __str__(self):
        return '<dealer=' + str(self.state['dealer'].hand[0]) + ', player=' + ','.join(
            [str(card) for card in self.state['player'].hand]) + '>'


class QLearner(AbstractAgent):
    def __init__(self, alpha, epsilon, gamma, learning_rate, learning=True, **player_init_kwargs):
        super().__init__(**player_init_kwargs)
        self._Q = {}
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.learning_rate = learning_rate

        self._last_state = None
        self._last_action = None
        self._learning = learning

    def action(self, state):
        # TODO: fix or comment on discrepancy between q learning state and blackjack state
        state = QLearningState(state)

        if state in self._Q and np.random.uniform(0, 1) >= self.epsilon:
            action = max(self._Q[state], key=self._Q[state].get)
        else:
            action = np.random.choice(self.legal_actions)

        if state not in self._Q:
            self._Q[state] = {}
        self._Q[state][action] = 0

        self._last_state = state
        self._last_action = action

        return action

    def update(self, new_state, reward):
        print('we are updating state with {}'.format(new_state))
        new_state = QLearningState(new_state)

        if self._learning:
            try:
                old = self._Q[self._last_state][self._last_action]
            except KeyError:
                foo = 1

            if new_state in self._Q:
                new = self.gamma * \
                      self._Q[new_state][max(self._Q[new_state], key=self._Q[new_state].get)]
            else:
                new = 0

            self._Q[self._last_state][self._last_action] = \
                (1 - self.learning_rate) * old + self.learning_rate * (reward + new)

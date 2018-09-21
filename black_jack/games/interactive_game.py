from ..components.player import Player
from ..components.deck import Deck
from ..components.card import Card

ROYALTIES = [11, 12, 13]


class InteractiveGame:
    """
    Verbose:
        0: Don't print anything.
        1: Print human level information.
        2: Print debugging information.

    Actions:
        0: hit
        1: stay
        2: double
        3: split
    """

    def __init__(self, nbr_players, nbr_decks, verbose=1):
        self.nbr_players = nbr_players
        self.nbr_decks = nbr_decks
        self.deck = Deck(self.nbr_decks)
        self.deck.shuffle()
        self.dealer = Player([card for card in self.deck.draw(1)])
        self.agents = [Player([card for card in self.deck.draw(2)]) for _ in range(nbr_players)]
        self.verbose = verbose
        self.black_jacks = list()
        self.doubles = [False for _ in range(len(self.agents))]
        self.check_for_blackjack()

    def check_for_blackjack(self):
        for player_index, player in enumerate(self.agents):
            card_values = [card.value for card in player.hand]

            def check_for_royalty(values):
                for value in values:
                    if value in ROYALTIES:
                        return True
                return False

            if check_for_royalty(card_values) and 14 in card_values:
                self.black_jacks.append(player_index)
                if self.verbose:
                    print('Player {} got black jack and won'.format(player_index + 1))

    def reset_board(self):
        self.deck = Deck(self.nbr_decks)
        self.deck.shuffle()
        self.dealer = Player([card for card in self.deck.draw(1)])
        self.reset_agents()

        self.black_jacks = list()
        self.doubles = [False for _ in range(len(self.agents))]
        self.check_for_blackjack()

    def reset_agents(self):
        nbr_children = 0
        for agent in self.agents:
            if agent.ancestor_index is not None:
                nbr_children += 1
        self.agents = [Player([card for card in self.deck.draw(2)]) for _ in range(self.nbr_players - nbr_children)]

    def print_state(self):
        print('dealer has: {}, value is: {}'.format([str(card) for card in self.dealer.hand],
                                                    self.dealer.value_of_hand()))
        for player_index, player in enumerate(self.agents):
            print('player {} has: {}, value is: {}'.format(player_index + 1, [str(card) for card in player.hand],
                                                           player.value_of_hand()))

    def init_new_players_after_split(self, player, player_index):
        new_player = Player([player.hand[1]])
        new_player.hand.append([card for card in self.deck.draw(1)][0])
        new_player.ancestor_index = player_index if player.ancestor_index is not None else player.ancestor_index

        self.agents.append(new_player)
        player.hand = [player.hand[0]]
        player.hand.append([card for card in self.deck.draw(1)][0])

        self.doubles.append(False)

    @staticmethod
    def ifu():
        print('############################')
        print('### Instructions For Use ###')
        print('Available commands:')
        print('hit')
        print('stay')
        print('double')
        print('############################')
        print()

    def get_action(self, player):
        raw_action = input(">>")
        if raw_action == 'hit':
            action = 0
        elif raw_action == 'stay':
            action = 1
        elif raw_action == 'double':
            if 7 <= player.value_of_hand() <= 11:
                action = 2
            else:
                if self.verbose == 1:
                    print('invalid command \'double\' for value of hand: {}'.format(player.value_of_hand()))
                return self.get_action(player)
        elif raw_action == 'split':
            if len(player.hand) != 2:
                if self.verbose == 1:
                    print('invalid command \'split\' when number of cards != 2')
                return self.get_action(player)
            elif player.hand[0].value != player.hand[1].value:
                if self.verbose == 1:
                    print('invalid command \'split\' when number value of cards are not equal')
                return self.get_action(player)
            action = 3
        else:
            if self.verbose == 1:
                print('Invalid command, see IFU for list of valid inputs: \n')
            self.ifu()
            return self.get_action(player)
        return action

    def perform_round(self, player, player_index):
        action = self.get_action(player)
        if action == 0:
            # hit
            player.hand += [card for card in self.deck.draw(1)]
            if self.verbose == 1:
                self.print_state()

            if player.value_of_hand() > 21:
                player.hand = [Card('none', 2)]
                player.hand[0].set_value = -1
                if self.verbose == 1:
                    print('Player {} is fat'.format(player_index + 1))
                return False

            return self.perform_round(player, player_index)
        elif action == 1:
            # stay
            return True
        elif action == 2:
            # double
            player.hand += [card for card in self.deck.draw(1)]
            if self.verbose == 1:
                self.print_state()

            if player.value_of_hand() > 21:
                player.hand = [Card('none', 2)]
                player.hand[0].set_value = -1
                if self.verbose == 1:
                    print('Player {} is fat'.format(player_index + 1))
                return False
            self.doubles[player_index] = True
            return True

        elif action == 3:
            self.init_new_players_after_split(player, player_index)
            if self.verbose == 1:
                self.print_state()
            return self.perform_round(player, player_index)

    def dealer_draws(self):
        while self.dealer.value_of_hand() < 17:
            self.dealer.hand += [card for card in self.deck.draw(1)]
            if self.verbose == 1:
                self.print_state()
                print('-' * 10)
        if self.dealer.value_of_hand() > 21:
            self.dealer.hand = [Card('hearts', 2)]
            self.dealer.hand[0].set_value = -1

    def find_winner(self, hand_value, dealer_hand_value, player_index):
        """
        victory == 0: player lost
        victory == 1: player won
        victory == 2: player played even with the dealer
        victory == 3: player got black jack
        victory == 4: player won with doubled money
        victory == 5: player lost with doubled money
        """
        if player_index in self.black_jacks:
            victory = 3
            if self.verbose == 1:
                print('Player {} got black jack and won'.format(player_index))
        else:
            if self.doubles[player_index]:
                victory = 5
            else:
                victory = 0
            if hand_value != -1:
                if dealer_hand_value != -1:
                    if hand_value > dealer_hand_value:
                        if self.verbose == 1:
                            print('Player {} won'.format(player_index + 1))
                        if self.doubles[player_index]:
                            victory = 4
                        else:
                            victory = 1
                    elif hand_value == dealer_hand_value:
                        if self.verbose == 1:
                            print('Player {} played even with the dealer.'.format(player_index + 1))
                        victory = 2
                    else:
                        if self.verbose == 1:
                            print('Player {} lost'.format(player_index + 1))
                else:
                    if self.verbose == 1:
                        print('Player {} won'.format(player_index + 1))
                    if self.doubles[player_index]:
                        victory = 4
                    else:
                        victory = 1
            else:
                if self.verbose == 1:
                    print('Player {} lost'.format(player_index + 1))
        return victory

    def play(self):
        if len(self.black_jacks) < len(self.agents):
            for player_index, player in enumerate(self.agents):
                if player_index in self.black_jacks or self.doubles[player_index]:
                    continue
                if self.verbose == 1:
                    print('player {}, what do you want to do?'.format(player_index + 1))
                self.perform_round(player, player_index)
            self.dealer_draws()

        dealer_hand_value = self.dealer.value_of_hand()
        winners = list()
        for player_index, player in enumerate(self.agents):
            hand_value = player.value_of_hand()
            winners.append(self.find_winner(hand_value, dealer_hand_value, player_index))
        return winners

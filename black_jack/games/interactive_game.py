from ..components.player import Player
from ..components.deck import Deck
from ..components.card import Card


# TODO:
#   1. split
#   2. black jack

class InteractiveGame:
    def __init__(self, nbr_players, nbr_decks):
        self.deck = Deck(nbr_decks)
        self.deck.shuffle()
        self.dealer = Player([card for card in self.deck.draw(1)])
        self.players = [Player([card for card in self.deck.draw(2)]) for _ in range(nbr_players)]

    def print_state(self):
        print('dealer has: {}, value is: {}'.format([str(card) for card in self.dealer.hand],
                                                    self.dealer.value_of_hand()))
        for player_index, player in enumerate(self.players):
            print('player {} has: {}, value is: {}'.format(player_index + 1, [str(card) for card in player.hand],
                                                           player.value_of_hand()))

    @staticmethod
    def ifu():
        print('### Instructions For Use ###')
        print('0: add card')
        print('1: stay')
        print('############################')
        print()

    def get_action(self):
        raw_action = input(">>")
        try:
            action = int(raw_action)
        except ValueError:
            print('Invalid command, see IFU for list of valid inputs: \n')
            self.ifu()
            return self.get_action()
        return action

    def perform_round(self, player, player_index):
        action = self.get_action()
        if action == 0:
            player.hand += [card for card in self.deck.draw(1)]
            self.print_state()

            if player.value_of_hand() > 21:
                player.hand = [Card('none', 2)]
                player.hand[0].set_value = -1
                print('Player {} is fat'.format(player_index + 1))
                return False

            return self.perform_round(player, player_index)
        elif action == 1:
            return True

    def dealer_draws(self):
        while self.dealer.value_of_hand() < 17:
            self.dealer.hand += [card for card in self.deck.draw(1)]
            self.print_state()
            print('-' * 10)
        if self.dealer.value_of_hand() > 21:
            self.dealer.hand = [Card('hearts', 2)]
            self.dealer.hand[0].set_value = -1

    @staticmethod
    def find_winner(hand_value, dealer_hand_value, player_index):
        if hand_value != -1:
            if dealer_hand_value != -1:
                if hand_value > dealer_hand_value:
                    print('Player {} won'.format(player_index + 1))
                elif hand_value == dealer_hand_value:
                    print('Player {} played even with the dealer.'.format(player_index + 1))
                else:
                    print('Player {} lost'.format(player_index + 1))
            else:
                print('Player {} won'.format(player_index + 1))
        else:
            print('Player {} lost'.format(player_index + 1))

    def play(self):
        for player_index, player in enumerate(self.players):
            print('player {}, what do you want to do?'.format(player_index + 1))
            self.perform_round(player, player_index)
        self.dealer_draws()

        dealer_hand_value = self.dealer.value_of_hand()
        for player_index, player in enumerate(self.players):
            hand_value = player.value_of_hand()
            self.find_winner(hand_value, dealer_hand_value, player_index)

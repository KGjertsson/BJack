class Player:
    def __init__(self, cards):
        self.hand = cards

    @staticmethod
    def _raw_value(cards):
        return sum([card.calculate_value() for card in cards])

    def value_of_hand(self):
        def convert_aces(hand, index):
            value = Player._raw_value(self.hand)
            if value > 21:
                if hand[index].calculate_value() == 11:
                    hand[index].set_value = 1
                if index < len(hand) - 1:
                    return convert_aces(hand, index + 1)
                else:
                    return hand
            else:
                return hand

        return self._raw_value(convert_aces([card for card in self.hand], 0))

from ..error_handling import decorators


class Card:
    """
    Representation of a playing card. A card has a value and a suite. The values range between 2 and 14, where 2 - 10
    are self explanatory and the rest follow the mapping:
        11: jack
        12: queen
        13: king
        14: ace

    The value of a card in the game of blackjack differs from their value identifiers. 2 - 10 always retain the value
    indicated by their card number, while jack, queen and king all have the same value of 10. Aces are worth 11
    (special rules apply for aces and their final value is determined dynamically in the game).

    The suites are of course:
        hearts
        clubs
        diamonds
        spades
    """

    def __init__(self, suite, value):
        # TODO: make sure we don't call the decorator explicitly, as it is now it sort of defeats the purpose of having
        # TODO: a decorator in the first place
        decorators.card_validator(suite, value)
        self.suite = suite
        self.value = value
        self.set_value = None

    def __str__(self):
        if self.suite == 'none':
            str_rep = ''
        else:
            if self.value == 11:
                value_string = 'jack'
            elif self.value == 12:
                value_string = 'queen'
            elif self.value == 13:
                value_string = 'king'
            elif self.value == 14:
                value_string = 'ace'
            else:
                value_string = str(self.value)
            str_rep = value_string + ' of ' + self.suite
        return str_rep

    def calculate_value(self):
        if self.set_value is None:
            if 11 <= self.value <= 13:
                calculated_value = 10
            elif self.value == 14:
                calculated_value = 11
            else:
                calculated_value = self.value
        else:
            calculated_value = self.set_value
        return calculated_value

from ..error_handling import decorators


class Card:
    def __init__(self, suite, value):
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

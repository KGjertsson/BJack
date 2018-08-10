from .exceptions import InvalidSuiteException, InvalidValueException

SUITES = ['hearts', 'clubs', 'spades', 'diamonds', 'none']


def card_validator(suite, value):
    if suite not in SUITES:
        raise InvalidSuiteException('Expected suite to be one of {}, found {}'.format(SUITES, suite))

    if value < 1 or value > 14:
        raise InvalidValueException('Expected value to be in range [1, 14], found {}'.format(value))

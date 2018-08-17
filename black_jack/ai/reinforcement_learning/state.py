class State:
    def __init__(self, current_points, dealer_value, is_soft, split_possibility):
        self.current_points = current_points
        self.dealer_value = dealer_value
        self.is_soft = is_soft
        self.split_possibility = split_possibility

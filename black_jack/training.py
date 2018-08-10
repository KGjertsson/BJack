from .ai.neural_network import FeedForwardNet


class AnnTrainer:
    def __init__(self, training_config_kwargs, compilation_kwargs):
        self.training_config_kwargs = training_config_kwargs
        self.compilation_kwargs = compilation_kwargs

    def configure_trainig(self):
        model = FeedForwardNet(**self.training_config_kwargs).make_model()
        model.summary()
        model.compile(**self.compilation_kwargs)

    def train(self):
        pass

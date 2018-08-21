from black_jack.training import AnnTrainer
from black_jack.ai import loss_functions

training_config_kwargs = {
    'nbr_input_features': 10,
    'nbr_layers': 4,
    'nbr_neurons': 100,
    'activation_function': 'relu',
    'output_activation_function': 'softmax'
}

compilation_kwargs = {
    'optimizer': 'SGD',
    'loss': loss_functions.bj_loss
}

trainer = AnnTrainer(training_config_kwargs, compilation_kwargs)
trainer.configure_trainig()

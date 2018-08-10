from keras.layers import Input, Dense, Activation
from keras.models import Model


class FeedForwardNet:
    def __init__(self, nbr_input_features, nbr_layers, nbr_neurons, activation_function, output_activation_function):
        self.nbr_input_features = nbr_input_features
        self.nbr_layers = nbr_layers
        self.nbr_neurons = nbr_neurons
        self.activation_function = activation_function
        self.output_activation_function = output_activation_function

    def make_model(self):
        input_layer = Input(shape=(self.nbr_input_features,))
        x = None
        for layer_index in range(self.nbr_layers):
            prev_layer = x if x is not None else input_layer
            
            x = Dense(self.nbr_neurons)(prev_layer)
            if layer_index != self.nbr_layers - 1:
                x = Activation(self.activation_function)(x)
            else:
                x = Activation(self.output_activation_function)(x)

        model = Model(inputs=[input_layer], outputs=[x])
        return model


if __name__ == '__main__':
    ann = FeedForwardNet(10, 4, 100, 'relu', 'softmax')
    ann.make_model().summary()

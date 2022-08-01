class Layer:

    def __init__(self) -> None:
        self.next_layer = None
        self.name = "Layer"

    def __call__(self, layer, *args, **kwargs) -> None:
        self.next_layer = layer
        return self.next_layer


class Input(Layer):

    def __init__(self, inputs: int) -> None:
        super().__init__()
        self.name = "Input"
        self.inputs = inputs


class Dense(Layer):

    def __init__(self, inputs: int, outputs: int, activation: str) -> None:
        super().__init__()
        self.name = "Dense"
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:

    def __init__(self, network: Layer) -> None:
        self.network = network

    def __iter__(self):
        self.__layer = self.network
        return self

    def __next__(self):
        if not self.__layer:
            raise StopIteration
        else:
            res = self.__layer
            self.__layer = self.__layer.next_layer
            return res


network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))
for x in NetworkIterator(network):
    print(x.name)

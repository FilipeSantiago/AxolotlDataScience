from sklearn.neural_network import MLPClassifier


class NeuralNetwork:

    def __init__(self):
        self.learning_algorithm = None

    def init_learning_algorithm(self):
        self.learning_algorithm = MLPClassifier(alpha=1)
        return self.learning_algorithm

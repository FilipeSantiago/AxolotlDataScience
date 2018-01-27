from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF


class GaussianProcess:

    def __init__(self):
        self.learning_algorithm = None

    def init_learning_algorithm(self):
        self.learning_algorithm = GaussianProcessClassifier(1.0 * RBF(1.0))
        return self

    def get_learning_algorithm(self):
        return self.learning_algorithm

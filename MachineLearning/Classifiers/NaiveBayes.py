from sklearn.naive_bayes import GaussianNB


class SupportVectorMachineClassifier:

    def __init__(self):
        self.learning_algorithm = None

    def init_learning_algorithm(self):
        self.learning_algorithm = GaussianNB()
        return self

    def get_learning_algorithm(self):
        return self.learning_algorithm

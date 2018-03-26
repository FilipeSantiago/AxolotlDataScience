from sklearn import svm


class SupportVectorMachineClassifier:

    def __init__(self):
        self.learning_algorithm = None

    def init_learning_algorithm(self):
        self.learning_algorithm = svm.SVC()
        return self.learning_algorithm


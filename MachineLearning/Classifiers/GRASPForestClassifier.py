from MachineLearning.Classifiers.GRASPForest.GRASPForest import GRASPForest


class GRASPForestClassifier:

    def __init__(self):
        self.learning_algorithm = None
        self.number_of_trees = 20
        self.GRASP_randomish = 3

    def set_number_of_trees(self, number_of_trees):
        self.number_of_trees = number_of_trees
        return self

    def set_number_of_GRASP_randomish(self, GRASP_randomish):
        self.GRASP_randomish = GRASP_randomish
        return self

    def init_learning_algorithm(self):
        self.learning_algorithm = GRASPForest(self.number_of_trees, self.GRASP_randomish)
        return self

    def get_learning_algorithm(self):
        return self.learning_algorithm

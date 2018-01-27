from sklearn.neighbors import KNeighborsClassifier as knn


class KNeighborsClassifier:

    def __init__(self):
        self.learning_algorithm = None

    def init_learning_algorithm(self):
        self.learning_algorithm = knn(n_neighbors=3, algorithm='ball_tree')
        return self

    def get_learning_algorithm(self):
        return self.learning_algorithm

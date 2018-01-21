from sklearn.model_selection import cross_val_score


class NFoldCrossValidation:

    def __init__(self, learning_algorithm, attributes, classes):
        self.learning_algorithm = learning_algorithm
        self.attributes = attributes
        self.classes = classes

    def ten_fold_cross_validation(self, cv=10):

        accuracy_vector = cross_val_score(self.learning_algorithm, self.attributes, self.classes, cv=cv)
        return sum(accuracy_vector) / float(len(accuracy_vector))

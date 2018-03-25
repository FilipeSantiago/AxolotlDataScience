from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np

class NFoldCrossValidation:

    def __init__(self, learning_algorithm, attributes, classes):
        self.learning_algorithm = learning_algorithm
        self.attributes = attributes
        self.classes = classes

    def ten_fold_cross_validation(self, cv=10):

        accuracy_vector = cross_val_score(self.learning_algorithm, self.attributes, self.classes, cv=cv)
        return sum(accuracy_vector) / float(len(accuracy_vector))

    def n_fold_cross_validation(self, cv=10):

        if isinstance(self.attributes, pd.DataFrame):
            self.attributes = self.attributes.as_matrix()

        if isinstance(self.classes, pd.DataFrame):
            self.classes = self.classes.as_matrix()

        data = np.concatenate((self.attributes, np.asarray([self.classes]).T), axis=1).tolist()

        split_list = lambda lst, sz: [lst[j:j + sz] for j in range(0, len(lst), sz)]

        part_data = split_list(data, int(len(data) / cv))
        total_acc = 0
        for i in range(0, cv):
            print("Iniciando Fold ", i, " de ", cv)
            train_set = []
            validator_set = part_data[i]
            for partial_data in part_data:
                if partial_data != validator_set:
                    train_set += partial_data

            self.learning_algorithm.get_learning_algorithm().builder(train_set)
            acc = self.learning_algorithm.get_learning_algorithm().avaliator(validator_set)
            total_acc += acc
            print(acc, '%')
        return total_acc / cv

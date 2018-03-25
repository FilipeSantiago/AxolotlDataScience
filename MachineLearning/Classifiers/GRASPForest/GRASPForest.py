from MachineLearning.Classifiers.GRASPForest.GRASPTreeBuilder import GRASPTreeBuilder
from MachineLearning.Classifiers.GRASPForest.ClassificationMethod import ClassificationMethod
import operator
import numpy as np

class GRASPForest(ClassificationMethod):

    GRASPForest = []

    def __init__(self, num_of_trees=None, randomish=None, thresholder=0, prune_thresholder=0.2):
        self.num_of_trees = num_of_trees  # Value of decision
        self.randomish = randomish  # list of data for this node (debug)
        self.thresholder = thresholder
        self.prune_thresholder = prune_thresholder

    def builder(self, dataset):
        self.build_GRASP_Forest(dataset, self.num_of_trees, self.randomish)

    def avaliator(self, dataset):

        dataset = np.asarray(dataset)
        predictions = self.predict(dataset)
        real_classes = dataset[:, len(dataset[0]) - 1]

        acc = 0

        for i in range(0, len(real_classes)):
            if predictions[i] == real_classes[i]:
                acc += 1

        return acc/len(real_classes)

    def build_GRASP_Forest(self, dataset, number_of_trees, grasp_variation):

        builder = GRASPTreeBuilder()

        for i in range(0, number_of_trees):
            print("constrindo árvore ", i)
            grasp_tree = builder.build_tree(dataset, grasp_variation, self.thresholder)
            builder.prune(grasp_tree, self.prune_thresholder, notify=False)
            self.GRASPForest.append(grasp_tree)

    def predict(self, dataset):

        predictions = []
        for row in dataset:
            prediction = self.classify_row(row)
            predictions.append(prediction)

        return predictions

    def classify_row(self, row):
        election = []

        for tree in self.GRASPForest:
            candidate = self.data_classificator(row, tree)
            election.append(candidate)
        winner = max(set(election), key=election.count)

        return winner

    def data_classificator(self, data, root):

        if root.right is None and root.left is None:
            return max(root.results.items(), key=operator.itemgetter(1))[0]
        else:
            node = root.right
            if isinstance(data[root.col], int) or isinstance(data[root.col], float):
                if data[root.col] < root.value:
                    node = root.left
            else:
                if data[root.col] != root.value:
                    node = root.left
            return self.data_classificator(data, node)
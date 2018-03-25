from MachineLearning.Classifiers.GRASPForest.TreeBuilder import TreeBuilder
from MachineLearning.Classifiers.GRASPForest.DecisionNode import DecisionNode
from MachineLearning.Classifiers.GRASPForest.BestEntropy import BestEntropy
import bisect
import random


class GRASPTreeBuilder(TreeBuilder):

    def build_tree(self, rows, k, thresholder):

        if len(rows) == 0:
            return DecisionNode()
        current_score = self.entropy(rows)

        best_gain = 0.0
        best_criteria = None
        best_sets = None
        ordered_gain = []

        column_count = len(rows[0]) - 1
        for col in range(0, column_count):
            global column_values
            column_values = {}
            for row in rows:
                column_values[row[col]] = 1
            for value in column_values.keys():
                (set1, set2) = self.divide_set(rows, col, value)
                p = float(len(set1)) / len(rows)
                gain = current_score - p * self.entropy(set1) - (1 - p) * self.entropy(set2)
                criteria = (col, value)
                sets = (set1, set2)
                if len(set1) > 0 and len(set2) > 0:
                    to_add = BestEntropy(gain, criteria, sets)
                    bisect.insort(ordered_gain, to_add)

        # Create the sub branches
        if len(ordered_gain) > 0:
            best_gain = ordered_gain[:k]
            use_node = random.choice(best_gain)
            if use_node.best_gain > thresholder:
                true_branch = self.build_tree(use_node.best_sets[0], k, thresholder)
                false_branch = self.build_tree(use_node.best_sets[1], k, thresholder)
                return DecisionNode(col=use_node.best_criteria[0], value=use_node.best_criteria[1],
                                    right=true_branch, left=false_branch)
            else:
                return DecisionNode(results=self.unique_counts(rows))
        else:
            return DecisionNode(results=self.unique_counts(rows))

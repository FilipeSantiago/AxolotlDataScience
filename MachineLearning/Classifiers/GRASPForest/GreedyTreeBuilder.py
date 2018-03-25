from MachineLearning.Classifiers.GRASPForest.TreeBuilder import TreeBuilder
from MachineLearning.Classifiers.GRASPForest.DecisionNode import DecisionNode


class GreedyTreeBuilder(TreeBuilder):

    def build_tree(self, rows, k=0, thresholder=0):

        if len(rows) == 0:
            return DecisionNode()
        current_score = self.entropy(rows)

        best_gain = 0.0
        best_criteria = None
        best_sets = None

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
                if gain > best_gain and len(set1) > 0 and len(set2) > 0:
                    best_gain = gain
                    best_criteria = (col, value)
                    best_sets = (set1, set2)

        # Create the sub branches
        if best_gain > thresholder:
            true_branch = self.build_tree(best_sets[0], thresholder=thresholder)
            false_branch = self.build_tree(best_sets[1], thresholder=thresholder)
            return DecisionNode(col=best_criteria[0], value=best_criteria[1],
                                right=true_branch, left=false_branch)
        else:
            return DecisionNode(results=self.unique_counts(rows))
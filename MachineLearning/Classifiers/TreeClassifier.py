import subprocess
from sklearn import tree
from sklearn.tree import export_graphviz


class TreeClassifier:

    def __init__(self):
        self.learning_algorithm = None

    def init_learning_algorithm(self):
        self.learning_algorithm = tree.DecisionTreeClassifier()
        return self

    def visualize_tree(self, tree, feature_names):

        with open("dt.dot", 'w') as f:
            export_graphviz(tree, out_file=f, feature_names=feature_names)

        command = ["dot", "-Tpng", "dt.dot", "-o", "dt.png"]
        try:
            subprocess.check_call(command)
        except:
            exit("Could not run dot, ie graphviz, to produce visualization")

    def get_learning_algorithm(self):
        return self.learning_algorithm

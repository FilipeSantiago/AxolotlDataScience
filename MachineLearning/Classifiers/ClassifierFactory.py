from MachineLearning.Classifiers import ClassifierTypes
from MachineLearning.Classifiers import TreeClassifier as treeClassifier
from MachineLearning.Classifiers import SupportVectorMachineClassifier as svm
from MachineLearning.Classifiers import KNeighborsClassifier as knn
from MachineLearning.Classifiers import NaiveBayes as nb
from MachineLearning.Classifiers import NeuralNetwork
from MachineLearning.Classifiers import GaussianProcess
from MachineLearning.Classifiers import GRASPForestClassifier

class ClassifierFactory:

    def choose_classifier(self, classifier_type):

        classifier_types = ClassifierTypes.ClassifierTypes
        classifier = None

        if classifier_type == classifier_types.Tree:
            classifier = treeClassifier.TreeClassifier()

        elif classifier_type == classifier_types.SVM:
            classifier = svm.SupportVectorMachineClassifier()

        elif classifier_type == classifier_types.KNN:
            classifier = knn.KNeighborsClassifier()

        elif classifier_type == classifier_types.NaiveBayes:
            classifier = nb.SupportVectorMachineClassifier()

        elif classifier_type == classifier_types.NeuralNetwork:
            classifier = NeuralNetwork.NeuralNetwork()

        elif classifier_type == classifier_types.GaussianProcess:
            classifier = GaussianProcess.GaussianProcess()

        elif classifier_type == classifier_types.GRASPForest:
            classifier = GRASPForestClassifier.GRASPForestClassifier()

        return classifier

    def init_classifier(self, classifier):
        return classifier.init_learning_algorithm() \
                         .get_learning_algorithm()

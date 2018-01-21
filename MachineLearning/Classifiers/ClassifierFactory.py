from MachineLearning.Classifiers import ClassifierTypes
from MachineLearning.Classifiers import TreeClassifier as treeClassifier
from MachineLearning.Classifiers import SupportVectorMachineClassifier as svm


class ClassifierFactory:

    def choose_classifier(self, classifier_type):

        classifier_types = ClassifierTypes.ClassifierTypes

        if classifier_type == classifier_types.Tree:
            tree = treeClassifier.TreeClassifier()
            return self.init_classifier(tree)

        elif classifier_type == classifier_types.SVM:
            svm_classifier = svm.SupportVectorMachineClassifier()
            return self.init_classifier(svm_classifier)

        return None

    def init_classifier(self, classifier):
        return classifier.init_learning_algorithm() \
                         .get_learning_algorithm()

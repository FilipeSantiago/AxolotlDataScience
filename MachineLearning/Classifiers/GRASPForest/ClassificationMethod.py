from abc import abstractmethod


class ClassificationMethod:

    @abstractmethod
    def builder(self, dataset):
        pass

    @abstractmethod
    def avaliator(self, dataset):
        pass
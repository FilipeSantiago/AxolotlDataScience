class BestEntropy:
    def __init__(self, best_gain=-1, best_criteria=None, best_sets=None):
        self.best_gain = best_gain
        self.best_criteria = best_criteria
        self.best_sets = best_sets

    def __lt__(self, other):
        return self.best_gain > other.best_gain
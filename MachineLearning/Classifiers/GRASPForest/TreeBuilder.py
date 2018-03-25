from abc import abstractmethod

__author__ = 'Filipe Santiago'


class TreeBuilder:

    def divide_set(self, rows, column, value):

        split_function = None
        if isinstance(value, int) or isinstance(value, float):  # check if the value is a number i.e int or float
            split_function = lambda row: row[column] >= value
        else:
            split_function = lambda row: row[column] == value
        set1 = [row for row in rows if split_function(row)]
        set2 = [row for row in rows if not split_function(row)]
        return set1, set2

    #Conta quantas linhas pertencem a cada classe
    def unique_counts(self, rows):
        results = {}
        for row in rows:
            # The result is the last column
            r = row[len(row) - 1]
            if r not in results:
                results[r] = 0
            results[r] += 1
        return results

    def entropy(self, rows):
        from math import log
        log2 = lambda x: log(x) / log(2)
        results = self.unique_counts(rows)
        # Now calculate the entropy
        ent = 0.0
        for r in results.keys():
            p = float(results[r]) / len(rows)
            ent = ent - p * log2(p)
        return ent

    def prune(self, tree, minGain, evaluationFunction=entropy, notify=False):
        evaluationFunction = self.entropy
        """Prunes the obtained tree according to the minimal gain (entropy or Gini). """
        # recursive call for each branch

        if tree.right is None and tree.left is None:
            return
        if tree.right.results is None:
            self.prune(tree.right, minGain, evaluationFunction, notify)
        if tree.left.results is None:
            self.prune(tree.left, minGain, evaluationFunction, notify)

        # merge leaves (potentionally)
        if tree.right.results is not None and tree.left.results is not None:
            tb, fb = [], []

            for v, c in tree.right.results.items():
                tb += [[v]] * c
            for v, c in tree.left.results.items():
                fb += [[v]] * c

            p = float(len(tb)) / len(tb + fb)

            union = tb + fb
            union_entropy = evaluationFunction(union)
            tb_entropy = p * evaluationFunction(tb)
            fb_entropy = (1 - p) * evaluationFunction(fb)
            delta = union_entropy - (tb_entropy + fb_entropy)
            if delta < minGain:
                if notify:
                    print('A branch was pruned: gain = %f' % delta)
                tree.right, tree.left = None, None
                tree.results = self.unique_counts(tb + fb)

    @abstractmethod
    def build_tree(self, data, k, thresholder):
        pass
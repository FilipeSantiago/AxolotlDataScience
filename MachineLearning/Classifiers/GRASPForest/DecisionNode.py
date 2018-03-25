class DecisionNode:

    def __init__(self, col=-1, value=None, results=None, right=None, left=None):
        self.col = col          # Column used to partition
        self.value = value      # Value of decision
        self.results = results  # list of data for this node (debug)
        self.right = right      # true results
        self.left = left        # false results
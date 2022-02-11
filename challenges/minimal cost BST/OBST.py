import sys
class Tree(object):
    
    def __init__(self, root, left=None, right=None):
        assert root and type(root) == Node
        if left: assert type(left) == Tree and left.root < root
        if right: assert type(right) == Tree and root < right.root

        self.left = left
        self.root = root
        self.right = right
        
    def is_leaf(self):
        return not(self.left or self.right)
        
    
    def __str__(self):
        pass
    
    def __eq__(self, other):
        pass
    
    def __ne__(self, other):
        pass

class Node(object):
    
    def __init__(self, value, weight=1):
        self.value = value
        self.weight = weight
    
    def __str__(self):
        return '%s:%d' % (self.value, self.weight)   
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __eq__(self, other):
        return self.value == other.value 

    def __ne__(self, other):
        return self.value != other.value 


def cost(tree, depth=1):
    '''
    Returns the cost of a tree which root is depth deep.
    '''
    cost_ = tree.root.weight * depth
    l_r = [tree.left, tree.right]
    for n in l_r:
        if isinstance(n, Tree):
            cost_ += cost(n, depth + 1)
        elif isinstance(n, Node):
            cost_ += n.weight * (depth + 1)
    return cost_


def make_min_tree(nodes):
    n = len(nodes)
    tree_struct = [[0 for i in range(n)] for j in range(n)]
    costs = [[0 for i in range(n)] for j in range(n)]
    sums = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
            sums[i][i] = nodes[i].weight

    # precomputed sums
    for i in range(n):
        for j in range(i+1, n):
            sums[i][j] += sums[i][j-1] + sums[j][j]

    for L in range(n):
        for i in range(n - L):
            j = i + L
            costs[i][j] = 2 ** 100
            for r in range(i, j+1):
                c = 0
                if r > i:
                    c += costs[i][r-1]
                if r < j:
                    c += costs[r+1][j]
                c += sums[i][j]
                if costs[i][j] > c:
                    costs[i][j] = c
                    tree_struct[i][j] = r
                    if r < j:
                        tree_struct[i][j] = Tree(nodes[r], tree_struct[i][r - 1], tree_struct[r + 1][j])
                    else:
                        tree_struct[i][j] = Tree(nodes[r], tree_struct[i][r - 1], None)
    return tree_struct[0][n - 1]

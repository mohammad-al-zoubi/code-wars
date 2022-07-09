def tree_by_levels(node):
    if not node:
        return []
    vals = [node.value]
    branches = [node.left, node.right]
    nums = False
    while not nums:
        lim = len(branches)
        k = []
        for n in branches:
            if n:
                if isinstance(n, Node):
                    vals.append(n.value)
                    k.append(n.left)
                    k.append(n.right)
                else:
                    vals.append(n)
        branches = k
        branches = list(filter(None, branches))
        nums = all(isinstance(i, int) for i in branches)
    return vals

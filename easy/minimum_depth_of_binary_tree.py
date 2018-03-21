from TreeNode import TreeNode


def minDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    depth = 1
    stack = [root]
    while len(stack) > 0:
        tmp = []
        for leaf in stack:
            if leaf.left is None and leaf.right is None:
                return depth
            else:
                if leaf.left:
                    tmp.append(leaf.left)
                if leaf.right:
                    tmp.append(leaf.right)
        stack = tmp
        depth += 1
    return depth
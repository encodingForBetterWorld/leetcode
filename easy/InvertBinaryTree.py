# Invert a binary tree.
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
# to
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return
    stock = [root]
    while stock:
        tmp = []
        for node in stock:
           t_node = node.left
           node.left = node.right
           node.right = t_node
           if node.left:
               tmp.append(node.left)
           if node.right:
               tmp.append(node.right)
        stock = tmp
    return root
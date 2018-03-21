# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
from leetcode.common.TreeNode import TreeNode

def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    max_path = 1
    ret = 1
    stack = []
    while True:
        left = root.left
        right = root.right
        if left is None and right is None:
            if len(stack) == 0:
                break
            root = stack.pop()
            max_path = max(max_path, ret)
            ret -= 1
        elif left:
            stack.append(root)
            root.left = None
            root = left
            ret += 1
        elif right:
            stack.append(root)
            root.right = None
            root = right
            ret += 1
    return max_path

leef = TreeNode(2)
leef.left = TreeNode(4)
leef.right = TreeNode(5)
leef.right.right = TreeNode(5)
leef.right.right.left = TreeNode(5)

root = TreeNode(1)
root.left = leef
root.right = TreeNode(3)
print maxDepth(root)
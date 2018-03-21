# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
# (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
from leetcode.common.TreeNode import TreeNode

def levelOrderBottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root is None:
        return []
    path = 0
    stack = []
    level_dict = {0:[root.val]}
    while True:
        left = root.left
        right = root.right
        if left is None and right is None:
            if len(stack) == 0:
                break
            root = stack.pop()
            path -= 1
        else:
            if left:
                stack.append(root)
                root.left = None
                root = left
                path += 1
            else:
                stack.append(root)
                root.right = None
                root = right
                path += 1
            level = level_dict.get(path)
            if level is None:
                level = [root.val]
                level_dict[path] = level
            else:
                level.append(root.val)
    ret = []
    idx = len(level_dict)
    while idx > 0:
        idx -= 1
        ret.append(level_dict.get(idx))
    return ret

leef = TreeNode(2)
# leef.left = TreeNode(4)
# leef.right = TreeNode(5)
# leef.right.right = TreeNode(5)
# leef.right.right.left = TreeNode(5)

root = TreeNode(1)
root.left = leef
root.right = TreeNode(3)
print levelOrderBottom(root)

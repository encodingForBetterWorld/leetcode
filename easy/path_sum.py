# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
from leetcode.common.TreeNode import TreeNode

def handler(leaf, s, sum):
    s += leaf.val
    if leaf.left == leaf.right == None:
        if s == sum:
            return True
    else:
        if leaf.left:
            if handler(leaf.left, s, sum):
                return True
        if leaf.right:
            if handler(leaf.right, s, sum):
                return True
    return False

def PathSum(root, sum):
    if root is None:
        return False
    if root.left:
        if handler(root.left, root.val, sum):
            return True
    if root.right:
        if handler(root.right, root.val, sum):
            return True
    if root.left == root.right == None:
        return root.val == sum
    return False

root = TreeNode(1)
root.left = TreeNode(0)

print PathSum(root, 1)
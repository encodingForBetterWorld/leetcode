# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3

# Definition for a binary tree node.\
from leetcode.common.TreeNode import TreeNode

def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
        return True
    stack = {0: root}
    pre_le = len(stack)
    while stack:
        tmp = {}
        for idx, node in stack.items():
            m_node = stack.pop(pre_le - idx - 1, None)
            if m_node is None:
                return False
            else:
                if m_node.val != node.val:
                    return False
            count = idx * 2
            if node.left:
                tmp[count] = node.left
            if m_node.right:
                tmp[pre_le*2 - count - 1] = m_node.right
            count += 1
            if node.right:
                tmp[count] = node.right
            if m_node.left:
                tmp[pre_le*2 - count - 1] = m_node.left
        pre_le *= 2
        stack = tmp
    return True

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = None
root.right.left = None
root.right.right = TreeNode(4)
root.left.left = TreeNode(4)
root.left.right = None
root.right.left = None
root.right.right = TreeNode(4)
root.left.left.right = TreeNode(5)
root.right.right.left = TreeNode(5)
root.left.left.right.right = TreeNode(6)
root.right.right.left.left = TreeNode(6)
l = TreeNode(7)
l.left = TreeNode(9)
l.right = TreeNode(0)
root.left.left.right.right.left = l
l = TreeNode(8)
l.left = TreeNode(0)
l.right = TreeNode(1)
root.left.left.right.right.right = l
l = TreeNode(8)
l.left = TreeNode(1)
l.right = TreeNode(0)
root.right.right.left.left.left = l
l = TreeNode(7)
l.left = TreeNode(0)
l.right = TreeNode(9)
root.right.right.left.left.right = l

print isSymmetric(root)
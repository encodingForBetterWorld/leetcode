# Given two binary trees, write a function to check if they are equal or not.
#
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

# Definition for a binary tree node.
from leetcode.common.TreeNode import TreeNode

def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p is None and q is None:
        return True
    elif None in (p, q):
        return False
    stack1 = [p]
    stack2 = [q]
    while stack1 and stack2:
        tmp1 = []
        tmp2 = []
        idx = 0
        while idx < len(stack1):
            leaf1 = stack1[idx]
            leaf2 = stack2[idx]
            if leaf1.val != leaf2.val:
                return False
            else:
                if leaf1.left:
                    if leaf2.left is None:
                        return False
                    else:
                        tmp1.append(leaf1.left)
                if leaf1.right:
                    if leaf2.right is None:
                        return False
                    else:
                        tmp1.append(leaf1.right)
                if leaf2.left:
                    if leaf1.left is None:
                        return False
                    else:
                        tmp2.append(leaf2.left)
                if leaf2.right:
                    if leaf1.right is None:
                        return False
                    else:
                        tmp2.append(leaf2.right)
            idx += 1
        stack1 = tmp1
        stack2 = tmp2
    return True

leef = TreeNode(2)
leef.left = TreeNode(4)
leef.right = TreeNode(5)

root = TreeNode(1)
root.left = leef
root.right = TreeNode(3)

r1 = root
r2 = TreeNode(1)

r2.left = leef
r2.right = TreeNode(4)

print isSameTree(r1, r2)

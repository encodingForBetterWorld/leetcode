# coding=utf-8
#  Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
#  According to the definition of LCA on Wikipedia:
#  “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
#
#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
#
#  For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

from leetcode.common import TreeNode

def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    stock = [root]
    lt = min(p.val, q.val)
    lg = max(p.val, q.val)
    while stock:
        tmp = []
        for node in stock:
            if lt <= node.val <= lg:
                return node
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        stock = tmp

root = TreeNode.stringToTreeNode("[2,1]")
p = TreeNode.stringToTreeNode("[2]")
q = TreeNode.stringToTreeNode("[1]")
print lowestCommonAncestor(root, p, q)

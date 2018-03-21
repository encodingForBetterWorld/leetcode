# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]
from leetcode.common import TreeNode
def binaryTreePaths(root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    ret = []
    def handle(node, path):
        path += "->%s" % node.val
        if node.left:
            handle(node.left, path)
        if node.right:
            handle(node.right, path)
        if node.right is None and node.left is None:
            ret.append(path)
    if root is not None:
        if root.left:
            handle(root.left, "%s" % root.val)
        if root.right:
            handle(root.right, "%s" % root.val)
        if root.right is None and root.left is None:
            ret.append(str(root.val))
    return ret

print binaryTreePaths(TreeNode.stringToTreeNode("[1,2,3,4,5]"))
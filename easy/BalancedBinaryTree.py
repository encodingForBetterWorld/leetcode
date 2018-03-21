from leetcode.common.TreeNode import TreeNode,stringToTreeNode

def handler(leaf):
    if leaf is None:
        return 0
    elif leaf.left == leaf.right == None:
        return 1
    else:
        left_height = handler(leaf.left)
        if left_height is False:
            return False
        right_height = handler(leaf.right)
        if right_height is False:
            return False
        if abs(left_height - right_height) > 1:
            return False
        else:
            return max(left_height+1, right_height+1)

def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
        return True
    else:
        l_h = handler(root.left)
        if l_h is False:
            return False
        r_h = handler(root.right)
        if r_h is False:
            return False
        return abs(l_h - r_h) <= 1

root = stringToTreeNode("[1,2,null,3,null,4,null,5]")
print isBalanced(root)
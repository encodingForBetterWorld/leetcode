from leetcode.common.TreeNode import TreeNode
# Given an array where elements are sorted in ascending order,
# convert it to a height balanced BST.
def handler(nums, node):
    if len(nums) == 0:return
    mid = len(nums)/2
    l_s = nums[:mid]
    if len(l_s) > 0:
        l_mid = len(l_s)/2
        l_node = TreeNode(l_s[l_mid])
        node.left = l_node
        handler(l_s, l_node)
    else:
        return
    r_s = nums[mid+1:]
    if len(r_s) > 0:
        r_mid = len(r_s)/2
        r_node = TreeNode(r_s[r_mid])
        node.right = r_node
        handler(r_s, r_node)
    else:
        return

def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    le = len(nums)
    if le == 0:
        return None
    elif le == 1:
        return TreeNode(nums[0])
    else:
        idx = le/2
        root = TreeNode(nums[idx])
    handler(nums, root)
    return root

# root = sortedArrayToBST([1,3,4,5,6])
# print root
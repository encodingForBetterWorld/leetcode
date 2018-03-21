 # Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
 #
 # Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.

from  leetcode.common import ListNode

def deleteNode(node):
    """
     :type node: ListNode
     :rtype: void Do not return anything, modify node in-place instead.
     """
    pre = None
    while node:
        if node.next is None and pre:
            pre.next = None
        elif node.next:
                node.val = node.next.val
        pre = node
        node = node.next

root = ListNode.arrayToTreeNode([1,2,3,4,5,6])
de = root.next.next

deleteNode(de)
print root


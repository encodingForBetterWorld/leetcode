# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def arrayToTreeNode(array):
    ret = head = ListNode(array[0])
    for num in array[1:]:
        head.next = ListNode(num)
        head = head.next
    return ret
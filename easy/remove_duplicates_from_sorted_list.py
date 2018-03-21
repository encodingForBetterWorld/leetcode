# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

from leetcode.common.ListNode import ListNode

def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    ret = head
    while head:
        v = head.val
        tmp = head.next
        if tmp and v == tmp.val:
            head.next = tmp.next
        else:
            head = head.next
    return ret

n = ListNode(1)
n.next = ListNode(1)
n.next.next = ListNode(2)
n.next.next.next = ListNode(2)

o = deleteDuplicates(n)
print o
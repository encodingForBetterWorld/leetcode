"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""
from leetcode.common.ListNode import ListNode

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # if l1 and l2:
    #     new_node = l1.val < l2.val and ListNode(l1.val) or ListNode(l2.val)
    # else:
    #     new_node = l1 or l2
    #     return new_node
    # count = 0
    # while True:
    #     if l1 and l2:
    #         if l1.val < l2.val:
    #             next_node = l1
    #             l1 = l1.next
    #         else:
    #             next_node = l2
    #             l2 = l2.next
    #         if count > 0:
    #             exec ("new_node%s=next_node" % (".next" * count))
    #     else:
    #         exec ("new_node%s=l1 or l2" % (".next" * count))
    #         break
    #     count += 1
    # return new_node
    l3, tail = None, None
    while l1 and l2:
        if l1.val < l2.val:
            selected = l1
            l1 = l1.next
        else:
            selected = l2
            l2 = l2.next

        if l3 is None:
            l3 = selected
        else:
            tail.next = selected
        tail = selected

    if l1:
        if l3 is None:
            l3 = l1
        else:
            tail.next = l1
    elif l2:
        if l3 is None:
            l3 = l2
        else:
            tail.next = l2

    return l3

l1 = ListNode(0)
l1.next = ListNode(2)
l1.next.next = ListNode(5)
l1.next.next.next = ListNode(5)
l1.next.next.next.next = ListNode(7)
l1.next.next.next.next.next = ListNode(9)

l2 = ListNode(1)
l2.next = ListNode(1)

ret = mergeTwoLists(l1, l2)
print ret
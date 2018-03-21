# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.


from leetcode.common.ListNode import ListNode

def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    is_repeat = False
    while head:
        val = head.val
        n = head.next
        if n and val == n.val:
            is_repeat = True
            head = n
        else:
            if is_repeat:
                head = n
                is_repeat = False
            else:
                break
    pre_val = None
    ret = pre = head
    while head:
        val = head.val
        n = head.next
        if n and val == n.val:
            pre_val = n.val
            pre.next = n.next
            head = pre
        else:
            if pre_val == val:
                pre.next = n
            else:
                pre = head
            head = head.next
    return ret

n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(2)
n.next.next.next = ListNode(2)
n.next.next.next.next = ListNode(4)
n.next.next.next.next.next = ListNode(4)
n.next.next.next.next.next.next = ListNode(5)

n = deleteDuplicates(n)

print n.val

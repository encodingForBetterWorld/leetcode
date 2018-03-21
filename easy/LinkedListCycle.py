# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?


def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head is None:
        return False
    slow = fast = head
    while slow and fast:
        slow = slow.next
        if fast.next is None:
            return False
        fast = fast.next.next
        if fast == slow:
            return True
    return False
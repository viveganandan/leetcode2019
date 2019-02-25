# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if (not head) or (head and not head.next):
            return None
        r1 = head
        r2 = head
        prev = None
        for _ in range(n - 1):
            r2 = r2.next
        while r2 and r2.next:
            prev = r1
            r1 = r1.next
            r2 = r2.next
        if prev:
            prev.next = r1.next
        else:
            head = head.next
        return head

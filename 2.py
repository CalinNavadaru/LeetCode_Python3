from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        r = head
        t = 0
        while l1 or l2:
            v = t
            if l1:
                v += l1.val
                l1 = l1.next
            if l2:
                v += l2.val
                l2 = l2.next
            t = v // 10
            r.next = ListNode(v % 10)
            r = r.next

        if t:
            r.next = ListNode(t)

        r = head.next
        del head
        return r

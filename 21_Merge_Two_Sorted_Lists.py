from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        i = list1
        j = list2
        result = ListNode(0)
        r = result
        while i is not None and j is not None:
            if i.val < j.val:
                t = ListNode(i.val)
                i = i.next
            else:
                t = ListNode(j.val)
                j = j.next

            r.next = t
            r = r.next

        while i:
            t = ListNode(i.val)
            i = i.next
            r.next = t
            r = r.next

        while j:
            t = ListNode(j.val)
            j = j.next
            r.next = t
            r = r.next

        r = result.next
        del result
        return r

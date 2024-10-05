# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(a: ListNode, b: ListNode) -> ListNode:
            p1, p2 = a, b
            ans = ListNode(-1)
            p3 = ans

            while p1 is not None and p2 is not None:
                if p1.val <= p2.val:
                    p3.next = p1
                    p3 = p3.next
                    p1 = p1.next
                else:
                    p3.next = p2
                    p3 = p3.next
                    p2 = p2.next

            while p1 is not None:
                p3.next = p1
                p3 = p3.next
                p1 = p1.next

            while p2 is not None:
                p3.next = p2
                p3 = p3.next
                p2 = p2.next

            return ans.next

        output = None

        for l in lists:
            output = merge(output, l)

        return output

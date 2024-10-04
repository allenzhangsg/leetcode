# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p = headA
        while p.next is not None:
            p = p.next
        p.next = headA

        try:
            if not headB.next:
                return None
            fast, slow = headB.next.next, headB.next
            while fast != slow:
                if not fast or not fast.next:
                    return None
                fast = fast.next.next
                slow = slow.next

            fast = headB
            while fast != slow:
                fast = fast.next
                slow = slow.next

            return fast
        finally:
            p.next = None

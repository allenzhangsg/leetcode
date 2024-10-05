# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(-1)

        p = head
        while p is not None:
            next_p = p.next
            p.next = dummyhead.next  # insert to the head
            dummyhead.next = p
            p = next_p

        return dummyhead.next

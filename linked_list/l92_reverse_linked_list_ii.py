# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummyhead = ListNode(-1)
        dummyhead.next = head
        p = dummyhead

        pos = 0
        while pos != left - 1:
            pos += 1
            p = p.next

        # p is the parent of left
        q = p.next
        p.next = None

        steps = right - left + 1

        while steps > 0:
            next_q = q.next
            q.next = p.next
            p.next = q
            q = next_q
            steps -= 1

        # now q points to the rest
        while p.next != None:
            p = p.next
        p.next = q

        return dummyhead.next

    def reverseBetween2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyhead = ListNode(-1)
        p = dummyhead

        index = 1
        cur = head

        while index <= right + 1:
            if index < left:  # insert to the tail
                p.next = cur
                cur = cur.next
                index += 1
                p = p.next
                p.next = None

            elif left <= index <= right:  # insert to the head
                next_cur = cur.next
                cur.next = p.next
                p.next = cur
                cur = next_cur
                index += 1
            else:
                while p.next is not None:
                    p = p.next
                p.next = cur
                break
        return dummyhead.next

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode(val=-1, next=head)
        l, r = dummy_head, head  # left pointer, and right pointer

        while r is not None:
            count = 1
            while count < k:
                r = r.next
                if r is None:
                    return dummy_head.next
                count += 1

            rest = r.next  # the rest of list
            r.next = None

            p = l.next  # the operation pointer
            last = l.next  # the leftmost node will be the rightmost after the sub list being reversed.
            l.next = None  # l points to the dummy head of the sub list
            while p is not None:
                # keep inserting to the head
                next_node = p.next
                p.next = l.next
                l.next = p
                p = next_node

            last.next = rest  # connect the reversed sublist with the rest
            l = last  # l points to the dummy head of the next sublist
            r = l.next

        return dummy_head.next


if __name__ == '__main__':
    s = Solution()
    s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)

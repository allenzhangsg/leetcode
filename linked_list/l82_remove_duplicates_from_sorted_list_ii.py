# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy_head = ListNode(-1)
        tail = dummy_head

        p = head
        q = p.next

        while p and q:
            count = 1
            while q and q.val == p.val:
                q = q.next
                count += 1
            if count == 1:
                tail.next = p
                tail = tail.next
                tail.next = None
            p = q
            if q:
                q = q.next

        if p:
            tail.next = p

        return dummy_head.next


if __name__ == '__main__':
    Solution().deleteDuplicates(
        # ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5))))))),
        ListNode(1, ListNode(1)),
    )

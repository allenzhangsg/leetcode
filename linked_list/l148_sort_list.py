# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Insert sort, which is slower than merge sort"""
        dummyhead = ListNode(0)

        q = head
        while q is not None:
            next_q = q.next
            p = dummyhead

            while p.next is not None and p.next.val < q.val:
                p = p.next

            if p.next is None:
                p.next = q
                q.next = None
            else:
                q.next = p.next  # 2->4
                p.next = q  # dummy ->2 ->4

            q = next_q

        return dummyhead.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Merge sort"""
        if head is None or head.next is None:
            return head

        mid = self.get_mid_node(head)
        p = head
        while p.next is not mid:
            p = p.next

        p.next = None

        left, right = head, mid
        return self.merge(
            self.sortList(left),
            self.sortList(right),
        )

    def get_mid_node(self, head):
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        output = ListNode(-1)
        last = output

        while left is not None and right is not None:
            if left.val <= right.val:
                last.next = left
                left = left.next
                last = last.next
                last.next = None
            else:
                last.next = right
                right = right.next
                last = last.next
                last.next = None
        if left is not None:
            last.next = left
        if right is not None:
            last.next = right
        return output.next

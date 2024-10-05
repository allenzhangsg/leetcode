# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        parent = {}
        p = head
        while p.next is not None:
            parent[p.next] = p
            p = p.next
        # print(parent)
        q = head

        while q != p and q.next != p:  # when q is neither p, nor the parent of p
            p.next = q.next
            q.next = p
            q = q.next
            p = parent[p]
            p.next = None

            if parent[p] == q.next or p == q.next:  # if q is the parent of p, or the grandparent of p
                break
            q = q.next


if __name__ == '__main__':
    head = ListNode(1, next=ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    Solution().reorderList(head)
    print(head)

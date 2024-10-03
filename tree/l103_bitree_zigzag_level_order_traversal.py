# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = [root]
        level_q = [1]
        ret = []
        last_level = 0

        while len(queue) > 0:
            head = queue.pop(0)
            this_level = level_q.pop(0)

            next_level = this_level + 1

            if last_level == this_level:  # on the same level
                if this_level % 2 == 1:
                    ret[-1].append(head.val)  # add to the tail
                else:
                    ret[-1].insert(0, head.val)  # add to the head
            else:  # on a new level
                ret.append([head.val])
                last_level = this_level

            left_child = head.left
            right_child = head.right

            if left_child is not None:
                queue.append(left_child)
                level_q.append(next_level)
            if right_child is not None:
                queue.append(right_child)
                level_q.append(next_level)

        return ret

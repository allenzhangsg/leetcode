# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = [root]
        level_queue = [1]

        level_list = [1]
        traversal_list = []

        while len(queue) > 0:
            cur = queue.pop()
            this_level = level_queue.pop()
            traversal_list.append(cur.val)

            if cur.left is not None:
                queue.insert(0, cur.left)
                level_list.append(this_level + 1)
                level_queue.insert(0, this_level + 1)

            if cur.right is not None:
                queue.insert(0, cur.right)
                level_list.append(this_level + 1)
                level_queue.insert(0, this_level + 1)

        print(level_list)
        print(traversal_list)
        output = []

        for i in range(len(level_list)):
            if i == len(level_list) - 1 or level_list[i] == level_list[i + 1] - 1:
                output.append(traversal_list[i])

        return output

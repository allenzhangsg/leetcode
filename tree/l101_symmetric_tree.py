# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def func(a, b) -> bool:
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            return a.val == b.val and func(a.left, b.right) and func(a.right, b.left)

        if root is None:
            return True
        else:
            return func(root.left, root.right)

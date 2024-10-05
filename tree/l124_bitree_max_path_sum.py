# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Info:
    def __init__(self, max_sum, max_sum_with_root):
        self.max_sum = max_sum
        self.max_sum_with_root = max_sum_with_root  # root as endpoint of path


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def func(node: TreeNode) -> Optional[Info]:
            if node is None:
                return None

            left_info = func(node.left)
            right_info = func(node.right)
            if left_info is not None and right_info is not None:
                max_sum_with_root = max(
                    left_info.max_sum_with_root + node.val,
                    right_info.max_sum_with_root + node.val,
                    node.val,
                )
                max_sum = max(
                    max_sum_with_root,
                    left_info.max_sum_with_root + right_info.max_sum_with_root + node.val,
                    left_info.max_sum,
                    right_info.max_sum,
                )
            elif left_info is None and right_info is not None:
                max_sum_with_root = max(
                    right_info.max_sum_with_root + node.val,
                    node.val,
                )
                max_sum = max(
                    max_sum_with_root,
                    right_info.max_sum,
                )
            elif left_info is not None and right_info is None:
                max_sum_with_root = max(
                    left_info.max_sum_with_root + node.val,
                    node.val,
                )
                max_sum = max(
                    max_sum_with_root,
                    left_info.max_sum,
                )
            else:
                max_sum_with_root = node.val
                max_sum = max_sum_with_root

            return Info(max_sum, max_sum_with_root)

        info = func(root)
        return info.max_sum

# Definition for a binary tree node.
from functools import reduce
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        num = []
        path_list = []

        def traverse(root):  # mid first
            num.append(root.val)
            if root.left is None and root.right is None:
                path_list.append(int(reduce(lambda x, y: f"{x}{y}", num)))

            if root.left is not None:
                traverse(root.left)
            if root.right is not None:
                traverse(root.right)
            num.pop()

        traverse(root)
        return sum(path_list)


if __name__ == '__main__':
    print(Solution().sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))))

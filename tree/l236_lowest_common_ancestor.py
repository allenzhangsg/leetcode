class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Info:
    def __init__(self, ancestor=None, has_p=False, has_q=False):
        self.ancestor = ancestor
        self.has_p = has_p
        self.has_q = has_q


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def func(head: TreeNode) -> Info:
            if head is None:
                return Info()

            left = func(head.left)
            right = func(head.right)

            if left.ancestor is not None:
                return Info(ancestor=left.ancestor)
            if right.ancestor is not None:
                return Info(ancestor=right.ancestor)

            if head == p:
                if left.has_q or right.has_q:
                    return Info(ancestor=head)
                else:
                    return Info(has_p=True)
            if head == q:
                if left.has_p or right.has_p:
                    return Info(ancestor=head)
                else:
                    return Info(has_q=True)

            if left.has_p and right.has_q \
                    or left.has_q and right.has_p:
                return Info(ancestor=head)
            elif left.has_p or right.has_p:
                return Info(has_p=True)
            elif left.has_q or right.has_q:
                return Info(has_q=True)
            else:
                return Info()

        info = func(root)
        return info.ancestor


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    s.lowestCommonAncestor(root, root.left, root)

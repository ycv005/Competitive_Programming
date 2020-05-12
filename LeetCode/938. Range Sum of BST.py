def inRangeAdd(n, l, r):
    """Number in range, then return n else 0"""
    if n>=l and n<=r:
        return n
    return 0

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root:
            return inRangeAdd(root.val, L, R) + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        return 0

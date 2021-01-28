# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def doMerging(self, t1, t2):
        if t1 and t2:
            t1.val += t2.val
            if t1.left:
                self.doMerging(t1.left, t2.left)
            elif t2.left:
                t1.left = t2.left

            if t1.right:
                self.doMerging(t1.right, t2.right)
            elif t2.right:
                t1.right = t2.right

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        self.doMerging(t1, t2)
        return t1

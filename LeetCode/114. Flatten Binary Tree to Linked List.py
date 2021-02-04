# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None

    def flattening(self, root):
        if root:
            self.flattening(root.right)
            self.flattening(root.left)

            root.right = self.prev
            root.left = None
            self.prev = root

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flattening(root)
        return root

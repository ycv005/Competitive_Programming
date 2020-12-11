# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def doIncreasingOrder(self, prev, root):
        if root:
            doIncreasingOrder(root, root.right)
            doIncreasingOrder(root, root.left)
            if root.left:
                prev.right = root.left

    def increasingBST(self, root: TreeNode) -> TreeNode:
        doIncreasingOrder(root, root.right)
        doIncreasingOrder(root, root.left)
        return root

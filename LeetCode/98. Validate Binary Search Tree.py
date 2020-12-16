# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.last_visited_val = float('-inf')
        self.isValid = True

    def isValidInorder(self, root):
        if root:
            self.isValidBST(root.left)
            if self.isValid and root.val <= self.last_visited_val:
                self.isValid = False
            else:
                self.last_visited_val = root.val
            self.isValidBST(root.right)
        return self.isValid

    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidInorder(root, False, False)

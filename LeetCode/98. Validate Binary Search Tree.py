# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    lastElement = "NA"
    valid = True

    def checkValiditiy(self, root):
        if root:
            self.checkValiditiy(root.left)
            if self.lastElement == "NA":
                self.lastElement = root.val
            else:
                if self.lastElement >= root.val:
                    self.valid = False
                    return
                self.lastElement = root.val
            self.checkValiditiy(root.right)

    def isValidBST(self, root: TreeNode) -> bool:
        self.checkValiditiy(root)
        return self.valid

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
        self.sm = 0

    def traverse(self, root, hsmp, t):
        if root:
            self.sm += root.val
            tmp = hsmp.get(self.sm - t, 0)
            self.res += tmp
            hsmp[self.sm] = hsmp.get(self.sm, 0) + 1

            self.traverse(root.left, hsmp, t)
            self.traverse(root.right, hsmp, t)

            hsmp[self.sm] = hsmp.get(self.sm, 0) - 1
            self.sm -= root.val

    def pathSum(self, root: TreeNode, t: int) -> int:
        hsmp = {}
        hsmp[0] = 1
        self.traverse(root, hsmp, t)
        return self.res

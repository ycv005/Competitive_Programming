# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = None

    def recurse(self, root, p, q):
        if not root:
            return False

        lt = self.recurse(root.left, p, q)
        rt = self.recurse(root.right, p, q)

        curr = (root == p) or (root == q)
        if curr + lt + rt >= 2:
            self.res = root

        return lt or rt or curr

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.recurse(root, p, q)
        return self.res

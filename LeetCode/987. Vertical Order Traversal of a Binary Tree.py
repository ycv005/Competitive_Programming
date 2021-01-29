from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def doVerticalTrav(self, root, pos, depth, hsmp):
        if root:
            hsmp[pos].append([root.val, depth])
            self.doVerticalTrav(root.left, pos - 1, depth + 1, hsmp)
            self.doVerticalTrav(root.right, pos + 1, depth + 1, hsmp)

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        hsmp = defaultdict(list)
        self.doVerticalTrav(root, 0, 0, hsmp)
        res = []
        for k in sorted(hsmp.keys()):
            v = hsmp[k]
            v.sort(key=lambda x: (x[1], x[0]))
        return res

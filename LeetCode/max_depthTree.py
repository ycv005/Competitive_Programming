def get_depthTree(root,max_dep, cur_dep):
    if root:
        max_dep[0]=max(max_dep[0], cur_dep)
        get_depthTree(root.left,max_dep, cur_dep+1)
        get_depthTree(root.right,max_dep, cur_dep+1)
        
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_dep=[0]
        get_depthTree(root,max_dep, 1)
        return max_dep[0]

# https://leetcode.com/problems/maximum-depth-of-binary-tree/
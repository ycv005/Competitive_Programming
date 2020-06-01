def traverse(root, wrapper):
    if root:
        traverse(root.left, wrapper)
        wrapper[1] -=1
        if wrapper[1]==0:
            wrapper[0] = root.val
            return
        traverse(root.right, wrapper)


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        wrapper =[0, k]
        traverse(root, wrapper)
        return wrapper[0]

# above was simple approach
#  below is advance approach that looks for kthSmallest even tree modifies

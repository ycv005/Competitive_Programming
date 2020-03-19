def get_depthTree(root,wrapper,height):
    if root and height<wrapper[0]:
        get_depthTree(root.left,wrapper,height+1)
#         at the leaf node
        if not root.left and not root.right:
            wrapper[0]=height
        get_depthTree(root.right,wrapper,height+1)
    
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        wrapper = [99999999999999999] #stores a depth, which will be consider as min, and will discard all path greater than this
        get_depthTree(root,wrapper, 1)
        return wrapper[0]
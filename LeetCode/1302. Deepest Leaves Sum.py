def inOrder(root,wrapper,mxh):
    if root:
        inOrder(root.left,wrapper,mxh+1)
        if not root.left and not root.right and mxh>=wrapper[0]: #at leaf, only append those whose height is more than stored mxh
            wrapper[0]=mxh
            wrapper.append([mxh,root.val])
        inOrder(root.right,wrapper,mxh+1)

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        wrapper = [0] #wrapper with max height and leave node with those height
        inOrder(root,wrapper,0)
        s=0
        for i in range(1,len(wrapper)):
            if wrapper[i][0]>=wrapper[0]:
                s+=wrapper[i][1]
        return s

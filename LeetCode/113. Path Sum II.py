def inOrder(root,wrapper,l):
    if root:
        l.append(root.val)
        inOrder(root.left,wrapper,l)
        if not root.left and not root.right and sum(l)==wrapper[0]: #leaf node
            wrapper.append(l[:])   #append a copy, not l, bcoz if l modify, then wrapper list will too
        inOrder(root.right,wrapper,l)
#         just finish completing this node, so poping out, right most
        l.pop()

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        wrapper=[sum]
        inOrder(root,wrapper,[])
        return wrapper[1:]
def getPath(wrapper,l):
    s=""
    for i in l:
        s+=str(i)
    wrapper[0]+=int(s)

def inOrder(root,wrapper,l):
    if root:
        l.append(root.val)
        inOrder(root.left,wrapper,l)
        if not root.left and not root.right:
            getPath(wrapper,l)
        inOrder(root.right,wrapper,l)
        l.pop()

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        wrapper = [0]
        l=[]
        inOrder(root,wrapper,l)
        return wrapper[0]
        # https://leetcode.com/problems/sum-root-to-leaf-numbers/
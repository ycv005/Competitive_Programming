def consecutive_in(B,A):
    return B in (A[i:i+len(B)] for i in range(len(A)))    
    
def got_path(stack, wrapper):
    if wrapper[0]!=True:
        wrapper[0]=consecutive_in(wrapper[1],stack)

def inOrder(head, root, stack, wrapper):
    if root:
        stack.append(root.val)
        if wrapper[0]!=True:
            inOrder(head, root.left, stack,wrapper)
        if root.left==None and root.right==None and wrapper[0]!=True:
            got_path(stack, wrapper)
        if wrapper[0]!=True:
            inOrder(head, root.right, stack,wrapper)
        stack.pop()

def get_node(head):
    l=[]
    t=head
    while t!=None:
        l.append(t.val)
        t=t.next
    return l
        
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        is_matched = False
        all_node = get_node(head)
        wrapper = [is_matched,all_node]
        stack = []
        inOrder(head, root, stack, wrapper)
        return wrapper[0]
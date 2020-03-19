from collections import deque

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        s=0
        if not root:
            return 0
        deq = deque()
        deq.append(root)
        while deq:
            node = deq.popleft()
            if node.left:
                deq.append(node.left)
                if not node.left.left and not node.left.right:
                    s+=node.left.val
            if node.right:
                deq.append(node.right)
        return s

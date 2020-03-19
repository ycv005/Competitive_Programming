from collections import deque

#picking last element from the deq (only works when you append left at last)
# if in last row, no left is present, we have to pick rightmost

# special case [0, null, -1]
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        deq = deque()
        tmp=root
        deq.append(root)
        while deq:
            node=deq.popleft()
            if node.right:
                deq.append(node.right)
            if node.left:
                deq.append(node.left)
            if deq: 
                tmp=deq[-1]
        return tmp.val
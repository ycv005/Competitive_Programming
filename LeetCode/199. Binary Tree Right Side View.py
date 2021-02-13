from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # will be doing lvl order trav.

        que = deque()
        que.append(root)
        # None is a symbol for the level end

        que.append(None)
        res = []

        while len(que) > 0:
            node = que.popleft()

            # reach to the end of the loop
            if node == None and len(que) == 0:
                continue
            # lvl change
            elif node == None and len(que) > 0:
                que.append(None)
            else:
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                if que[0] == None:
                    res.append(node.val)

        return res

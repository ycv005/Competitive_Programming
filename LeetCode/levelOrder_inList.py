def get_levelOrder(root, que, curLevel):
    if root:
        if len(que)<curLevel:
            que.append([root.val])
        else:
            que[curLevel-1].append(root.val)
        get_levelOrder(root.left, que, curLevel+1)
        get_levelOrder(root.right, que, curLevel+1)

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que = []
        get_levelOrder(root, que, 1)
        # print(que)
        return que
        
# https://leetcode.com/problems/binary-tree-level-order-traversal/
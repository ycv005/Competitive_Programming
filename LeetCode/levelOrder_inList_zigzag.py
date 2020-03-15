def get_levelOrder(root, que, curLevel):
    if root:
        if len(que)<curLevel:
            que.append([root.val])
        else:
            if curLevel%2==0:
                que[curLevel-1] = [root.val] + que[curLevel-1] 
            else:
                que[curLevel-1].append(root.val)
        get_levelOrder(root.left, que, curLevel+1)
        get_levelOrder(root.right, que, curLevel+1)

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que = []
        get_levelOrder(root, que, 1)
        # print(que)
        return que

# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
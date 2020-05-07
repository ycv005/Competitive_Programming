def levelOrderCheck(root, depth, x, y, depth_x_y):
    if root and depth_x_y[2] == None:
        if root.left and root.right and (root.left.val == x or root.left.val == y) and (root.right.val == x or root.right.val == y):
            depth_x_y[2] = False
            return
        if root.val == x:
            depth_x_y[0] = depth
        if root.val == y:
            depth_x_y[1] = depth

        if depth_x_y[0] != -1 and depth_x_y[1] != -1:
            depth_x_y[2] = depth_x_y[0] == depth_x_y[1]
            return
        levelOrderCheck(root.right, depth + 1, x, y, depth_x_y)
        levelOrderCheck(root.left, depth + 1, x, y, depth_x_y)

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # if x == y: return False
        depth_x_y = [-1, -1, None] # x_depth, y_depth, isCousins bool
        levelOrderCheck(root, 0, x, y, depth_x_y)
        return depth_x_y[2]

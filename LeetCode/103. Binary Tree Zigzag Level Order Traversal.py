class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        lvl = 0
        que = []
        res = []
        
        que.append(root)
        while len(que)>0:
            if len(res) <= lvl:
                res.append([])
            
            col= res[lvl]
            
            for i in range(len(que)):
                node = que.pop(0)
                
                if lvl % 2==0:
                    col.append(node.val)
                else:
                    col.insert(0, node.val)
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            # print(col)
            lvl += 1
            
        return res
        
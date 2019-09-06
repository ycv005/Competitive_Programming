class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def traverseCount(root,t,c):
    if root!=None:
        c+=1
        if c in t:
            # append to list
            t[c].append([root.info])
        else:
            # create list
            t[c]=[root.info]
        traverseCount(root.left,t,c)
        traverseCount(root.right,t,c)
    return t


def levelOrder(root):
    t={}
    count=0
    traverseCount(root,t,count)
    for i in range(len(t)):
        for j in t[i+1]:
            if isinstance(j,int):
                print(j,end=" ")
            else:
                print(j[0],end=" ")


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)
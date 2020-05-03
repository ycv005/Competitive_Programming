from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.max_size = capacity
        self.current_size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key]
            self.cache.move_to_end(key)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return
        if self.current_size>=self.max_size:
            self.cache.popitem(last=False)
            self.current_size-=1
        self.cache[key] = value
        self.current_size+=1

#---------------Above method uses library function--------------
# -------------- Below method uses scratch function ------------


from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.max_size = capacity
        self.current_size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key]
            self.cache.move_to_end(key)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return
        if self.current_size>=self.max_size:
            self.cache.popitem(last=False)
            self.current_size-=1
        self.cache[key] = value
        self.current_size+=1

#---------------Above method uses library function--------------
# -------------- Below method uses scratch function ------------


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        # front pointer, dummy node with dummy value
        self.front = Node(-1, -1)
        # rear pointer, dummy Node with dummy value
        self.rear = Node(-1, -1)
        # doubly linked list setup
        self.front.next = self.rear
        self.rear.prev = self.front

    def put(self, key, val):
        # dictionary.get(key, DefaultValue)
        node = self.cache.get(key, None) #if set None as default
        if not node:
            # create a node
            node = Node(key, val)
            self.addNodeToStart(node)
            # storing it in LRUCache
            self.cache[key] = node
            self.size += 1
            if self.size > self.capacity:
                # now, removing least used Node
                removedNode = self.removeLastNode()
                del self.cache[removedNode.key]
                self.size -= 1
        else:
            node.val = val
            self.moveNodeToTop(node)

    def addNodeToStart(self, node):
        node.prev = self.front
        node.next = self.front.next

        self.front.next.prev = node
        self.front.next = node

    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def moveNodeToTop(self, node):
        self.removeNode(node)
        self.addNodeToStart(node)

    def removeLastNode(self):
        node = self.rear.prev
        self.removeNode(node)
        return node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.moveNodeToTop(node)
            return node.val
        return -1

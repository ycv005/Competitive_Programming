class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def heapSize(self):
        return self.size

    def peek(self):
        if self.size == 0:
            return None
        return self.heap[0]

    def display(self):
        if self.size == 0:
            return None
        for i in range(self.size):
            n = self.heap[i]
            print(n, end=" ")
        print()

    def insert(self, val):
        self.heap.append(val)
        self.size += 1
        self.upHeapify(self.size - 1)

    def parentIndex(self, index):
        return index // 2

    def leftChildIndex(self, index):
        if index == 0:
            return 1
        tmp = index * 2
        return tmp if tmp and tmp < self.size else None

    def rightChildIndex(self, index):
        if index == 0:
            return 2
        tmp = self.leftChildIndex(index)
        return tmp + 1 if tmp and tmp < self.size else None

    def downHeapify(self, index):
        if self.safeIndex(index):
            li = self.leftChildIndex(index)
            ri = self.rightChildIndex(index)
            if li and ri:
                if self.heap[index] <= self.heap[li] or self.heap[index] <= self.heap[ri]:
                    if self.heap[li] > self.heap[ri]:
                        self.swap(index, li)
                        self.downHeapify(li)
                    else:
                        self.swap(index, ri)
                        self.downHeapify(ri)
            elif li or ri:
                # only 1 child
                if li and self.heap[index] <= self.heap[li]:
                    self.swap(index, li)
                    self.downHeapify(li)
                elif ri and self.heap[index] <= self.heap[ri]:
                    self.swap(index, ri)
                    self.downHeapify(ri)
            else:
                # No child
                pass

    def upHeapify(self, index):
        if self.safeIndex(index):
            pi = self.parentIndex(index)
            if self.heap[pi] < self.heap[index]:
                self.swap(pi, index)
                self.upHeapify(pi)

    def pop(self):
        if self.size == 0:
            return None
        tmp = self.heap[0]
        self.swap(0, self.size - 1)
        self.size -= 1
        self.heap.pop()
        self.downHeapify(0)
        return tmp

    def safeIndex(self, i):
        return i >= 0 and i < self.size

    def swap(self, i, j):
        if self.safeIndex(i) and self.safeIndex(j):
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


maxHeap = MaxHeap()
maxHeap.insert(5)
maxHeap.insert(3)
maxHeap.insert(17)
maxHeap.insert(10)
maxHeap.insert(84)

maxHeap.display()
maxHeap.pop()

maxHeap.display()
maxHeap.insert(19)
maxHeap.insert(6)
maxHeap.insert(22)
maxHeap.insert(9)

maxHeap.display()

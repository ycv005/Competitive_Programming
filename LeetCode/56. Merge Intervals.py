def doMerge(deq,b):
    if len(deq)>0:
        # b will be top of stack, as we are going to add
        a=deq.pop()
        if max(b)<min(a): # b is covered by a, so reversing them
            doMerge(deq,b)
            deq.append(a)
        elif a[0]>=b[0] and a[-1]<=b[-1]:   #a is covered by b
            doMerge(deq,b)
        elif a[-1]>=b[0]: #good for merge
            b=[min(a[0],b[0]),max(a[-1],b[-1])]
            doMerge(deq,b)
        else: #no-merge
            deq.append(a)
            deq.append(b)
    else: #do the stack is empty, so append b
        deq.append(b)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<2:
            return intervals
        deq = [] # or use deque([])
        t=intervals[0]
        deq.append(t)
        for i in range(1,len(intervals)):
            t=intervals[i]
#           before inserting into the stack, we will try to merge them, else append it.
            doMerge(deq,t)
        return deq

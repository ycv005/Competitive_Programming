class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr)==0:
            return 0
        elif len(arr)<3:
            return arr[0]
        prev,size=-1,0
        thres=0.25*len(arr)
        for i in arr:
            if prev==i:
                size+=1
                if size>thres:
                    return prev
            else:
                size=1
            prev=i
                
        # https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
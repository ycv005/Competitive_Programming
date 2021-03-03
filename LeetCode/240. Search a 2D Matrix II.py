class Solution:
    def doBinarySearch(self, arr, target):
        if arr == None or target == None:
            return -1
        l = 0
        r = len(arr)-1
        while l < r:
            m = (l + r)//2
            if target == arr[m]:
                return m
            elif target < arr[m]:
                r = m - 1
            else:
                l = m + 1

        if target == arr[l]:
            return l
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None or matrix[0] == None:
            return False
        for arr in matrix:
            if arr[0] <= target and target <= arr[len(arr)-1]:
                val = self.doBinarySearch(arr, target)
                if val != -1:
                    return True

        return False

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        isIncreasing = True
        isDecreasing = False
        for i in range(len(A)-1):
            if A[i] == A[i+1]:
                # either strictly inc or dec
                return False
            if isIncreasing:
                if A[i] > A[i+1]:
                    if i == 0:
                        # Mountain Starts falling from starting
                        return False
                    isDecreasing = True
                    isIncreasing = False
            elif isDecreasing:
                if A[i] < A[i+1]:
                    return False
        if not isDecreasing:
            # means, we mountain only raise but didn't fall
            return False
        return True

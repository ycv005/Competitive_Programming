class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {}
        for a in arr:
            if 2*a in d or (int(a/2) in d and a/2 == int(a/2)):
                return True
            else:
                d[a]=1
        return False

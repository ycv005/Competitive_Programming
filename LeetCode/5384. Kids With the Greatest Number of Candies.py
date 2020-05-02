class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = float('-inf')
        # mn = float('inf')
        for c in candies:
            mx = max(mx, c)
            # mn = max(mn, c)
        res = []
        for c in candies:
            if c+extraCandies>=mx:
                res.append(True)
            else:
                res.append(False)
        return res

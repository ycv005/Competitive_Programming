class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt = num**0.5
        return int(sqrt)==sqrt

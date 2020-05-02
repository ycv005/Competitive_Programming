from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stones = Counter(S)
        s=0
        for j in J:
            if j in stones:
                s+=stones[j]
        return s

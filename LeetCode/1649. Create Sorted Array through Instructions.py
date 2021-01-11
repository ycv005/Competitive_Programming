from sortedcontainers import SortedList


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        Slist = SortedList()
        cost = 0
        for n in instructions:
            cost += min(Slist.bisect_left(n),
                        len(Slist) - Slist.bisect_right(n))
            cost %= MOD
            Slist.add(n)
        return cost

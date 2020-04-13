import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-val for val in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x1 = heapq.heappop(stones)
            x2 = heapq.heappop(stones)
            if x1 != x2:
                heapq.heappush(stones,x1-x2)
        return -stones[0] if stones else 0

from heapq import heappop, heappush


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])

        minHeap = [(0, 0, 0)]  # distance, row, col
        dist = [[float('inf') for j in range(m)] for i in range(n)]
        direction = [0, 1, 0, -1, 0]
        while minHeap:
            d, r, c = heappop(minHeap)
            if d > dist[r][c]:
                # already relaxed
                continue
            if r == n-1 and c == m-1:
                return d
            for i in range(4):
                nr, nc = r + direction[i], c + direction[i + 1]
                if 0 <= nr and 0 <= nc and nr < n and nc < m:
                    newDist = max(d, abs(heights[r][c] - heights[nr][nc]))
                    if newDist < dist[nr][nc]:
                        dist[nr][nc] = newDist
                        heappush(minHeap, (newDist, nr, nc))

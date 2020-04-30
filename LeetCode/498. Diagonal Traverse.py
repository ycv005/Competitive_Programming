class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        if not nums or not nums[0]:
            return []
        N, M = len(nums), len(nums[0])
        row, col = 0, 0
        direction = 1
        res = []
        while row < N and col < M:
            res.append(nums[row][col])
            new_row = row + (-1 if direction == 1 else 1)
            new_col = col + (1 if direction == 1 else -1)
            if new_row < 0 or new_row == N or new_col < 0 or new_col == M:
                if direction:
                    # up
                    row += (col == M-1)
                    col += (col < M-1)
                else:
                    # down
                    col += (row == N-1)
                    row += (row < N-1)
                direction =  1 - direction
            else:
                row = new_row
                col = new_col
        return res

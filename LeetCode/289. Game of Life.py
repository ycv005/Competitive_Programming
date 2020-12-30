class Solution:
    # let's use a representation
    # for change occur for 0->1, place their 2
    # for change occur for 1->0, place their 3
    # return value as % 2, will work for 0, 1, 2, 3

    def getValue(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return 0
        return board[i][j] % 2

    def getLiveNeighbour(self, board, i, j):
        count = 0
        # horizontal
        count += self.getValue(board, i, j+1) + self.getValue(board, i, j - 1)
        # vertical
        count += self.getValue(board, i - 1, j) + \
            self.getValue(board, i + 1, j)
        # diagonal
        count += self.getValue(board, i-1, j - 1) + \
            self.getValue(board, i+1, j + 1)
        # opp. diagonal
        count += self.getValue(board, i+1, j - 1) + \
            self.getValue(board, i-1, j + 1)
        return count

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0 and self.getLiveNeighbour(board, i, j) == 3:
                    board[i][j] = 2
                elif board[i][j] == 1:
                    nbr = self.getLiveNeighbour(board, i, j)
                    if nbr < 2 or nbr > 3:
                        board[i][j] = 3
        # retriving all the value to correct answer
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0

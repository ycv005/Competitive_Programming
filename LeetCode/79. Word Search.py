class Solution:
    def isSafe(self, matrix, i, j):
        return i >= 0 and j >= 0 and i < len(matrix) and j < len(matrix[0])

    def isWordPresent(self, board, i, j, word, k):
        if k == len(word):
            return False
        if not self.isSafe(board, i, j):
            return False

        tmp = board[i][j]
        board[i][j] = " "
        if k == len(word)-1 and word[k] == tmp:
            res = True
        elif word[k] != tmp:
            res = False
        else:
            res = self.isWordPresent(
                board, i+1, j, word, k+1) or self.isWordPresent(board, i-1, j, word, k+1) or self.isWordPresent(board, i, j-1, word, k+1) or self.isWordPresent(board, i, j+1, word, k+1)
        board[i][j] = tmp
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j] and self.isWordPresent(board, i, j, word, 0):
                    return True
        return False

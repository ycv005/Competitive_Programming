class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        s = int("".join(map(str, A))) + 1
        return list(str(s))

# https://www.interviewbit.com/problems/add-one-to-number/
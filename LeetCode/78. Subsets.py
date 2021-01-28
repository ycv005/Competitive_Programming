class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for n in nums:
            output += [curr + [n] for curr in output]

        return output

class Solution:
    def mostCompetitive(self, nums, k):
        attemptYouCanTry = len(nums) - k
        st = []
        for n in nums:
            while len(st) > 0 and st[-1] > n and attemptYouCanTry > 0:
                st.pop()
                attemptYouCanTry -= 1
            st.append(n)

        return st[:k]

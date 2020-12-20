class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        curr_with_last_3comb = 6
        curr_with_last_2comb = 6
        for i in range(2, n+1):
            tmp = last_2comb

            curr_with_last_2comb = 3 * tmp + 2 * curr_with_last_3comb
            curr_with_last_3comb = 2 * tmp + 2 * curr_with_last_3comb
        return (curr_with_last_2comb + curr_with_last_3comb) % MOD

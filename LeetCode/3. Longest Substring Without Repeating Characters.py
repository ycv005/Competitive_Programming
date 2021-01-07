class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        mx_len = cur_mx_len = 1
        hmp = {}
        hmp[s[0]] = 0
        i = 0
        j = 1
        dont_check_below_this_index = 0
        while j < len(s):
            if s[j] in hmp and hmp[s[j]] >= dont_check_below_this_index:
                i = hmp[s[j]] + 1
                cur_mx_len = j - i + 1
                dont_check_below_this_index = i
            else:
                cur_mx_len += 1

            hmp[s[j]] = j
            mx_len = max(mx_len, cur_mx_len)

            j += 1
        return mx_len

#https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(s):
    d={}
    start=0 #after which we have to lookup into the dictionary
    mx = 0
    for i,c in enumerate(s):
        if c in d and d[c]>=start:
            start = d[c] + 1
            d[c]=i
        else:
            d[c]=i
        mx = max(mx, i - start + 1)
    print(mx)

s = "argejapa"
lengthOfLongestSubstring(s)

def longestSubArray(p):
    i = 0
    j = 1
    curr_lg = max_lg = 1
    while j<len(p):
        if p[j] - p[j-1] <=2:
            curr_lg += 1
        else:
            curr_lg = 1
        j += 1
        max_lg = curr_lg if curr_lg > max_lg else max_lg
    return max_lg

def shortestSubArray(p):
    i = 0
    j = 1
    curr_sm = min_sm = len(p)
    while j<len(p):
        if p[j] - p[j-1] >2:
            if j == len(p)-1:
                curr_sm = 1
            else:
                curr_sm = (j - 1) - i + 1
            i = j
        elif j == len(p)-1:
            curr_sm = j - i + 1
        j+=1
        min_sm = curr_sm if curr_sm < min_sm else min_sm
    return min_sm

for t in range(int(input())):
    n = int(input())
    p = [int(i) for i in input().split()]
    sm = shortestSubArray(p) # subarray with consecutive element <=2
    lg = longestSubArray(p) # subarray with consecutive element <=2
    print(sm, lg)

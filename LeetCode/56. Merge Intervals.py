# we have two list, we need to check do they merge or not.
def isOverlapping(l1, l2):
    a, b = l1
    c, d = l2
    # if a or b are in range of c-d
    # if c or d are in range of a-b
    if (c <= a and a <= d) or (c <= b and b <= d) or (a <= c and c <= b) or (a <= d and d <= b):
        return True
    return False


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: -x[1])
        # print(intervals)
        prev = intervals[0]
        i = 1
        while i < len(intervals):
            curr = intervals[i]
            if isOverlapping(prev, curr):
                # print("overlap-",prev,curr)
                intervals[i-1][0] = min(prev[0], curr[0])
                intervals[i-1][1] = max(prev[1], curr[1])
                intervals.pop(i)

            else:
                prev = curr
                i += 1
            # print("end of loop-", prev, curr)
        return intervals

def insert(intervals, new_interval):
    if new_interval[0] > intervals[-1][-1]:
        # print("1")
        return intervals + [new_interval]
    elif new_interval[-1] < intervals[0][0]:
        # print("2")
        return list(new_interval) + intervals
    else:
        # print("3")
        m1 = -1
        m2 = -1
        for i in range(len(intervals)):
            if new_interval[0] in range(intervals[i][0],intervals[i][-1]+1):
                if m1==-1:
                    m1 = i
                if new_interval[-1] in range(intervals[i][0],intervals[i][-1]+1):
                    return intervals
                else:
                    continue
            elif new_interval[-1] in range(intervals[i][0],intervals[i][-1]+1):
                if m1>=0:
                    m2 = i

        if m1==-1 and m2 ==-1:
            return intervals
        elif m1>=0 and m2==-1:
            intervals[m1][0] = min(intervals[m1][0],new_interval[0])
            intervals[m1][1] = max(intervals[m1][1],new_interval[1])
        else:
            a = min(intervals[m1][0],new_interval[0])
            b = max(intervals[m2][1],new_interval[1]) 
            intervals[m1:m2+1] = tuple([[a,b]])

        return intervals


intervals = [ (1, 2), (3, 6) ]
new_interval = (10, 8)
l = insert(intervals,tuple(sorted(new_interval)) )
for i in l:
    print(i,end=" ")

# https://www.interviewbit.com/problems/merge-intervals/
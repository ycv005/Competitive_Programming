# https://www.interviewbit.com/problems/max-non-negative-subarray/
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, l):
        if len(l)<1:
            return l

        start=end=sm=mx=0
        index = [start,end]
        for i,v in enumerate(l):
            if v>=0:
                sm+=v
                if mx==sm:
                    # may be, we need to change index
                    end=i
                    if end-start>index[-1]-index[0]:
                        index=[start,end]
                if mx<sm:
                    mx=sm
                    end=i
                    index = [start,end]
            else:
                # print("got neg v")
                sm=0
                if i+1<len(l):
                    start=i+1

        # print(index)
        if index[0]==index[1] and l[index[1]]<0: #only negative no.
            # print("all neg")
            return []
        return l[index[0]:index[1]+1]

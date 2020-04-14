class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_score = [0]*(N+1) #0 is the dummy person
        for a,b in trust:
            trust_score[a]-=1
            trust_score[b]+=1

        for idx, val in enumerate(trust_score):
            if idx!=0 and val==N-1:
                return idx
        return -1

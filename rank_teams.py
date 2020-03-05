class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        if len(votes)==1:
            return votes[0]
        alpha = {}
        rank=[0 for i in range(len(votes[0]))]
        for i in votes[0]:
            alpha[i]=[0 for j in range(len(votes[0]))]
        for v in votes:
            for i in range(len(v)):
                alpha[v[i]][i]+=1
#         sorted in reverse order, + sorting on alphabetical order
        return ''.join(sorted(votes[0], key= lambda l: (alpha[l], -ord(l)), reverse=True))
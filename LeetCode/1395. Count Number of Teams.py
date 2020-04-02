class Solution:
    def numTeams(self, rating: List[int]) -> int:
        c=0
        for j in range(len(rating)):
            left_small=right_great=0
            left_great=right_small=0
            for i in range(len(rating)):
                if rating[i]<rating[j] and i<j:
                    left_small+=1
                elif rating[i]>rating[j] and i<j:
                    left_great+=1
                elif rating[i]<rating[j] and i>j:
                    right_small+=1
                elif rating[i]>rating[j] and i>j:
                    right_great+=1
            c+=left_small*right_great + left_great*right_small
        return c

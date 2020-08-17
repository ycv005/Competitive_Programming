class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0]*(num_people)
        i = 1
        while candies>0:
            if i > candies:
                res[(i-1)%num_people] += candies
                break
            else:
                candies -= i
            res[(i-1)%num_people] += i
            i += 1
        return res

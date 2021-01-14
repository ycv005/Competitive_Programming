class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people)-1
        count = 0
        people.sort()
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            count += 1

        return count

import math
def get_cd(n,ps):
    ps= math.floor(ps)
    while ps:
        if n%ps==0:
            return [int(ps), int(n/ps)]
        ps-=1
    
class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ps = math.sqrt(num+1)
        ps1 = math.sqrt(num+2)
        t1 = get_cd(num+1,ps)
        t2 = get_cd(num+2,ps1)
        if int(abs(t1[0]-t1[1]))-int(abs(t2[0]-t2[1]))<0:
            return t1
        else:
            return t2
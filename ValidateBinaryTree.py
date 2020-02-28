#   using dic for checking closed  tree or not
def check_dic(d,l):
    if l in d:
        return False
    else:
        d[l]=1

class Solution(object):
    def validateBinaryTreeNodes(self, n, l, r):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        val = True
        d={0:1}
        is_present = 1
        # pos_node = 0 
        for i in range(n):
            if r[i]!=-1:
                if check_dic(d,r[i]) == False:
                    # print("1st false")
                    return False
            if l[i]!=-1:
                if check_dic(d,l[i]) == False:
                    # print("2st false")
                    return False
            if is_present not in l and is_present not in r and is_present<n:
                # print("3st false")
                return False
            is_present+=1
        return val
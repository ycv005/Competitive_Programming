class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for st in strs:
            sorted_st = ''.join(sorted(st))
            if sorted_st not in dic:
                dic[sorted_st] = [st]
            else:
                dic[sorted_st].append(st)
        return [v for v in dic.values()]

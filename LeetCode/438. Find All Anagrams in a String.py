from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq = defaultdict(int)

        for char in p:freq[char]+=1
        counter = len(freq)
        beg = 0
        end = 0
        res = []
        while end<len(s):
            if freq.get(s[end],None)!=None:
                freq[s[end]]-=1
                if freq[s[end]]==0:counter-=1

            end+=1
            while counter==0:

                if end-beg == len(p):
                    res.append(beg)
                if freq.get(s[beg],None)!=None:
                    freq[s[beg]]+=1
                    if freq[s[beg]]>0:
                        counter+=1
                beg+=1
        return res       

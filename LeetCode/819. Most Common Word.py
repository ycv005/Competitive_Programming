import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=re.findall("[\w]+",paragraph)
        band={}
        for i in banned:
            i=i.lower()
            band[i]=0
        d={}
        mx=1
        mstFreq=paragraph[0].lower()
        for s in paragraph:
            s=s.lower()
            if s not in band:
                if s not in d:
                    d[s]=1
                else:
                    d[s]+=1
                if d[s]>=mx:
                    mx = d[s]
                    mstFreq = s
        return mstFreq

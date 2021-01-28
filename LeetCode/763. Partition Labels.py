from collections import defaultdict


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        freqWithIndexes = defaultdict(list)

        for i, c in enumerate(S):
            freqWithIndexes[c].append(i)

        # print(freqWithIndexes)
        i = 0
        res = []
        while i < len(S):
            c = S[i]
            # elemenet has occured once
            if len(freqWithIndexes[c]) == 1:
                res.append(1)
            # element has occured more than once
            else:
                tmp = freqWithIndexes[c]
                l = tmp[0]
                r = tmp[-1]
                j = l + 1
                while j <= r:
                    c = S[j]
                    if len(freqWithIndexes[c]) > 1:
                        tmp = freqWithIndexes[c]
                        l = min(l, tmp[0])
                        r = max(r, tmp[-1])
                    j += 1
                res.append(r - l + 1)
                i = r
            i += 1

        return res

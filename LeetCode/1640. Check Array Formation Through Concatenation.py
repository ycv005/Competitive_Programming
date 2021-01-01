class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        hmp = {}
        for i, v in enumerate(arr):
            hmp[v] = i
        for i, pcs in enumerate(pieces):
            lastSetIndex = -1
            for j, p in enumerate(pcs):
                if p in hmp:
                    tmpIndex = hmp[p]
                    if lastSetIndex != -1:
                        if tmpIndex != lastSetIndex + 1:
                            # print(tmpIndex, lastSetIndex, p)
                            # print("last set index not matched")
                            return False
                    lastSetIndex = tmpIndex
                else:
                    print("not in dic")
                    return False
        return True

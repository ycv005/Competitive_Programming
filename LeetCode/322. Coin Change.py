class Solution:
    def coinChange(self, coins: List[int], amt: int) -> int:
        if amt==0: return amt
        elif amt<=0: return -1
        mem=[0]*(amt+1)
        for i in range(1,amt+1):
            mnCoin = float("inf")
            for c in coins:
                t=i-c
                if t>=0:
                    currMin = mem[t] +1
                    if currMin>=0 and mnCoin>currMin:
                        mnCoin = currMin
                mem[i]=mnCoin
        if mnCoin==float("inf"): return -1
        return mem[amt]

class Solution:
    def findComplement(self, num: int) -> int:
        s = ''
        for b in bin(num)[2:]:
            if b == '0':
                s += '1'
            else:
                s += '0'
        return int(s, 2)

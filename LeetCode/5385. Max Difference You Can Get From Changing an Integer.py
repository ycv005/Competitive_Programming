class Solution:
    def maxDiff(self, num: int) -> int:
        # cases when no zero present
        numStr = str(num)
        if numStr[0] == '1':
            # we have carefully think on minimum
            mx = numStr.replace(numStr[0], '9')
            v = None
            for d in numStr:
                if d != '1' and d != '0':
                    v = d
                    break
            if v == None:
                mn = numStr
            else:
                mn = numStr.replace(v, '0')
            return int(mx) - int(mn)
        elif numStr[0] == '9':
            # we have to carefully on maximum
            mn = numStr.replace(numStr[0], '1')
            v = None
            for d in numStr:
                if d != '9':
                    v = d
                    break
            if v:
                mx = numStr.replace(v, '9')
            else:
                mx = numStr
            return int(mx) - int(mn)
        else:
            mn = numStr.replace(numStr[0], '1')
            mx = numStr.replace(numStr[0], '9')
            return int(mx) - int(mn)

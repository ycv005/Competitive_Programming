class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        counter = 0
        # push
        stack.append(num[0])
        counter += 1
        while counter < len(num):
            # compare element on top of stack
            if stack[-1]>num[counter]:
                stack.pop(-1)
                k-=1
                if k == 0:
                    # print('time to break')
                    # join things in stack, with left num
                    if len(stack)==0: # case - 102000
                        return str(int(num[counter:]))
                    return ''.join(stack) + num[counter:]
            if len(stack)==0 and num[counter] == '0':
                pass # avoiding leading zeros
            else:
                stack.append(num[counter])
            counter+=1

        # if almost all digit are same, ex - 111111 or 111121111
        while k>0:
            stack.pop()
            k-=1
        return ''.join(stack)

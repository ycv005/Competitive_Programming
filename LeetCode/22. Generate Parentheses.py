def backtrack(S,left, right, wrapper):
    if len(S)==2*wrapper[1]:
        wrapper[0].append(S)
        return
    if left<wrapper[1]:
        backtrack(S+'(',left+1,right,wrapper)
    if right<left:
        backtrack(S+')',left,right+1,wrapper)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        wrapper = [[],n]
        backtrack('',0,0,wrapper)
        return wrapper[0]

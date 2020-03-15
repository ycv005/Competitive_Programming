# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==0:
            return True
        else:
            st=[]
            for i,val in enumerate(s):
                if len(st)==0:
                    if i==0 and val==')' or val=='}' or val==']':
                        return False
                    st.append(val)
                elif st[-1]=='(' and val==')' or st[-1]=='{' and val=='}' or st[-1]=='[' and val==']':
                    st.pop()
                else:
                    st.append(val)
            if len(st)==0:
                return True
            else:
                return False
                    
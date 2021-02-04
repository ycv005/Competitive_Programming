class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        # we will be using stack to store and process the parenthesis
        st = []
        for i, c in enumerate(S):
            if len(st) == 0:
                st.append(c)
            else:
                if c == "(":
                    st.append(c)
                elif c == ")":
                    if st[-1] == "(":
                        a = 1
                        st.pop()
                        if len(st) > 0 and st[-1].isdigit():
                            a += int(st.pop())
                        st.append(str(a))
                    elif st[-1].isdigit():
                        v = int(st.pop())
                        if st[-1] == "(":
                            st.pop()
                            st.append(str(2*v))
                        else:
                            st.append(v)
                        a = 0
                        while len(st) > 0 and st[-1].isdigit():
                            a += int(st.pop())
                        st.append(str(a))

        return int(st.pop())

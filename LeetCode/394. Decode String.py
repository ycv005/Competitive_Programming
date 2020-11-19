class Solution:
    def decodeString(self, s: str) -> str:

        st = []
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                while s[i+1].isdigit():
                    c += s[i+1]
                    i += 1

            if c == "]":
                tmp = ""
                while st[-1] != "[":
                    tmp = st.pop() + tmp
                st.pop()
                val = st.pop()
                st.append(int(val)*tmp)
            else:
                st.append(c)
            i += 1
        return "".join(st)

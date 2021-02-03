# distance to the next big element to right
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        st = []

        # into stack, put index, so that distance as well largest/smallest will be easily compared
        i = len(T) - 1

        # we will traverse the list from behind, becuase, since we need to find the next big
        # element to right. So when we reach to a element from its right side, then we have in our knowledge about
        # bigger element

        # res to store the answer for each n element
        # also, initializing list before while loop, we don't need to insert element at the position
        # by this, we have directed access to an index
        res = [0] * len(T)
        while i >= 0:
            if len(st) == 0:
                res[i] = 0
                st.append(i)
                # print('st empty 1')
            else:
                while len(st) > 0 and T[st[-1]] <= T[i]:
                    # print('st pop', st[-1], T[i])
                    st.pop()
                if len(st) == 0:
                    st.append(i)
                    res[i] = 0
                    # print('st empty 2')
                else:
                    tmp = st[-1] - i
                    st.append(i)
                    res[i] = tmp
                    # print('st somting on top')

            # print(st)

            i -= 1

        return res

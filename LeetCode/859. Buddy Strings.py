class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            seen = set()
            for c in A:
                if c in seen:
                    return True
                seen.add(c)
            return False
        else:
            pairs = []
            for a, b in zip(A, B):
                if a != b:
                    pairs.append(a, b)
                if len(pairs) > 2:
                    return False
            return True if len(pairs) == 2 and pairs[0] == pairs[1][::-1] else False

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = Counter(magazine)
        for c in ransomNote:
            if c not in magazine or magazine[c] == 0:
                return False
            else:
                magazine[c] -=1
        return True

class Solution:
    def firstUniqChar(self, s: str) -> int:
        lst = list(dict.fromkeys(s))
        for letter in lst:
            if s.count(letter) == 1: return s.index(letter)
        return -1 
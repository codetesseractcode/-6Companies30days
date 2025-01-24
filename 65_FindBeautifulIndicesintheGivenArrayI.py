class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        len_a = len(a)
        len_b = len(b)
        idx_a = []
        idx_b = []

        for i in range(0, len(s) - len_a + 1):
            if s[i:i+len_a] == a:
                idx_a.append(i)

        for i in range(0, len(s) - len_b + 1):
            if s[i:i+len_b] == b:
                idx_b.append(i)

        res = []
        if not len(idx_a) or not len(idx_b):
            return res
        i = 0
        j = 0

        while i < len(idx_a) and j < len(idx_b):
            if abs(idx_a[i] - idx_b[j]) <= k:
                res.append(idx_a[i])
                i += 1
            elif idx_a[i] > idx_b[j]:
                j += 1
            else:
                i += 1
            
        return res
        
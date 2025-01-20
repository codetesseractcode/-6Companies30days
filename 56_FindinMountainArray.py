class Solution:
    def sumScores(self, s: str) -> int:
        ans = 0
        n = len(s)
        l, r, i = 0, 0, 1

        z_arr = [0] * n
        for i in range(1, n):
            if i > r:
                l = r = i

                while r < n and s[r] == s[r - l]:
                    r += 1

                z_arr[i] = r - l
                r -= 1
            else:
                k = i - l
                if z_arr[k] < r - i + 1:
                    z_arr[i] = z_arr[k]
                else:
                    l = i
                    while r < n and s[r] == s[r - l]:
                        r += 1
                    z_arr[i] = r - l
                    r -= 1
            ans += z_arr[i]

        ans += n
        return ans
class Solution:
    def waysToReachStair(self, k: int) -> int:
        mem = {}
        def dfs(cur, jump, back):
            if (cur, jump, back) in mem:
                return mem[(cur, jump, back)]
            ways = 0
            if cur == k and (back == 1 or cur == 0) and jump > 0:
                return 1
            elif cur == k:
                ways += 1
            if cur < 0:
                return 0
            nxt = cur + (1 << jump)
            if nxt <= k+1:
                ways += dfs(nxt, jump+1, False)
            if cur > 0 and back == 0:
                ways += dfs(cur-1, jump, True)
            mem[(cur, jump, back)] = ways
            return ways
        return dfs(1, 0, False)
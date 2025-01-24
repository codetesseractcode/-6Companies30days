class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        ans = inf
        for bars in hBars, vBars: 
            cand = cnt = 0 
            for i, x in enumerate(bars): 
                if i and bars[i-1]+1 < x: cnt = 0
                cnt += 1
                cand = max(cand, cnt)
            ans = min(ans, cand+1)
        return ans**2
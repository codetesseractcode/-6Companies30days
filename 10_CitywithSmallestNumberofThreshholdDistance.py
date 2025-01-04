class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[1e9]*n for _ in range(n)]
        for x, y, wt in edges:
            dist[x][y] = wt
            dist[y][x] = wt
        # for i in dist:
        #     print(*i)
        for i in range(n):
            dist[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i != j and dist[i][k] != 1e9 and dist[k][j] != 1e9 and dist[i][j] > dist[i][k]+dist[k][j]:
                        dist[i][j] = dist[i][k]+dist[k][j]
        # for i in dist:
        #     print(*i)
        res = [-1, 1e9]
        for i in range(n):
            cur = 0
            for j in range(n):
                if i!=j and dist[i][j] <= distanceThreshold:
                    cur += 1
            if res[1] >= cur:
                res = [i, cur]
        return res[0]
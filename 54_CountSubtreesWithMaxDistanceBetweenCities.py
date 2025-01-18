class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        
        def fn(edges): 
            """ """
            graph = {} # graph as adjacency list 
            for u, v in edges:
                graph.setdefault(u-1, []).append(v-1) # 0-indexed 
                graph.setdefault(v-1, []).append(u-1)
            group = [None]*n
            dist = [0]*n
            
            def dfs(x, d=0): 
                """ """
                seen.add(x) # mark visited 
                for xx in graph.get(x, []): 
                    dist[x] = max(dist[x], d)
                    if group[xx] is None: group[xx] = group[x]
                    if xx not in seen: dfs(xx, d+1)
                
            for i in range(n): 
                seen = set()
                if group[i] is None: group[i] = i
                dfs(i)
            return group, dist 
        
        ans = {} # answer 
        for r in range(1, len(edges)+1):
            for x in combinations(edges, r): 
                temp = {}
                d = {}
                seen, dist = fn(x)
                for i in range(n): 
                    temp.setdefault(seen[i], []).append(i)
                    if seen[i] not in d: d[seen[i]] = dist[i]
                    else: d[seen[i]] = max(d[seen[i]], dist[i])
                for k, v in temp.items(): 
                    if len(v) > 1: 
                        ans.setdefault(d[k], set()).add(tuple(sorted(v)))
        return [len(ans.get(x, set())) for x in range(1, n)]
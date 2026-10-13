class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visit = set()
        def dfs(curr, prev):
            visit.add(curr)
            for n in graph[curr]:
                if n == prev or n in visit:
                    continue
                dfs(n, curr)
        
        res = 0
        for i in range(n):
            if i in visit:
                continue
            res += 1
            dfs(i, -1)
        
        return res
            
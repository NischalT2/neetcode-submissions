class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]

        for curr, neigh in edges:
            graph[curr].append(neigh)
            graph[neigh].append(curr)
        
        visit = set()
        def dfs(curr, parent):
            if curr in visit:
                return False
            
            visit.add(curr)
            for neigh in graph[curr]:
                if neigh == parent:
                    continue
                
                if not dfs(neigh, curr): 
                    return False
            
            return True
        
        if not dfs(0, -1): return False

        return len(visit) == n
            

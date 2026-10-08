class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = []
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(i, j, curr):
            if (i, j) in visited or i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == "0":
                return False

            if grid[i][j] == "1":
                if curr == 0:
                    res.append((i, j))
                visited.add((i, j))
                dfs(i-1, j, curr + 1)
                dfs(i+1, j, curr + 1)
                dfs(i, j-1, curr + 1)
                dfs(i, j+1, curr + 1)

            return True
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, 0)
        
        return len(res)

            
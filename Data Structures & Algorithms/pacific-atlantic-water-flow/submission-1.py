class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()

        def dfs(i, j, visited, prev):
            if (i, j) in visited or i < 0 or j < 0 or i == ROWS or j == COLS or prev > heights[i][j]:
                return
            visited.add((i, j))

            dfs(i-1, j, visited, heights[i][j])
            dfs(i, j-1, visited, heights[i][j])
            dfs(i+1, j, visited, heights[i][j])
            dfs(i, j+1, visited, heights[i][j])
        
        for j in range(COLS):
            dfs(0, j, pac, heights[0][j])
            dfs(ROWS-1, j, atl, heights[ROWS-1][j])
        
        for i in range(ROWS):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, COLS-1, atl, heights[i][COLS-1])
        
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        
        return res

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        word_len = len(word) - 1
        visited = set()

        def backtrack(i, j, curr):
            if curr == len(word):
                return True

            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[curr] or (i, j) in visited:
                return False
            
            visited.add((i, j))
            res = backtrack(i-1, j, curr+1) or backtrack(i+1, j, curr+1) or backtrack(i, j-1, curr+1) or backtrack(i, j+1, curr+1)
            visited.remove((i, j))
            return res
        
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0): return True
        
        return False

        

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        three = defaultdict(list)

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != ".":
                    row_map = row // 3
                    col_map = col // 3

                    if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in three[(row_map, col_map)]:
                        return False
                    
                    rows[row].append(board[row][col])
                    cols[col].append(board[row][col])
                    three[(row_map, col_map)].append(board[row][col])
            
        return True
                    

            



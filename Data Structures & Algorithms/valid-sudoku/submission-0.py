class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashcol = {}
        box = [set() for _ in range(9)]
        for row in range(len(board)):
            seen_in_row = set()
            for col in range(len(board)):
                curr_val = board[row][col]
                if curr_val.isdigit():
                    if col not in hashcol:
                        hashcol[col] = set()
                    if curr_val in hashcol[col] or curr_val in seen_in_row:
                        return False
                    hashcol[col].add(curr_val)
                    seen_in_row.add(curr_val)

                    box_index = (row // 3) * 3 + (col // 3)
                    if curr_val in box[box_index]:
                        return False
                    box[box_index].add(curr_val)
        return True

                

                    

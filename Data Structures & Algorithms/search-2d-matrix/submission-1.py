class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute force
        for row in matrix:
            for col in row:
                if col == target:
                    return True
        
        return False
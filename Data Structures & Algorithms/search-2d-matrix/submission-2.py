class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        firstRow, lastRow = 0, len(matrix) - 1
        while firstRow <= lastRow:
            midRow = (firstRow + lastRow) // 2
            if matrix[midRow][-1] < target:
                firstRow = midRow + 1
            elif matrix[midRow][0] > target:
                lastRow = midRow - 1
            else:
                l, r = 0, len(matrix[midRow])-1
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[midRow][mid] > target:
                        r = mid - 1
                    elif matrix[midRow][mid] < target:
                        l = mid + 1
                    else:
                        return True
                return False
        return False
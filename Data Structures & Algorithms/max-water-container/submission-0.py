class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        left, right = 0, len(heights) - 1

        while left < right:
            cur_area = (right - left) * min(heights[left], heights[right])
            largest = max(largest, cur_area)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return largest
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0;

        res, l, r, = 0, 0, len(height) - 1
        max_l, max_r = height[l], height[r]

        while l < r:
            if max_l <= max_r:
                l += 1
                curr_water = (min(max_l, max_r) - height[l])
                if curr_water > 0:
                    res += curr_water
                max_l = max(height[l], max_l)
            else:
                r -= 1
                curr_water = (min(max_l, max_r) - height[r])
                if curr_water > 0:
                    res += curr_water
                max_r = max(height[r], max_r)
            
        return res
            
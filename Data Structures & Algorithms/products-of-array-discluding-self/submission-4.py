class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        left, right = 1, 1

        for n in range(len(nums)):
            res[n] *= left
            left *= nums[n]
            
        
        for n in range(len(nums)-1, -1, -1):
            res[n] *= right
            right *= nums[n]
        
        return res
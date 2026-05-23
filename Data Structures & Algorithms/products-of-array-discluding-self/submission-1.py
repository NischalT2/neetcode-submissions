class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
        
        right = 1
        for j in range(len(nums)-1, -1, -1):
            output[j] *= right
            right *= nums[j]
        
        return output
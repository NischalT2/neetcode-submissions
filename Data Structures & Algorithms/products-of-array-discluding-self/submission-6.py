class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix, suffix = 1, 1

        for i, n in enumerate(nums):
            res[i] *= prefix
            prefix *= n
        
        for j in range(len(nums)-1, -1, -1):
            res[j] *= suffix
            suffix *= nums[j]
        
        return res
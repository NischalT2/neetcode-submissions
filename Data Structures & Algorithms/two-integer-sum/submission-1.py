class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen and seen[diff] != i:
                return [seen[diff], i]
            
            seen[nums[i]] = i
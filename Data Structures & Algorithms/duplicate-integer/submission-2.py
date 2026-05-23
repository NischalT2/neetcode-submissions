class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            seen.add(i)
        
        return len(seen) != len(nums)
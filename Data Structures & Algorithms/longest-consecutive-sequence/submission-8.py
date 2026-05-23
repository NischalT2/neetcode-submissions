class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for i in nums:
            if i - 1 not in nums:
                counter = 0
                while i + counter in nums:
                    counter += 1
                res = max(res, counter)
        
        return res
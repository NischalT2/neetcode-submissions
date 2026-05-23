class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for n in nums:
            curr_max = 0
            if n - 1 in nums:
                continue

            j = n
            while j in nums:
                curr_max += 1
                j += 1

            res = max(res, curr_max)
        
        return res
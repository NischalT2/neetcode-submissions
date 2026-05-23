class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for n in nums:
            i = 0
            if n - 1 not in nums:
                while n + i in nums:
                    i += 1
            res = max(res, i)
        return res


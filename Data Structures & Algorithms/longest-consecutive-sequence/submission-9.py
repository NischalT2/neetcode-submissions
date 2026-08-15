class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in nums:
                curr_count = n
                curr_res = 0
                while curr_count in nums:
                    curr_res += 1
                    curr_count += 1
                res = max(res, curr_res)
        
        return res
            
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for n in nums:
            curr_max = 0
            if n - 1 not in num_set:
                i = 0
                while n + i in nums:
                    curr_max += 1
                    i += 1
                
            res = max(res, curr_max)

        return res
                    
            

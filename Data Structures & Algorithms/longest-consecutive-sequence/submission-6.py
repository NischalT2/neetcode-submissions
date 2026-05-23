class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        nums = set(nums)

        for n in nums:
            if n-1 in nums:
                continue
            else:
                j = 0
                while n+j in nums:
                    j += 1
                res = max(j, res)
    
        return res
                

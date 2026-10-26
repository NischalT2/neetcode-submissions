class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums) + 1)

        for i in range(len(nums)):
            curr_max = dp[i]
            for j in range(i):
                if nums[i] > nums[j]:
                    curr_max = max(curr_max, dp[i] + dp[j])
            
            dp[i] = curr_max
        
        res = 0
        for n in dp:
            res = max(res, n)  

        return res
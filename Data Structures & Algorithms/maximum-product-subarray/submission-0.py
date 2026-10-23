class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1

        for n in nums:
            tmp = currMax * n
            currMax = max(tmp, n * currMin, n)
            currMin = min(tmp, n * currMin, n)
            res = max(res, currMax)

        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for n in range(len(nums)):
            if n > 0 and nums[n] == nums[n-1]:
                continue
            
            l, r = n + 1, len(nums) - 1
            while l < r:
                t_sum = nums[n] + nums[l] + nums[r]

                if t_sum < 0:
                    l += 1
                elif t_sum > 0:
                    r -= 1
                else:
                    res.append([nums[n], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1 

        return res

                        

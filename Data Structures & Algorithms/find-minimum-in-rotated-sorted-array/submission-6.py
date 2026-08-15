class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[r]:
                l  = mid + 1
            else:
                r = mid - 1
        
        return res


    
    # 3, 4, 5, 6, 1, 2
    # l     m        r
    # 

    # 1, 2, 3, 4, 5, 6
    # 6, 1, 2, 3, 4, 5
    # 5, 6, 1, 2, 3, 4
    # 4, 5, 6, 1, 2, 3
    # 3, 4, 5, 6, 1, 2
    # 2, 3, 4, 5, 6, 1
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob1(nums[1:]), self.rob1(nums[:-1]))
    
    def rob1(self, subnums):
        prev, curr = 0, 0
        
        for i in subnums:
            temp = max(curr, prev + i)
            prev = curr
            curr = temp
        
        return curr

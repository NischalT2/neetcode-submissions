class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.path = []
        self.res = []

        def backtrack(start):
            for i in range(start, len(nums)):
                self.path.append(nums[i])
                path_sum = sum(self.path)

                if path_sum == target:
                    self.res.append(self.path.copy())
                elif path_sum > target:  
                    self.path.pop()
                    continue
                backtrack(i)
                self.path.pop()
            
        backtrack(0)
        return self.res
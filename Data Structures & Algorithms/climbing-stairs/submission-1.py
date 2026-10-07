class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 0, 1

        for i in range(n):
            tmp = curr
            curr += prev
            prev = tmp
        
        return curr
        
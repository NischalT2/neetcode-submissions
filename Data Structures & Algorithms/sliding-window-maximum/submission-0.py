class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        left = right = 0

        while right < len(nums):
            while dq and nums[right] > nums[dq[-1]]:
                dq.pop()
            dq.append(right)

            if left > dq[0]:
                dq.popleft()

            if (right + 1) >= k:
                res.append(nums[dq[0]])
                left += 1
            right += 1
        
        return res

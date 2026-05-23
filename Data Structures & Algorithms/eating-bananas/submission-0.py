class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2

            total_time = 0
            for n in piles:
                total_time += math.ceil(n/float(mid))

            if total_time <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for c in count:
            bucket[count[c]].append(c)

        for i in range(len(bucket) - 1, -1, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) >= k:
                    return res
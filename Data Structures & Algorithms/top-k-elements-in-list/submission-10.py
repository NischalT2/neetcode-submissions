class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = defaultdict(int)
        bucket = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for c in count:
            bucket[count[c]].append(c)
        
        for l in range(len(bucket) - 1, -1, -1):
            for m in bucket[l]:
                res.append(m)
                if len(res) >= k:
                    return res
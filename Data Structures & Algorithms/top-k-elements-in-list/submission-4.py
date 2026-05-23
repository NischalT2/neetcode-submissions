class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = defaultdict(int)
        bucket = [[] for _ in range(len(nums)+1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for i in count:
            bucket[count[i]].append(i)

        for j in range(len(bucket) - 1, 0, -1):
            for l in bucket[j]:
                res.append(l)
            if len(res) == k:
                return res
            
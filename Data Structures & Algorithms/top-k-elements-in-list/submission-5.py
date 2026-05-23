class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        bucket = [[] for _ in range(len(nums) + 1)] 
        res = []

        for i in nums:
            count[i] = count.get(i, 0) + 1

        for j in count:
            bucket[count[j]].append(j)
        
        for z in range(len(bucket)- 1, -1, -1):
            for l in bucket[z]:
                res.append(l)
                if len(res) == k:
                    return res

        
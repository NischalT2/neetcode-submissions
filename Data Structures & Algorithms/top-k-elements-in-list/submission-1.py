class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        tot_count = [[] for _ in range(len(nums) + 1)]
        res = []

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        for j in count:
            tot_count[count[j]].append(j)

        for i in range(len(tot_count) -1, 0, -1):
            for n in tot_count[i]:
                res.append(n)
                if len(res) == k:
                    return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Use bucket sort but a modification
        #First count the number of times each number appears
        count = defaultdict(int)
        order = [[] for _ in range(len(nums) + 1)] 
        res = []
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for c in count:
            order[count[c]].append(c)
        
        for n in range(len(order) - 1, 0, -1):
            for i in order[n]:
                res.append(i)
            if len(res) == k:
                return res
                
        
        
        
            

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = defaultdict(int)

        for num in nums:
            output[num] += 1

        sorted_output = [item[0] for item in sorted(output.items(), key=lambda item: item[1], reverse=True)]
        return sorted_output[:k]
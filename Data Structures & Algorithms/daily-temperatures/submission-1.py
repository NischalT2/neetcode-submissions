class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                last = stack.pop()
                res[last[1]] = (i - last[1])
            stack.append((t, i))
        
        return res


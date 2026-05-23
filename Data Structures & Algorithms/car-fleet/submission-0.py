class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair_arr = []
        for  i in range(len(position)):
            pair_arr.append([position[i], speed[i]])
        
        stack = []
        for p, s in sorted(pair_arr)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)



class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pos_speed = []
        for i in range(len(position)):
            pos_speed.append([position[i], speed[i]])
        
        pos_speed = sorted(pos_speed)

        for pos, speed in reversed(pos_speed):
            steps = (target - pos) / speed
            if not stack or steps > stack[-1]:
                stack.append(steps)
        
        return len(stack)

        
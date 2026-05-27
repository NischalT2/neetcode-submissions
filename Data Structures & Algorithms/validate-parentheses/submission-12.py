class Solution:
    def isValid(self, s: str) -> bool:
        matches = {"]": "[", 
                    ")": "(", 
                    "}":"{"}
        stack = []

        for c in s:
            if c not in matches:
                stack.append(c)
            else:
                if not stack or stack.pop() != matches[c]:
                    return False
        
        return True if not stack else False

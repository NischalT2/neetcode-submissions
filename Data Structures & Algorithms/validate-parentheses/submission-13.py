class Solution:
    def isValid(self, s: str) -> bool:
        matches = {")": "(", "}": "{", "]":"["}

        stack = []
        for c in s:
            if not stack and c in matches:
                return False
            
            if c not in matches:
                stack.append(c)
            else:
                if matches[c] != stack.pop():
                    return False
            
        return True if not stack else False
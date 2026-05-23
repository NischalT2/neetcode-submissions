class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c not in closeToOpen:
                stack.append(c)
            else:
                if not stack or closeToOpen[c] != stack.pop():
                    return False
        
        return True if not stack else False
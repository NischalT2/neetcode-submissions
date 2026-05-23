class Solution:
    def isValid(self, s: str) -> bool:
        matches = {")":"(", "}": "{", "]":"["}
        stack = []

        for c in s:
            if c in matches:
                if not stack or stack.pop() != matches[c]:
                    return False
            elif c in matches.values():
                stack.append(c)
        
        return True if not stack else False
            
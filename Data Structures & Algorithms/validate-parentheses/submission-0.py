class Solution:
    def isValid(self, s: str) -> bool:
        hm = {")":"(", "}":"{", "]":"["}
        stack = []

        for char in s:
            if char in hm.values():
                stack.append(char)
            elif char in hm:
                if not stack or stack.pop() != hm[char]:
                    return False
        
        return True if not stack else False
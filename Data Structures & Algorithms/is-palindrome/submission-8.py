class Solution:
    def isPalindrome(self, s: str) -> bool:
        norm_s = ""
        for c in s:
            if c.isalnum() and c != " ":
                norm_s += c.lower()
        
        l, r = 0, len(norm_s) - 1
        while l <= r:
            if norm_s[l] != norm_s[r]:
                return False
            l += 1
            r -= 1

        return True

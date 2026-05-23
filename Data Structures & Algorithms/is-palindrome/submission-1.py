class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""
        for c in s:
            if c.isalnum():
                s_new += c.lower()
        print(s_new)

        l, r = 0, len(s_new) - 1
        while l <= r:
            if s_new[l] != s_new[r]:
                return False
            l += 1
            r -= 1
        
        return True
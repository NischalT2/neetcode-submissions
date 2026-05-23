class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l, res = 0, 0
        
        for c in range(len(s)):
            while s[c] in window:
                window.remove(s[l])
                l += 1
            window.add(s[c])
            res = max(res, (c - l + 1))
        
        return res



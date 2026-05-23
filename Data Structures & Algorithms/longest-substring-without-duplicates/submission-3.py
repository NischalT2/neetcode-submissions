class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        seen = set()

        for c in range(len(s)):
            while s[c] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[c])

            res = max(res, c - l + 1)
        
        return res
            


            
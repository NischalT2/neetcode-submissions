class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        n = len(s)

        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                currLen = r - l + 1
                if currLen > resLen:
                    res = s[l:r+1]
                    resLen = currLen
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                currLen = r - l + 1
                if currLen > resLen:
                    res = s[l:r+1]
                    resLen = currLen
                l -= 1
                r += 1
            
        return res
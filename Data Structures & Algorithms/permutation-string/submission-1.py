class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        len_s1 = len(s1)
        sorted_s1 = sorted(s1)
        l, r = 0, len_s1
        while r <= len(s2):
            curr = sorted(s2[l:r])
            if curr == sorted_s1:
                return True
            l += 1
            r += 1
        
        return False
            